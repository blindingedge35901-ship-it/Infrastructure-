"""Lossless ingestion primitives for legacy NBI CSV exports.

This module deliberately performs no semantic field conversion. Identifiers,
codes, dates, and numeric-looking values remain source strings until a
versioned, field-specific normalization rule is applied downstream.

The reader is lazy: it opens the source only when iteration begins, closes it
when iteration completes or is closed, and checks that the file fingerprint
has not changed between manifest creation and a complete read.
"""
from __future__ import annotations

import csv
import hashlib
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Mapping


class NbiCsvError(ValueError):
    """Raised when an NBI CSV file cannot be read without structural ambiguity."""


@dataclass(frozen=True)
class NbiCsvManifest:
    path: str
    sha256: str
    byte_count: int
    row_count: int | None
    headers: tuple[str, ...]
    encoding: str


def file_fingerprint(path: str | Path, chunk_size: int = 1024 * 1024) -> tuple[str, int]:
    """Return SHA-256 and byte count for the exact current file contents."""
    digest = hashlib.sha256()
    byte_count = 0
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(chunk_size), b""):
            digest.update(chunk)
            byte_count += len(chunk)
    return digest.hexdigest(), byte_count


def sha256_file(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    """Compatibility helper returning only the file SHA-256 digest."""
    return file_fingerprint(path, chunk_size)[0]


def read_nbi_csv(
    path: str | Path,
    *,
    encoding: str = "utf-8-sig",
    required_fields: tuple[str, ...] = (
        "YEAR",
        "STATE_CODE_001",
        "STRUCTURE_NUMBER_008",
    ),
) -> tuple[NbiCsvManifest, Iterator[dict[str, str]]]:
    """Return a manifest and one-pass iterator of raw string rows.

    Header matching is exact by design. If a portal export uses different
    display headers, callers must provide an explicit, documented profile;
    this function will not guess aliases or silently rename columns. The
    iterator must be consumed fully for the end-of-read fingerprint check.
    """
    source = Path(path)
    if not source.is_file():
        raise NbiCsvError(f"CSV source does not exist: {source}")

    digest, byte_count = file_fingerprint(source)
    with source.open("r", encoding=encoding, newline="") as stream:
        reader = csv.reader(stream)
        headers = tuple(next(reader, ()))

    if not headers:
        raise NbiCsvError("CSV has no header row")
    if len(set(headers)) != len(headers):
        raise NbiCsvError("CSV contains duplicate column headers")
    missing = [field for field in required_fields if field not in headers]
    if missing:
        raise NbiCsvError(f"CSV is missing required source fields: {missing}")

    def rows() -> Iterator[dict[str, str]]:
        with source.open("r", encoding=encoding, newline="") as stream:
            reader = csv.DictReader(
                stream, restkey="__EXTRA_FIELDS__", restval=None
            )
            if tuple(reader.fieldnames or ()) != headers:
                raise NbiCsvError("CSV header changed between manifest and row read")
            for line_number, row in enumerate(reader, start=2):
                if row.get("__EXTRA_FIELDS__") is not None:
                    raise NbiCsvError(
                        f"CSV row {line_number} has more values than the header"
                    )
                if any(
                    value is None
                    for key, value in row.items()
                    if key != "__EXTRA_FIELDS__"
                ):
                    raise NbiCsvError(
                        f"CSV row {line_number} has fewer values than the header"
                    )
                row.pop("__EXTRA_FIELDS__", None)
                yield {key: value for key, value in row.items()}
        final_digest, final_byte_count = file_fingerprint(source)
        if (final_digest, final_byte_count) != (digest, byte_count):
            raise NbiCsvError("CSV source changed during ingestion; discard this read")

    manifest = NbiCsvManifest(
        path=str(source),
        sha256=digest,
        byte_count=byte_count,
        row_count=None,
        headers=headers,
        encoding=encoding,
    )
    return manifest, rows()


def profile_nbi_rows(
    rows: Iterator[Mapping[str, str]],
    *,
    year_field: str = "YEAR",
    state_field: str = "STATE_CODE_001",
    structure_field: str = "STRUCTURE_NUMBER_008",
) -> dict[str, object]:
    """Count rows by year/state and flag duplicate source keys without dropping them."""
    by_year: Counter[str] = Counter()
    by_year_state: Counter[tuple[str, str]] = Counter()
    source_keys: Counter[tuple[str, str, str]] = Counter()
    blank_identifier_rows = 0
    total = 0

    for row in rows:
        total += 1
        year = row.get(year_field, "")
        state = row.get(state_field, "")
        structure = row.get(structure_field, "")
        by_year[year] += 1
        by_year_state[(year, state)] += 1
        if not structure.strip():
            blank_identifier_rows += 1
        else:
            source_keys[(year, state, structure)] += 1

    duplicate_keys = {
        "|".join(key): count
        for key, count in source_keys.items()
        if count > 1
    }
    return {
        "row_count": total,
        "rows_by_year": dict(sorted(by_year.items())),
        "rows_by_year_state": {
            "|".join(key): count
            for key, count in sorted(by_year_state.items())
        },
        "blank_identifier_rows": blank_identifier_rows,
        "duplicate_source_keys": duplicate_keys,
        "duplicate_source_key_count": len(duplicate_keys),
    }
