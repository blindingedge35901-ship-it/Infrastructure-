# Bridge data ingestion primitives

`nbi_csv.py` provides a deliberately lossless first-pass reader for legacy
NBI CSV exports. It preserves every source field as text, requires explicit
header names, fingerprints the source file, rejects row-width/header
ambiguities, and profiles year/state counts and duplicate source keys without
silently dropping records.

It does **not**:
- infer physical bridge identity across years;
- map legacy NBI fields to SNBI;
- convert codes, dates, units, or identifiers;
- validate engineering semantics;
- claim that a portal export reproduces FHWA totals.

The first test fixture is synthetic and tests parser behavior only. A real
FHWA export is still required before this reader can be considered tested
against the actual portal's CSV dialect and headers.
