# 2026 SNBI JSON Record Inspection — District of Columbia

**Inspection date:** 2026-11-26  
**Source:** FHWA 2026 NBI public JSON, District of Columbia  
**URL:** https://www.fhwa.dot.gov/bridge/nbi/2026/JSON/DC26.json  
**Official 2026 inventory page:** https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm

## Scope and evidence boundary

The FHWA-hosted JSON file was opened through the web source viewer and representative records were inspected directly. The viewer exposed 226 lines of JSON content, including complete-looking bridge objects and nested collections. This is direct inspection of source excerpts, not a local download, full-file parse, schema validation, or independent recount of all records.

FHWA's 2026 download page reports 261 District of Columbia highway bridges. A third-party catalog also reports an independently executed 261-record load, but that catalog is not used as the primary evidence for this audit. The count should be reproduced from the full FHWA file once acquired locally.

## Directly observed record structure

The file is a top-level JSON array of bridge objects. Observed top-level scalar keys include:

- Identity/location: `BL01`, `BID01`, `BID02`, `BID03`, `BL02`–`BL12`
- Classification: `BCL01`–`BCL06`, `BRH01`, `BRH02`
- Geometry: `BG01`–`BG11`, `BG16`
- Load rating: `BLR01`, `BLR03`–`BLR08`
- Inspection/bridge indicators: `BIR01`, `BIR03`
- Condition: `BC01`–`BC04`, and observed examples of `BC06`, `BC09`, `BC11`–`BC15`
- Approach/scour: `BAP01`–`BAP04`
- Year built: `BW01`

Observed nested arrays include:

- `Features`, with feature records and nested `Routes`
- `SpanSets`
- `SubstructureSets`
- `PostingEvaluations`
- `PostingStatuses`
- `Inspections`
- `Elements`
- `Works`

These are actual observed names, not inferred names. Full item definitions and units must still come from the SNBI and crosswalk.

## Important implementation observations

1. **Nested arrays must be retained.** A bridge may have multiple feature records; a feature may have multiple routes; bridge records may have multiple inspections, element observations, span sets, posting statuses, and work records. A single flattened bridge table would lose repeatable child records or multiply rows in ways that distort bridge counts.
2. **Optional fields are genuinely absent in individual objects.** For example, inspected bridge objects do not all expose the same full set of geometry, load-rating, condition, approach/scour, and feature attributes. The parser must distinguish an absent key from an explicit JSON null and from a present value.
3. **Values are not uniformly numeric.** Observed fields contain numbers, numeric-looking strings, alphanumeric codes, date strings, and special/temporary code values.
4. **Transition codes appear in live 2026 records.** Examples observed include `Y-T`, `MI-T`, `AB-T`, `S-T`, `C-T`, `CR-T`, `T-U`, `2-T`, `1-T`, `I0-T`, and `VLM-T`. These are examples only, not a complete code inventory. Their meanings must be taken from the applicable Detailed Coding Map and current validation logic; do not strip suffixes or normalize them without an item-specific rule.
5. **Identifier formatting matters.** `BID01` appears as a string with leading zeros (e.g. `"0001"`), so it must not be coerced to an integer. Raw values and exact strings must be preserved.
6. **Date-like values are strings.** Observed values include `20260101`, `20260209`, and `20260326`. Store raw tokens and parse to typed dates only under field-specific definitions.
7. **An empty nested array is present.** Example `"SubstructureSets":[]`. Preserve empty array as distinct from missing key and null.

## Initial data architecture implications

Keep one bridge-observation row per bridge per source vintage, keyed by source file and raw bridge identifier, and separate child tables for each repeated relationship:

- `bridge_feature_observation`
- `bridge_route_observation`
- `bridge_span_set_observation`
- `bridge_substructure_set_observation`
- `bridge_posting_evaluation_observation`
- `bridge_posting_status_observation`
- `bridge_inspection_observation`
- `bridge_element_observation`
- `bridge_work_observation`

Every child row should retain source vintage, source-file ID, parent raw identifier, array ordinal, raw JSON payload, and parsed fields. Do not assume array order is a stable identity key across years; ordinal is provenance only.

Do not flatten repeated child arrays into one denormalized bridge record for model calculations until aggregation rules have been defined and tested. In particular, element quantities and condition states are not interchangeable with bridge-level condition ratings.

## Outstanding verification

- Acquire the full DC JSON file as bytes and record file size and SHA-256.
- Parse all 261 records and verify count against FHWA's published DC count.
- Compare actual keys/types/required fields with the current FHWA JSON schema and SNBI Errata No. 1 and No. 2.
- Build a complete inventory of observed keys, value types, missingness, temporary codes, and array cardinalities.
- Reconcile bridge-level calculated condition fields with the official 2026 computation procedure.
- Test whether every bridge has `BID01`, how `BID03` no-predecessor value is represented, and whether raw IDs are unique within state/vintage.
- Inspect a larger state file and compare its structure; DC alone is not a sufficient national sample.

## Evidence status

- **Directly observed:** top-level JSON array; bridge-object keys and nested array names listed above; representative code and value patterns; optional-key variation; leading-zero string IDs; date strings; empty array example.
- **Source-reported:** 261 District of Columbia bridges on FHWA's 2026 download page.
- **Not established:** full-file count, complete schema conformance, nationwide key coverage, code definitions, longitudinal identifier stability, or parser correctness.

Internal research record only; not approved for publication.
