# NBI Public Export Access Route — SODA3 Review (2026-11-27)

## Finding

The FHWA-published National Bridge Inventory Socrata dataset is public. Its Data.gov catalog record identifies the FHWA as publisher, lists CC0 1.0 / U.S. Government work rights, and gives the dataset identifier `pced-83j4`. The catalog record was modified 2026-11-02 and describes temporal applicability as 2024/2025.

The dataset's cataloged full-export endpoint is:

`https://data.transportation.gov/api/v3/views/pced-83j4/export.csv?accessType=DOWNLOAD`

Socrata's current SODA3 documentation distinguishes full exports from filtered queries:
- Full exports from public datasets do not require authentication.
- Filtered exports and query endpoints require an app token or another authentication method.
- App tokens can be registered through a Socrata profile; the developer documentation describes their use for higher request limits, not as a paid data license.

This corrects the earlier working assumption that all useful access to this dataset would require an app token. The unfiltered export endpoint is the preferred no-cost route to test first. Do not use the filtered query endpoint until an app token is available.

## Retrieval test in this environment

On 2026-11-27, the full-export URL was tested through the available web page opener and direct container download/runtime request. The web opener returned an inaccessible/internal error; the container request failed at DNS resolution. No response body, HTTP status from the data host, or CSV bytes were obtained.

This is an environment/network retrieval failure, not evidence that FHWA or Socrata denies public access. The dataset's public export remains documented and should be retried from a normal browser or a network-enabled environment.

## Data lineage and scope caveats

- Dataset ID: `pced-83j4`.
- Publisher: FHWA Office of Bridges and Structures.
- Dataset last updated: 2026-11-02.
- Temporal applicability in catalog: 2024/2025.
- Do not treat this single portal dataset as a historical annual panel. FHWA separately publishes annual NBI files; 1992–2025 legacy ASCII files and 2026+ SNBI-format files have different structures and transition rules.
- FHWA's 2026 download page reports 624,939 highway bridges nationally and 9,018 in Colorado. These are FHWA-published totals, not counts independently reproduced from downloaded records.

## Recommended next retrieval sequence

1. Retry the full CSV export from a normal browser or network-enabled environment; do not append filters.
2. Save the untouched export and record retrieval timestamp, byte count, SHA-256, response headers, and exact URL.
3. Inspect the actual CSV header row before mapping columns. The existing parser requires explicit `YEAR`, `STATE_CODE_001`, and `STRUCTURE_NUMBER_008` headers; these have not yet been verified against the portal export.
4. Run the lossless CSV reader and row profiler, preserving identifiers as strings and retaining duplicates for audit.
5. Reconcile year/state counts and condition/area totals against FHWA's published tables before any longitudinal modeling.
6. Acquire historical annual FHWA files separately and preserve source vintage/layout; do not assume the Socrata export is a substitute for the 1992–2025 archive.

## Sources

- FHWA / Data.gov catalog record: https://catalog.data.gov/dataset/national-bridge-inventory-2839c
- Dataset landing page: https://data.transportation.gov/Roadways-and-Bridges/National-Bridge-Inventory/pced-83j4
- Full CSV export: https://data.transportation.gov/api/v3/views/pced-83j4/export.csv?accessType=DOWNLOAD
- Socrata SODA3 announcement: https://support.socrata.com/hc/en-us/articles/34730618169623-Introducing-the-new-SODA3-API
- SODA3 usage and authentication: https://support.socrata.com/hc/en-us/articles/43491231777047-Using-the-SODA3-API
- Socrata application-token documentation: https://dev.socrata.com/docs/app-tokens
- FHWA annual NBI download page: https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm
- FHWA 2026 download page: https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm

## Status

A viable documented no-token full-export route has been identified. Retrieval is not yet complete. No raw records have been downloaded, parsed, or independently reconciled in this environment.
