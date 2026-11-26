# SNBI Detailed Coding Map: Semantic Loss and Temporary-Code Audit

**Status:** Selected detailed mapping tables reviewed from FHWA's published page. This is a targeted semantic audit, not a complete transcription of the downloadable workbook.  
**Research date:** 2026-11-26  
**Source:** FHWA, Detailed Code Mapping for Individual Data Items: https://www.fhwa.dot.gov/bridge/snbi/codemapping.cfm

## Executive finding

The Detailed Coding Map contains transformations that are not simple code substitutions. Several legacy fields:
- collapse multiple legacy meanings into a temporary code;
- split one legacy field into multiple SNBI items;
- assign values to a specific feature or route based on assumptions;
- use another legacy item to disambiguate a value;
- create calculated values;
- leave fields blank where the legacy source cannot support an SNBI value.

These transformations create different levels of historical comparability. The model must retain source values and transformation logic, not just the resulting SNBI code.

## 1. Scour: one legacy rating becomes multiple concepts

Legacy Coding Guide Item 113 (Scour Critical Bridges) maps to both:
- B.C.11 Scour Condition Rating; and
- B.AP.03 Scour Vulnerability.

Examples from FHWA's detailed map:
- Legacy 113 = N: B.C.11 = N; B.AP.03 blank because bridge does not cross over a waterway.
- Legacy 113 = U: B.C.11 blank; B.AP.03 = U (scour appraisal not completed due to unknown foundations).
- Legacy 113 = T: B.C.11 blank; B.AP.03 = 0 (scour appraisal not completed).
- Legacy 113 = 9: B.C.11 = 9 (no scour); B.AP.03 = A (appraisal completed; stable for scour).
- Legacy 113 values 8, 7, 5, and 3 can produce temporary B.C.11 value MI-T, while B.AP.03 maps to AB-T, BCE-T, or CD-T depending on the legacy value.
- Legacy 113 = 4 can map B.C.11 to MO-T and B.AP.03 to AB-T.
- Legacy 113 = 2 can map B.C.11 to MA-T and B.AP.03 to CD-T.
- Legacy 113 = 1 or 0 maps B.C.11 to 1 or 0 and B.AP.03 to CD-T.

**Model implication:** Do not treat the resulting B.C.11 and B.AP.03 as two independent historical observations. Both are transformations of one legacy source item. Preserve the common source lineage and a transformation flag. Avoid double-counting the same legacy signal in a composite scour-risk measure.

The mapping also shows that a legacy code can produce a temporary code for one SNBI item and a permanent code for the other. Temporary/permanent status must be stored per output item, not per source record.

## 2. Load posting: legacy categories are broader than permanent SNBI states

Legacy Item 41 maps to B.PS.01 Load Posting Status. Selected mappings:
- A → PO (permanent bridge in place, open without restrictions)
- B → PA-T (temporary code combining several permanent/temporary posting states and reasons)
- D → SO (permanent bridge with temporary shoring, open without restrictions)
- E → TO (temporary bridge in place, open without restrictions)
- G → N (new bridge not yet open)
- K → C (closed to all traffic)
- P → PP-T (temporary code combining several posted-load states)
- R → PR-T (temporary code combining several non-load restriction states)
- null → no value

**Model implication:** PA-T, PP-T, and PR-T are not final, fully resolved posting categories. Do not translate them into a single specific permanent state. Retain the original Item 41 code, temporary SNBI value, and unresolved alternatives.

## 3. Span continuity and deck material: subtype information is lost

FHWA's detailed map shows legacy Item 43B/44B values can map to temporary codes when the old classification cannot identify a unique permanent SNBI subtype.

Examples:
- Span continuity values can map to S-T, GB-T, GT-T, BM-T, BS-T, F-T, T-T, AD-T, AT-T, L-T, C-T, Z-T, or GC-T.
- These temporary values represent groups of possible permanent span types.
- Deck Material and Type (B.SP.09) can map to CR-T, CP-T, S-T, T-T, or X-T where the legacy fields do not support a unique permanent subtype.
- Additional legacy fields may be used to disambiguate some cases; for example, Item 43B/44B value 08 changes the mapping of one steel deck value to S04.

**Model implication:** Preserve the candidate set represented by a temporary code. Do not arbitrarily select one permanent material or span type. Where multiple legacy fields jointly determine the mapping, retain all inputs and the rule version.

## 4. Traffic direction: directionality is not preserved by legacy data

Legacy Item 102 maps:
- 1 → 1-T (one-way traffic; could be NB, EB, SB, or WB)
- 2 or 3 → 2-T (two-way traffic; could be NS or EW)
- other values → no value

**Model implication:** The legacy field supports one-way versus two-way classification, but does not necessarily support compass direction. A parser must not convert 1-T to northbound or 2-T to north-south. Direction-specific analysis needs a new observed SNBI value or independent authoritative evidence.

## 5. Functional classification and urban code: cross-field assumptions

The detailed map uses legacy Item 26 to populate both:
- B.H.01 Functional Classification; and
- B.H.02 Urban Code.

Examples:
- Legacy values 01, 02, 06, 07, 08, or 09 map B.H.02 to 99999 (rural).
- Legacy urban-coded values map B.H.02 to temporary T-U.
- Some functional classification values map directly; legacy collector values 17 map to temporary C-T because the old code does not resolve the new distinction between major and minor collector.
- Validation rules accept T-U and C-T only for the 2026 and 2027 transition years.

**Model implication:** Functional classification and urban code must remain separate attributes. Do not infer a permanent urban code from T-U. Retain the original Item 26 value and transition rule.

## 6. Overtopping likelihood: cross-field transformation

B.AP.02 Overtopping Likelihood is derived from legacy Item 71 (Waterway Adequacy) and, in selected cases, Item 26 (Functional Classification).

Examples:
- Item 71 = N: no value because the bridge does not cross a waterway.
- Item 71 = 9 or 8: code 1 (remote).
- Item 71 = 7: temporary VLM-T (very low to moderate).
- Item 71 = 6: code 1 for selected local functional classes, otherwise VLM-T.
- Item 71 = 4: code 5 (high) for selected local functional classes, otherwise code 1.
- Item 71 = 3: code 6 (very high) for selected local functional classes; code 1 for selected Interstate classes; otherwise code 5.
- Item 71 = 2 or 0: temporary HVH-T (high to very high).

**Model implication:** This is a derived estimate from legacy waterway adequacy and route classification, not a direct historical measurement of overtopping frequency. Retain both input fields and mark the value as transition-derived. Do not interpret the assigned frequency band as observed flood occurrence.

## 7. Scour plan of action: a temporary inferred requirement

Legacy Item 113 maps to B.AP.04 Scour Plan of Action:
- legacy values 4, 5, 8, or 9 → 0 (POA not required);
- other values → Y-T (temporary: POA required and implemented);
- N → no value.

**Model implication:** Y-T is a temporary transition result. Do not treat it as a permanent verified POA record without subsequent confirmation. Keep the distinction between requirement and implementation explicit; the temporary description includes both.

## 8. Border bridge inspection responsibility: funding is used as a proxy

The primary Data Crosswalk notes that legacy Item 98B represents funding responsibility, while the transition assumes funding and inspection responsibility are the same:
- 99 → 0 (no responsibility)
- 00 → 2 (full responsibility)
- other values → 1 (shared responsibility)

**Model implication:** This is a semantic proxy assumption, not a direct historical observation of inspection responsibility. Do not use it to attribute inspection workload or agency performance without qualification and verification.

## 9. Other transformations requiring explicit formulas or provenance

The primary crosswalk includes additional nontrivial transformations:
- Latitude/longitude: convert legacy degrees/minutes/seconds to decimal degrees, with sign determined by geography/state code.
- LRS Mile Point: convert legacy kilometerpoint to miles and round to the nearest thousandth.
- Clearance and horizontal-width fields: convert metric values to feet with field-specific rounding and sentinel values for large clearances.
- Bypass Detour Length: convert metric to miles; legacy 199 maps to 999.
- Annual Average Daily Truck Traffic: multiply legacy truck percentage by Average Daily Traffic.
- Route Number: concatenate route number and directional suffix, with leading-zero and zero-only handling.
- Bridge Number: trim spaces; leading-zero treatment requires an explicit selection and no default.
- Calculated deck area: calculated from source geometry under the applicable transition-era formula.

**Model implication:** These transformations need versioned, unit-aware code and test cases. Do not implement a generic “convert metric to imperial” helper without the exact field-specific rounding and sentinel behavior.

## 10. Parser and analytical requirements

For every transformed item, store:
- source legacy item ID(s);
- source raw value(s);
- target SNBI item/tag;
- mapped value;
- transition class;
- temporary/permanent status;
- rule identifier and version;
- any cross-field dependencies;
- any assumptions;
- whether the target is calculated, inferred, or directly mapped;
- source record and source vintage.

For temporary values, store the set of possible permanent values when the crosswalk defines one. Do not resolve ambiguity without later record-level evidence.

For any composite risk score, avoid double-counting derived items that share the same legacy source signal. In particular, the dual scour mapping must be modeled with source lineage and a dependency relationship.

## 11. What this audit does not establish

- It does not transcribe every table in codemapping.xlsx.
- It does not establish the actual verification status of individual 2026 bridge records.
- It does not establish that temporary codes in a public record were subsequently corrected.
- It does not provide coefficients linking scour, load posting, overtopping, or material types to failure probabilities.
- It does not justify replacing observed SNBI data with transition-derived legacy values.
- It does not establish that all jurisdictions used identical transition practices beyond FHWA's published rules.

## Sources

1. FHWA, Detailed Code Mapping for Individual Data Items: https://www.fhwa.dot.gov/bridge/snbi/codemapping.cfm
2. FHWA, Data Crosswalk for "Over" Records and "Under" Records: https://www.fhwa.dot.gov/bridge/snbi/datacrosswalk.cfm
3. FHWA, SNBI Data Validation Logic, including transition-year temporary-code acceptance and conditional checks: https://www.fhwa.dot.gov/bridge/snbi/data_validation_logic.cfm
4. FHWA, NBI Submittal File Schema and transition schema notes: https://www.fhwa.dot.gov/bridge/snbi/schema.cfm

## Evidence classification

- **Source-reported:** Selected mapping tables and transformation notes described above.
- **Derived:** These transformations may create semantic loss, cross-field dependency, and shared-source double counting if treated as direct observations.
- **Model recommendation:** Preserve source lineage, ambiguity, transformation version, and evidence status.
- **Outstanding:** Complete workbook acquisition and systematic transcription/test coverage for every item.
