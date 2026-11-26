# 2026 SNBI Validation Rules Audit — 2026-11-26

## Primary source
FHWA, SNBI Data Validation Logic, Version 1.2, updated September 16, 2026:
https://www.fhwa.dot.gov/bridge/snbi/data_validation_logic.cfm

FHWA states that version 1.2 is the release validation module used in preparation for the first SNBI NBI submittal on March 15, 2026. FHWA describes critical errors, general errors, and flags; critical errors require correction and resubmission within 15 business days. Minor/isolated general errors may be corrected no later than the next year's submittal; widespread errors may require further analysis. Flags are reviewed to determine whether they are true errors.

## Transition-year policy
For 2026 and 2027, datasets may contain:
- Temporary codes for specified data items.
- Null values for items not collected under the Coding Guide.

FHWA says temporary codes will not be accepted for the 2028 submittal or later. This is a field-specific exception regime, not a general acceptance of arbitrary values with a "-T" suffix.

## Confirmed field-specific temporary-code examples
The current validation page explicitly identifies these examples:

| SNBI item | Data tag | Temporary codes explicitly accepted in 2026–27 | Rule context |
|---|---|---|---|
| B.SP.04 Span Material | BSP04 | X-T, CR-T, S-T, CP-T, T-T, M-T, AI-T | Span material |
| B.SP.05 Span Continuity | BSP05 | C-T, 7-T | Span continuity |
| B.RH.01 Bridge Railings | BRH01 | I0-T, Y-T | Railings |
| B.RH.02 Transitions | BRH02 | I0-T, Y-T | Transitions |
| B.RT.03 Route Direction | BRT03 | 1-T, 2-T | Route direction |
| B.H.01 Functional Classification | BH01 | C-T | Functional classification |
| B.H.02 Urban Code | BH02 | T-U | Urban code |
| B.H.04 National Highway Freight Network | BH04 | 1-T | Freight network |
| B.AP.02 Overtopping Likelihood | BAP02 | VLM-T, HVH-T | Overtopping likelihood |
| B.AP.03 Scour Vulnerability | BAP03 | AB-T, BCE-T, CD-T | Scour vulnerability |

This table is a selected subset of the current validation page, not a complete code inventory. In particular, the code examples observed in DC records must be traced to their exact field and applicable detailed coding-map entry before being assigned meanings.

## Identity validation rules
FHWA validation logic specifies:
- B.ID.01 / BID01 Bridge Number is critical: required, checked for duplicates, maximum 15 characters, and restricted to specified characters.
- B.ID.02 / BID02 Bridge Name is optional; missing name generates a flag, not a critical error.
- B.ID.03 / BID03 Previous Bridge Number must have a value or 0 when no previous bridge number exists; null generates a flag. Maximum 15 characters and character restrictions apply. BID03 should not equal BID01.

Implementation implications:
- Preserve bridge numbers as strings; do not cast to integers or discard leading zeros.
- Preserve raw BID03 value, and normalize 0 into a semantic no-previous-bridge state only in a derived field.
- Implement validation against the exact item-specific permitted character set and length.
- Distinguish a critical error, general error, and flag; do not collapse all validation findings into a single boolean.

## Conditional validation and relationships
Validation logic is not just per-field domain checking. It contains conditional rules tied to relationships and other items. Examples:
- B.RT.01–B.RT.05 route fields are required under specified highway-feature conditions.
- B.H.01–B.H.06 highway feature attributes are required under specified feature-type/location conditions.
- B.H.18 crossing bridge number must match B.ID.01 within the dataset.
- B.AP.02–B.AP.04 scour/overtopping fields are conditionally reported based on feature type.
- B.E.03 element total quantity must equal the sum of condition-state quantities (B.CS.01–B.CS.04) for the corresponding element.

Implementation implications:
- Validation must operate across parent-child records and sometimes across bridge records, not only on individual JSON scalar values.
- Retain nested feature, route, span, element, and other child records in relational form.
- Implement checks in distinct layers: parsing/type checks, item-level domain checks, conditional checks, cross-record referential checks, and quantitative reconciliation checks.

## 2026 national inventory context
FHWA's 2026 data page reports 624,939 highway bridges nationally. It reports 261 for the District of Columbia and 9,018 for Colorado. The 2025 page reports 261 for DC and 8,990 for Colorado. These are published inventory counts, not independently parsed results.

The unchanged DC count between 2025 and 2026 does not establish that the same 261 physical bridges are present in both years. It only establishes equal published aggregate counts. Identity matching and additions/removals must be determined from bridge-level records and history.

Sources:
- 2026: https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm
- 2025: https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2025.cfm

## Model and ingestion safeguards
1. Never strip "-T" suffixes or map temporary codes to permanent codes without a field-specific FHWA rule.
2. Store raw code, field ID, inventory vintage, and validation-rule version together.
3. Mark temporary-code observations as transition-period values; do not interpret as stable longitudinal categories without a documented crosswalk.
4. Preserve null, absent key, empty array, and explicit no/zero code as distinct states.
5. Keep source data and validation findings immutable; corrections belong in derived normalized views with provenance.
6. Do not interpret FHWA validation acceptance as evidence that a value is physically correct; validation is a data-quality rule, not independent field verification.

## Evidence status
- **Source-reported:** Validation version/date; error categories; field-specific temporary-code examples; identity and conditional rules; published state counts.
- **Directly observed in 2026 DC JSON excerpts:** Several temporary-code values and nested data structures.
- **Not established:** Full-file code frequency, full set of temporary codes present in the national 2026 data, actual error/flag outcomes for each DC record, or completeness of every rule in this selected audit.
- **Next step:** Retrieve current schema and Errata No. 2 artifacts and parse a complete state file to build exhaustive code/key/type/cardinality inventories.

Internal research record only; not approved for publication.
