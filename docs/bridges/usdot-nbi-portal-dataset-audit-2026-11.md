# USDOT National Bridge Inventory Portal Dataset Audit — 2026-11-27

## Status

**Result: official dataset identified and its published schema metadata inspected; bulk row export and raw-record parsing remain blocked in this environment.**

This audit concerns the USDOT Data Portal dataset titled **National Bridge Inventory**, published by the Federal Highway Administration (FHWA), dataset identifier `pced-83j4`.

- Dataset landing page: https://data.transportation.gov/Roadways-and-Bridges/National-Bridge-Inventory/pced-83j4
- Data.gov catalog record: https://catalog.data.gov/dataset/national-bridge-inventory-2839c
- Column metadata: https://data.transportation.gov/api/views/pced-83j4/columns.json
- CSV download endpoint: https://data.transportation.gov/api/v3/views/pced-83j4/export.csv?accessType=DOWNLOAD
- JSON download endpoint: https://data.transportation.gov/api/v3/views/pced-83j4/query.json?accessType=DOWNLOAD
- XML download endpoint: https://data.transportation.gov/api/v3/views/pced-83j4/query.xml?accessType=DOWNLOAD

The Data.gov catalog identifies FHWA as publisher, public access, and a dataset update date of 2026-11-02. Its temporal metadata describes 2024-01-01 through 2025-01-01. The portal landing page likewise labels the dataset temporal applicability 2024/2025.

## Record-count metadata

The public column metadata reports:

| Year | Cached record count |
|---|---:|
| 2024 | 623,218 |
| 2025 | 624,193 |
| Total | 1,247,411 |

The 2025 cached record count equals the FHWA-published 2025 national highway bridge count of 624,193. This is a strong reconciliation lead, but it is not an independent row-level recount: the count is portal-provided cached metadata, and the full export has not yet been acquired and parsed.

The 2024 count must be checked against the matching official FHWA 2024 published baseline and its precise scope before treating it as reconciled.

## Initial schema observations

The column metadata endpoint was successfully opened and exposes 7,800 lines of JSON metadata. Each column entry can include a display name, field name, data type, description, position, null/non-null counts, common values, and other cached statistics.

The first fields include:

- `YEAR` — numeric year of record.
- `STATE_CODE_001` — numeric state code.
- `STRUCTURE_NUMBER_008` — text structure number.
- `RECORD_TYPE_005A` — numeric inventory route/record type.
- Route signing prefix, service level, route number and direction.
- Highway district, county code, place code, and feature description.

The cached metadata reports `STRUCTURE_NUMBER_008` as text, which is the correct semantic treatment for an identifier. However, some cached example values are rendered in scientific notation (for example, `1E+14`). This may be a metadata display/cache representation rather than the raw export value. It is not yet proof that source identifiers have been corrupted. **Do not ingest from cached examples.** Inspect raw CSV/JSON values and compare them with official FHWA records before deciding whether the export preserves identifier fidelity.

The metadata reports `RECORD_TYPE_005A` as value 1 for all 1,247,411 rows. This is consistent with the dataset description that it contains highway bridge records, but the actual export and scope rules still need direct validation. Do not reuse the legacy Item 5A filter as a universal definition outside the documented historical context.

## Acquisition attempts and limitations

- Opening the USDOT portal landing page yielded only a minimal rendered page in the web viewer.
- The column metadata JSON endpoint was accessible and inspected.
- Opening the bulk JSON query/download endpoint through the web viewer failed with a cache-miss error.
- A direct container download attempt for the CSV endpoint failed.
- A filtered Socrata-style row query for Colorado was also inaccessible through the web viewer.
- No raw CSV, JSON or XML records were acquired in this attempt. No row-level parser, checksum, Colorado subset count, or identifier validation has been completed.

These are retrieval limitations of the current environment, not evidence that the public dataset itself is unavailable.

## Implications for the bridge model

1. This dataset is a promising official, bulk-access route for 2024–2025 legacy NBI records and could support a reproducible baseline ingestion test if the raw file can be retrieved.
2. It does not replace the InfoBridge All Years export for multi-year longitudinal identity and inspection-history reconstruction.
3. Keep source vintage and year of record separate. A single portal dataset containing two annual cohorts is not itself a longitudinal event table.
4. Preserve raw field names, values, types, and source positions. Do not numeric-cast structure numbers, route numbers, county codes, place codes, or other identifiers.
5. Verify the exact 2024 and 2025 scopes, duplicate behavior, missingness, and published totals before using the portal dataset for model calibration.
6. Keep legacy NBI and 2026+ SNBI as separate source eras. This portal's described temporal coverage is 2024/2025; it is not evidence of SNBI transition-era coverage.
7. The next viable step is obtaining the actual CSV or JSON through a browser session or user-provided official download, then checksum/register it, inspect raw records, and independently reproduce year/state counts.

## Source references

- FHWA NBI download page: https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm
- FHWA 2026 download page: https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm
- Data.gov catalog metadata: https://catalog.data.gov/dataset/national-bridge-inventory-2839c
- USDOT dataset landing page: https://data.transportation.gov/Roadways-and-Bridges/National-Bridge-Inventory/pced-83j4
- USDOT column metadata: https://data.transportation.gov/api/views/pced-83j4/columns.json
- FHWA InfoBridge Data portal: https://infobridge.fhwa.dot.gov/Data

## Research classification

- **Source-reported:** dataset publisher, public-access designation, temporal applicability, metadata fields, cached record counts, cached data types and null counts.
- **Derived:** 2024 + 2025 cached counts sum to 1,247,411; 2025 cached count equals the FHWA-published 2025 national count.
- **Unresolved:** raw identifier fidelity, exact row-level scope, duplicates, state/year count reproduction, and bulk acquisition.
- **Not established:** that the portal export is suitable for production ingestion or predictive calibration.
