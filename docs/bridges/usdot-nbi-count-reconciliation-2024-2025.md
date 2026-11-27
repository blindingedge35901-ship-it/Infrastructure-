# USDOT NBI Portal — Published Count Reconciliation Audit (2024–2025)

Date: 2026-11-27

## Purpose

Cross-check the USDOT Data Portal's cached annual row counts for the FHWA National Bridge Inventory dataset (`pced-83j4`) against FHWA's own published annual condition tables. This is a metadata/aggregate reconciliation, not a raw-row validation.

## Dataset metadata

USDOT dataset: https://data.transportation.gov/Roadways-and-Bridges/National-Bridge-Inventory/pced-83j4

- Publisher: Federal Highway Administration.
- Last updated: 2026-11-02.
- Temporal applicability: 2024/2025.
- Rows described as bridges; 124 columns.
- API field names and data types are published on the dataset landing page and in the column metadata endpoint: https://data.transportation.gov/api/views/pced-83j4/columns.json
- Cached year counts: 2024 = 623,218; 2025 = 624,193; total = 1,247,411.

## FHWA aggregate cross-check

### 2024

FHWA's 2024 Bridge Condition by Highway System page (dated June 15, 2024) reports:

- National all-bridge count: 623,218.
- Good: 274,859.
- Fair: 306,279.
- Poor: 42,080.
- National bridge area: 406,604,942 m².
- Colorado count: 8,965.
- Colorado Good/Fair/Poor: 3,197 / 5,336 / 432.
- Colorado area: 5,208,984 m².

The USDOT portal's cached 2024 record count (623,218) exactly matches FHWA's published national all-bridge count. The portal's 2024 count therefore has an independent aggregate benchmark at the national level.

FHWA Colorado condition table values match the values extracted from the 2024 condition-by-highway-system table. The portal's year-level cached metadata does not expose a Colorado count in the landing-page summary; the state count is the FHWA benchmark for a future row-level query.

FHWA page: https://www.fhwa.dot.gov/bridge/nbi/no10/condition24.cfm

### 2025

FHWA's 2025 published all-bridge count is 624,193. The USDOT portal's cached 2025 record count is also 624,193.

The equality is a strong aggregate consistency check. It is not an independent row-level recount and does not prove that all fields in the portal export are preserved without transformation.

## What this establishes

- The portal's cached annual counts align exactly with FHWA's published national all-bridge totals for both 2024 and 2025.
- The dataset is a promising official route for acquiring a reproducible two-year bridge-level baseline.
- The 2024 official Colorado benchmark is 8,965 bridges, with 3,197 Good, 5,336 Fair, and 432 Poor.
- The 2024 table reports bridge area in square metres. Preserve units and do not compare directly with 2026 SNBI area in square feet without explicit conversion and definition controls.

## What this does not establish

- No raw CSV/JSON/XML rows have yet been retrieved in this environment.
- No independent row count, state filter, duplicate test, identifier integrity test, null profile, or field-by-field comparison has been performed.
- Matching cached totals do not prove matching record-level scope or that structure numbers have not been transformed.
- The portal's two-year dataset does not supply the multi-year history needed for identity reconstruction, inspection-event reconstruction, or treatment-effect estimation.
- No model calibration or predictive validation is supported by this audit.

## Acquisition blocker

A bounded read-only attempt to retrieve five Colorado JSON rows and the bulk CSV export through the connected TinyFish fetch service could not execute because the Composio instant wallet had no remaining credits. This is a tool-account execution limitation, not a source-access denial or evidence that the public dataset is unavailable.

Alternative routes remain:
1. Obtain the official CSV/JSON through a browser session with public download access.
2. Use a user-provided official download, preserving the original file and metadata.
3. Continue with FHWA InfoBridge All Years export for the longer historical panel.

## Research classification

- **Source-reported:** portal metadata, cached year counts, FHWA 2024 national/state condition totals, FHWA 2025 national count.
- **Derived:** exact equality of portal cached counts and FHWA published national counts for both years.
- **Unresolved:** raw-record fidelity, exact row-level scope, duplicate behavior, and independent state/year counts.
- **Not established:** production ingestion suitability, longitudinal identity continuity, or predictive model calibration.
