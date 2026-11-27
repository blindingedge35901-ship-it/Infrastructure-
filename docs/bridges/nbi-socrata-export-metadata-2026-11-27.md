# NBI Socrata Export Metadata and Header Verification — 2026-11-27

## Verified portal metadata

The FHWA National Bridge Inventory dataset page identifies:
- Dataset ID: `pced-83j4`
- Dataset title: National Bridge Inventory
- Publisher / data provider: Federal Highway Administration, Office of Bridges and Structures
- Dataset update and metadata update: 2026-11-02
- Temporal applicability: 2024/2025
- Row unit: Bridge
- Column count: 124
- Rights: CC0 1.0; Public Domain U.S. Government
- Source link: FHWA NBI ASCII archive page

The portal's displayed column metadata explicitly lists the following source column names and API field names:
| Portal column name | Description | API field name | Data type |
|---|---|---|---|
| YEAR | Year of Record | year | Number |
| STATE_CODE_001 | State Code | state_code_001 | Number |
| STRUCTURE_NUMBER_008 | Structure Number | structure_number_008 | Text |

This confirms that the three exact header names currently required by `read_nbi_csv` match the portal's displayed column-name convention. It also independently confirms that structure number is a text field and must not be numeric-coerced.

## Important distinction: update date vs temporal coverage

The dataset's November 2, 2026 update date is not evidence that the rows represent 2026 bridge observations. The portal explicitly lists temporal applicability as 2024/2025. Treat this as a recent portal publication/update containing 2024/2025 vintage data, not as a 2026 condition baseline or a historical annual panel.

The FHWA's separate annual NBI archive remains necessary for the long time series. Legacy ASCII files and 2026+ SNBI JSON files must continue to be handled as distinct source eras.

## Implications for ingestion

1. The CSV reader's required header names are consistent with the portal's displayed column-name metadata.
2. The portal reports `STRUCTURE_NUMBER_008` as Text; preserve the exact token including leading zeroes.
3. The portal also exposes lowercase API field names. Do not assume the full-export CSV uses API field names; inspect the downloaded file's actual header row before parsing. The human-readable export may use displayed column names.
4. Record both portal update timestamp and row-level YEAR. They answer different questions.
5. The portal metadata is not a substitute for a raw-file fingerprint, actual row count, duplicate audit, or aggregate reconciliation.

## Source

FHWA National Bridge Inventory portal dataset page:
https://data.transportation.gov/Roadways-and-Bridges/National-Bridge-Inventory/pced-83j4

## Evidence status

Metadata facts above are portal-reported. No CSV export bytes have yet been acquired in this environment. No row-level values have been parsed or independently recounted.
