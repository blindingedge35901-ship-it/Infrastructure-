# 2026–2027 SNBI Transition Provenance and Verification Audit

**Status:** FHWA transition policy verified; record-level provenance encoding remains unverified.  
**Research date:** 2026-11-26  
**Scope:** How to interpret the 2026 and 2027 NBI datasets during the Coding Guide-to-SNBI transition.

## Executive finding

FHWA explicitly states that the 2026 and 2027 datasets contain a combination of:
1. data transitioned from the legacy Coding Guide into SNBI format;
2. data collected under SNBI; and
3. transitioned data that has been verified by inspection or review.

FHWA defines legacy data as data previously reported using the Coding Guide and says it remains available in its original form. FHWA will accept transitioned data only for the 2026 and 2027 submissions; transitioned data will not be accepted for the March 15, 2028 submission.

**Implication:** A dataset-year label is not a sufficient measure of the age, collection method, or verification status of an individual value. The 2026 condition baseline must not be treated as a fully homogeneous, newly collected SNBI observation set.

## What is source-confirmed

The FHWA SNBI Q&A, Topic T: Data Transition, Q/T-3, says the 2026 and 2027 datasets contain a combination of transitioned SNBI data and collected or verified SNBI data. It defines verified data as transitioned data validated by inspection or review. The same Q&A says transitioned data will not be accepted for the March 15, 2028 submittal.

FHWA's current NBI download page independently warns that 2026 and 2027 transition data may contain temporary codes and null values, and directs users to the Data Crosswalk and Detailed Coding Map for the relationships and temporary-code information.

## What has not yet been established

The reviewed public materials do not yet establish a complete, machine-readable field-level method to distinguish, for every bridge and item:
- directly collected SNBI value;
- transitioned legacy value;
- transitioned value subsequently verified by inspection;
- transitioned value verified by other review;
- value absent because it was not collected under the legacy Coding Guide;
- value absent for another reason.

Do not assume a particular tag, flag, date, or temporary code represents provenance unless the authoritative schema, crosswalk, validation rules, or data documentation explicitly defines it that way.

The 2026 DC JSON excerpt confirms that actual public records contain SNBI-tagged values, nested collections, date-like strings, temporary codes, and optional fields. It does not, by itself, establish a universal field-level provenance flag. The excerpt is not a complete local file parse.

## Required model treatment

### 1. Keep submission vintage separate from observation vintage

At minimum, preserve:
- `submission_year`
- `source_publication_date`
- `inspection_event_date` where the source explicitly identifies it
- `field_value`
- `field_source_era` only when supported by source metadata
- `field_verification_status` only when explicitly supported
- `provenance_evidence_source`
- `provenance_confidence`

Do not infer inspection date from submission year. Do not infer that a value was inspected or verified simply because it appears in the 2026 SNBI dataset.

### 2. Preserve the original legacy series

Keep original Coding Guide source files and parsed observations immutable and separately addressable. The transitioned SNBI representation should be stored as a distinct observation layer, not used to overwrite original historical values.

### 3. Keep missingness and transition status separate

A null or missing value may reflect an item not collected under the old Coding Guide, a value not transitioned, a source omission, a not-applicable condition, or another reason. Preserve raw values and source-specific missingness codes. Do not convert all missing values to a single null category.

### 4. Do not assume 2026 is a clean break or a clean continuation

For longitudinal analysis:
- retain the 2025 Coding Guide observation series;
- retain the 2026 SNBI observation series;
- link fields through the documented crosswalk;
- mark transition-derived mappings and temporary codes;
- compare only where item meaning, units, scope, and provenance are sufficiently aligned;
- quantify unmatched, missing, temporary-coded, and unverified observations.

If field-level provenance cannot be recovered, mark it unknown rather than assigning the whole record or dataset a false uniform status.

## Data acquisition and schema status

FHWA's SNBI schema page identifies the public submittal schema as updated July 18, 2024, and the example submittal data file as updated February 26, 2025. The page says the schema accommodates Errata No. 1 and temporary codes for the 2026–2027 submissions, and that a new schema is expected before the 2028 submission.

The schema page's indexed content is readable, but the page itself currently returns an FHWA internal-error page to the browser retrieval tool. The actual linked schema and example JSON bytes have not yet been acquired and parsed in this research environment. The DC26.json endpoint is readable through the web document viewer as a 226-line excerpt, but direct file download failed. Therefore:
- schema version and published update dates are source-confirmed;
- selected schema changes are source-confirmed from the FHWA page;
- full schema structure, complete property definitions, and formal validation against the schema remain outstanding;
- no production parser should be claimed or deployed yet.

## Next verification steps

1. Acquire the actual schema JSON and example submission file bytes, recording URL, retrieval timestamp, byte count, and SHA-256.
2. Parse the schema and enumerate root properties, nested object definitions, array item definitions, types, required fields, allowed values, and field length constraints.
3. Locate and inspect the complete FHWA Data Crosswalk and Detailed Coding Map, including any transition/provenance annotations.
4. Determine whether 2026 public download records expose field-level transition or verification metadata, and document the exact tags and semantics if present.
5. Test representative records against the schema and validation rules; separately test source-level missingness and temporary codes.
6. Only then implement versioned parser and normalization rules.

## Sources

1. FHWA, *SNBI Questions and Answers*, Topic T: Data Transition, especially QT-3 and AT-3: https://www.fhwa.dot.gov/bridge/snbi/qanda/04.cfm
2. FHWA, *Download NBI Data Files*, transition and missing-value notice: https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm
3. FHWA, *NBI Submittal File Schema*, schema/example update dates and 2026–2027 temporary-code accommodation: https://www.fhwa.dot.gov/bridge/snbi/schema.cfm
4. FHWA, *Download NBI Data Files 2026*, published state and national counts and JSON availability: https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm
5. FHWA, District of Columbia 2026 JSON endpoint (viewer excerpt inspected; not a full-file local parse): https://www.fhwa.dot.gov/bridge/nbi/2026/JSON/DC26.json

## Evidence classification

- **Source-reported:** 2026–2027 contain a mixture of transitioned, collected, and verified SNBI data; transitioned data ceases with the 2028 submission.
- **Source-reported:** FHWA retains legacy Coding Guide data in its original form.
- **Derived:** Submission year alone cannot establish the observation vintage or verification status of every value.
- **Unknown/unresolved:** Complete field-level provenance indicators and their semantics in the publicly downloadable 2026 records.
- **Model recommendation:** Preserve original and transitioned layers separately; unknown provenance stays unknown.
