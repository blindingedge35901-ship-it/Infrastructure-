# Bridge Data Dictionary and Ingestion Specification v0.1

**Status:** Technical design specification; not an implemented parser or validated dataset.  
**Prepared:** 2026-11-26  
**Scope:** Public-road bridge inventory and condition data, national and state reporting.  
**Publication:** Internal research only; not approved for publication.

## 1. Purpose and governing rule

This document defines how bridge source records are preserved, interpreted, normalized, linked through time, and made available to the bridge stock-and-flow model.

The governing rule is **preserve first, normalize second, derive third**:

1. Preserve each source file and source record exactly as received.
2. Parse source fields according to the correct source era, layout, and coding guide.
3. Store normalized values without overwriting source values.
4. Store every mapping, transformation, unit conversion, filter, and derived value with a version and provenance.
5. Keep unresolved or ambiguous records visible. Do not silently coerce them into valid values.

The dictionary distinguishes established source concepts, proposed internal fields, and mappings requiring item-by-item verification. It does not claim every field is available in every year or for every bridge.

## 2. Source eras and transition handling

### 2.1 Legacy NBI Coding Guide era

- Historical NBI annual ASCII files cover 1992–2025.
- 2025 is the final year using the legacy Coding Guide ASCII format.
- NBI submissions are annual agency submissions and can be corrected during the year. FHWA identifies June 15 as the final public-highway-bridge data publication point for the annual vintage.
- Preserve the exact downloaded vintage and retrieval date. Do not silently replace an earlier corrected copy.
- Legacy record layouts and field meanings must be selected by year and applicable Coding Guide / errata version. Never interpret every year using one timeless layout.

### 2.2 SNBI transition era: 2026–2027

- The 2026 data submittal and later submissions use the JSON-based NBI Submittal File Schema.
- FHWA's Data Crosswalk defines relationships between legacy Coding Guide items and SNBI items. The Detailed Coding Map defines temporary codes and item-level transition details.
- Transitioned data can contain temporary codes and null values. Retain them as reported; do not treat temporary codes as permanent values or convert nulls to zero.
- The crosswalk identifies clean, partial, and non-clean transitions. A legacy value that does not transition cleanly must not be populated into an SNBI field by an assumed one-to-one mapping.
- Some SNBI fields have no legacy equivalent; some fields may remain unpopulated until verified or newly collected.

### 2.3 Full SNBI era: 2028 onward

FHWA implementation guidance expects the March 2028 submission to be complete and verified using SNBI-based data, with temporary codes replaced by permanent values and fields not populated by transition completed.

Treat 2026 and 2027 as distinct transition vintages, not ordinary legacy years or fully mature SNBI years. Treat 2028 as the planned start of the full SNBI regime while retaining each actual file's schema version and validation status.

### 2.4 Never flatten the eras

Every observation must carry:
- source system: legacy Coding Guide, SNBI transition, or SNBI;
- submission / observation year;
- source file vintage and retrieval date;
- schema or record-layout version;
- Coding Guide, SNBI, errata, crosswalk, and code-map versions where applicable;
- whether the record is original, agency-transitioned, FHWA-transitioned, or otherwise transformed;
- transition status and temporary-code flag.

Do not rewrite historical source records into SNBI form and discard the originals. FHWA says legacy data remains available in original Coding Guide format; both original and transitioned representations are analytically valuable.

## 3. Source register and precedence

| Source | Primary use | Limitation / handling |
|---|---|---|
| FHWA annual NBI download files | Official annual inventory and condition records | Annual agency submissions; revisions possible before final publication |
| FHWA legacy NBI ASCII archives | Historical record-level data, 1992–2025 | Year-specific layout and Coding Guide rules; historical scope filters must be versioned |
| SNBI specifications and errata | Current field definitions, units, precision, valid values, reporting rules | Use the version effective for the actual submission |
| NBI Submittal File Schema | JSON structure and relationships for 2026+ | Schema does not guarantee every item is populated |
| Data Crosswalk | Legacy-to-SNBI relationship | Mapping can be clean, partial, or absent; follow item-specific notes |
| Detailed Code Mapping | Temporary codes and item-specific transition behavior | Transition-only values must remain identifiable |
| NBI Element Data / SNBI Bridge Element data | Element-level condition and quantity where submitted | Element collection is required for NHS bridges and optional for non-NHS bridges |
| FHWA published condition tables | Independent aggregate reproduction and validation | Record table scope, vintage, denominator, and calculation procedure |
| FHWA InfoBridge / structure-number history | Supporting identity reconciliation | Structure number is not a guaranteed permanent physical-asset identifier |
| Project, contract, and agency records | Intervention and construction evidence | Distinguish funding/obligation from completed work on a specific asset |

The applicable official specification controls field meaning. The raw annual record controls what value was actually submitted. Published aggregate tables are validation targets, not substitutes for record-level data. Preserve conflicts and investigate them.

## 4. Four-layer data architecture

### Layer A — immutable source archive

Store original downloaded files or payloads byte-for-byte, with source URL and publisher, retrieval timestamp (UTC), submission year, filename, file size, SHA-256 checksum, archive/member path, format/compression, schema/layout version, applicable specification and errata, source release notes, and download/parse status.

Never modify files in this layer. If a source is reissued, store a second vintage.

### Layer B — raw parsed records

Store each record with original field names/positions and raw string/value representations. For JSON, preserve the original object and array/relationship structure. Do not trim, case-fold, zero-pad, or normalize the raw value in place.

Each parsed record points to its immutable source file and stable source-record locator (record number, JSON path, or equivalent).

### Layer C — normalized observations

Convert source fields to typed internal values only when the applicable definition and mapping are established. Retain source field ID/name, raw source value, normalized value, normalized unit, mapping rule ID/version, validity and missingness classification, transformation timestamp, software version, and quality flags.

A normalized field must be traceable to its raw source value.

### Layer D — derived model data

Derived fields include calculated deck area, age at observation, condition class under a specified rule, identity links, annual stock-flow events, and model features. Each derived field records its formula, inputs, rule version, and uncertainty/confidence where applicable.

Do not mix derived values into the normalized source-observation layer.

## 5. Dictionary conventions

### 5.1 Naming and types

Use stable lower-case snake_case names internally. Preserve official source IDs separately (for example, legacy Item 8 and SNBI B.ID.01).

- Identifiers: strings, never numeric.
- Codes: strings or categorical values; do not assume ordinal meaning unless specified.
- Counts: integers.
- Measurements: decimal numeric plus explicit unit.
- Dates: ISO 8601 date; retain source precision if only year/month is known.
- Booleans: nullable boolean, not forced true/false.
- Geometry: decimal latitude/longitude with source and coordinate-reference metadata.
- Money: decimal amount plus currency, price year, and cost basis.

Identifiers must not be cast to integers. Leading zeroes, spaces, punctuation, and alphanumeric values may be meaningful.

### 5.2 Missingness taxonomy

Do not collapse all missing-like values into SQL NULL or zero. Use a separate missingness / quality status with at least:

- PRESENT — valid source value is present;
- SOURCE_NULL — explicit null in source;
- BLANK — empty field or blank string;
- NOT_REPORTED — source or agency did not report the item;
- NOT_APPLICABLE — item does not apply under the source definition;
- NOT_COLLECTED — item was not collected;
- NOT_TRANSITIONED — no value populated by transition;
- TEMPORARY_CODE — valid only under transition rules;
- INVALID_SOURCE_VALUE — fails applicable source code/range rule;
- UNKNOWN_REASON — missingness exists but reason is not established.

These are internal data-management labels, not replacements for official FHWA codes. Maintain the exact raw missing token/code alongside them. Zero is a value, not a generic missing-data substitute.

## 6. Core bridge data dictionary

This is the initial logical dictionary. It identifies concepts and source families; it does not assert that every item is present in all vintages. Item-level mappings must be completed against the controlling Coding Guide and SNBI crosswalk before production ingestion.

### 6.1 Asset identity and location

| Internal field | Meaning | Legacy NBI source candidate | SNBI source family / candidate | Rules |
|---|---|---|---|---|
| source_record_id | Unique record within a source vintage | File + record locator | File + JSON path / object locator | Internal immutable key |
| source_system | NBI era / representation | Legacy ASCII | SNBI JSON / transition | Required |
| submission_year | Annual data year | File vintage | File vintage | Not necessarily inspection year |
| state_code | State or territory code | Item 1 | B.L.01 State Code | Preserve exact source code and code-list version |
| county_code | County / parish code | Item 3 | B.L.02 County Code | Preserve raw and normalized forms |
| structure_number_raw | Structure identifier as submitted | Item 8 | B.ID.01 Bridge Number | String; never assume immutable |
| previous_bridge_number | Prior identifier associated with current bridge | Structure-number change history | B.ID.03 Previous Bridge Number | Preserve relationship and provenance |
| bridge_name | Reported bridge name | Not consistently available as legacy item | B.ID.02 Bridge Name | Optional; not a key |
| feature_intersected | Feature crossed by bridge | Item 6 | SNBI location / feature fields | Retain source wording/code |
| facility_carried | Route/facility carried by bridge | Item 7 | SNBI route / location fields | Retain source wording/code |
| location_description | Textual location | Item 9 | SNBI location description | Preserve source text |
| latitude / longitude | Geographic coordinates | Items 16 / 17 | SNBI location coordinates | Preserve precision and coordinate reference |
| bypass_detour_length | Reported detour length | Item 19 | SNBI route / detour fields only if crosswalk confirms | Unit and code rules versioned |

Identity resolution belongs in bridge_identity_link, not in direct replacement of raw structure numbers. Keep jurisdiction + year + raw identifier as a record key. physical_asset_id is an internal adjudicated link, not a copied NBI field.

### 6.2 Route, use, and exposure descriptors

| Internal field | Meaning | Legacy NBI source candidate | SNBI source family / candidate | Rules |
|---|---|---|---|---|
| route_designation | Route / network designation | Item 5 and associated route fields | SNBI route and location sections | Detailed mapping pending |
| record_type | Legacy record relation (on / under) | Item 5A | No assumed direct equivalence | Critical for historical filtering; not condition |
| highway_system_class | NHS / other system classification | Applicable legacy route/system items | SNBI route / classification items | Preserve rule version |
| average_daily_traffic | Reported ADT | Item 29 | SNBI traffic data items | Retain value, definition, and year |
| adt_year | Year associated with traffic count | Item 30 | SNBI traffic data items | Do not assume submission year |
| lanes_on_bridge / lanes_under_bridge | Lane counts | Item 28 | SNBI roadway / route items | Confirm exact mapping |
| approach_roadway_width | Approach roadway width | Item 32 | B.G.09 Approach Roadway Width | Preserve unit and precision |
| functional_class | Functional classification | Applicable legacy route item(s) | SNBI route / functional classification | Exact mapping pending |
| rural_urban_context | Geographic context | Derived / external geography | Derived / external | Keep separate from source-reported classification |

### 6.3 Physical geometry and asset characteristics

| Internal field | Meaning | Legacy NBI source candidate | SNBI source family / candidate | Rules |
|---|---|---|---|---|
| year_built | Original construction year | Item 27 | SNBI construction / age fields per crosswalk | Preserve reported year |
| year_reconstructed | Reported reconstruction year | Legacy construction history item; exact mapping to verify | SNBI construction / history fields | Do not implement until verified |
| structure_type | Main structure type | Legacy Items 43–45 family | SNBI structure type / material / design items | Keep material, design, and type distinct |
| material_type | Primary material | Legacy structure type/material fields | SNBI material items | Version code list |
| design_type | Structural design type | Legacy structure type/design fields | SNBI design items | Version code list |
| nbis_bridge_length | Length under NBIS definition | Item 49 | B.G.01 NBIS Bridge Length | Unit and definition version |
| total_bridge_length | Total bridge length | Legacy length fields; exact mapping to verify | B.G.02 Total Bridge Length | Do not substitute NBIS length |
| maximum_span_length | Maximum span length | Legacy span fields where available | B.G.03 Maximum Span Length | Preserve source unit |
| minimum_span_length | Minimum span length | Legacy span fields where available | B.G.04 Minimum Span Length | Preserve source unit |
| width_out_to_out | Bridge width out-to-out | Legacy width fields; exact mapping to verify | B.G.05 Bridge Width Out-to-Out | Preserve source unit |
| width_curb_to_curb | Curb-to-curb width | Legacy width fields; exact mapping to verify | B.G.06 Bridge Width Curb-to-Curb | Preserve source unit |
| irregular_deck_area | Reported irregular deck area | Not assumed available in legacy NBI | B.G.15 Irregular Deck Area | SNBI field; preserve as reported |
| calculated_deck_area | FHWA-calculated deck area | Published/derived legacy area where applicable | B.G.16 Calculated Deck Area | FHWA-calculated, not directly reported |
| deck_area_model | Internally calculated comparable deck area | Derived from approved geometry rules | Derived from SNBI geometry and FHWA procedure | Store formula and rule version |

SNBI geometry fields include B.G.01–B.G.16. FHWA states B.G.16 Calculated Deck Area is calculated by FHWA and is not reported by the submitting agency. Preserve the distinction between reported dimensions, FHWA-calculated deck area, and internal reconstruction.

### 6.4 Condition and structural evaluation

| Internal field | Meaning | Legacy NBI source candidate | SNBI source family / candidate | Rules |
|---|---|---|---|---|
| deck_condition_rating | Deck component rating | Item 58 | B.C.01 Deck Condition Rating | Preserve raw code and regime |
| superstructure_condition_rating | Superstructure rating | Item 59 | B.C.02 Superstructure Condition Rating | Preserve raw code and regime |
| substructure_condition_rating | Substructure rating | Item 60 | B.C.03 Substructure Condition Rating | Preserve raw code and regime |
| culvert_condition_rating | Culvert rating | Item 62 | SNBI culvert condition item per specification | Applicability matters |
| lowest_condition_code | Legacy lowest component code / derived summary | Legacy computed field where present | No assumed direct SNBI equivalent | Rule-versioned |
| overall_condition_class | Good / Fair / Poor / Unknown under specified procedure | Derived under legacy procedure | Derived under applicable SNBI procedure | Never store without rule version |
| structurally_deficient_status | Historical SD classification | Legacy era | Not a synonym for Poor | Keep historical series distinct |
| poor_condition_status | Post-2018 Poor classification | Derived under post-2018 rule | Derived under applicable current procedure | Retain procedure and completeness |
| structural_evaluation | Structural evaluation measure | Item 67 | SNBI structural evaluation / load-rating fields as applicable | Not condition |
| deck_geometry_evaluation | Deck geometry adequacy | Item 68 | SNBI geometry / appraisal fields | Separate from condition |
| underclearance_evaluation | Underclearance adequacy | Item 69 | SNBI clearance fields | Preserve direction / route context |
| waterway_adequacy | Waterway adequacy | Item 71 | SNBI hydraulic / waterway fields | Not condition rating |
| approach_alignment | Approach roadway alignment | Item 72 | SNBI roadway geometry / appraisal fields | Not condition rating |

The exact SNBI IDs and field names for candidates above must be confirmed from the current specification and Data Crosswalk before parser implementation. B.C.01–B.C.03 are used here only for the three named component ratings; do not infer adjacent IDs or guessed mappings.

The 2018 transition from Structurally Deficient to Poor is a classification regime change. The post-2018 Poor rule is based on the lowest applicable rating among deck, superstructure, substructure, and culvert where applicable, using the defined threshold. Reproduce it using the correct year-specific FHWA procedure; it is not a direct rename of the earlier SD category.

### 6.5 Inspection, safety, and operating restrictions

These fields must be collected from the appropriate annual NBI/SNBI items and, where possible, inspection or agency source records. The complete item mapping remains an implementation prerequisite.

Internal concepts:
- last_inspection_date
- inspection_type
- inspection_interval_months
- inspection_method
- inspection_due_date
- load_rating
- operating_rating
- load_posting_status
- load_restriction_value
- scour_evaluation
- scour_vulnerability
- fracture_critical_status
- fatigue_sensitive_details_status
- closure_status
- closure_start_date
- closure_reason

Rules:
- Annual inventory snapshots are not annual inspections.
- Keep actual inspection date separate from submission year.
- Keep inspection interval and method as reported / approved; do not infer them from annual snapshot cadence.
- Load posting, load rating, scour, fracture-critical status, and closure are separate dimensions from condition class.
- Do not interpret a missing value as a safe condition.

### 6.6 Element-level condition data

Maintain element-level data in a separate fact table, linked to bridge observation and physical asset where identity is sufficiently supported.

SNBI Bridge Element data includes element number, parent element number, total element quantity, and quantities in condition states 1, 2, 3, and 4.

FHWA states element-level data collection is required for bridges on the National Highway System and optional for bridges not on the NHS. Missing element data outside the NHS must not be interpreted as zero defects or complete condition.

Element data can add deterioration detail unavailable in coarse NBI component ratings, but it is not a uniform national census across every bridge and year. Preserve its coverage denominator.

## 7. Required internal tables and key fields

### bridge_source_file
source_file_id, source_system, submission_year, source_vintage, retrieved_at_utc, source_url, file_name, sha256, file_size_bytes, format, schema_version, layout_version, specification_version, errata_version, crosswalk_version, code_map_version, download_status, parse_status.

### bridge_record_observation
record_observation_id, source_file_id, source_record_locator, submission_year, reporting_agency_code, structure_number_raw, source_record_type, raw_payload, parse_version, record_scope_status, scope_rule_version, quality_status.

One row per submitted source record per vintage. Do not deduplicate across years in this table.

### bridge_asset
physical_asset_id, first_observed_year, last_observed_year, asset_identity_status, identity_confidence, identity_review_status.

This table represents internal physical-asset identity, not the source record.

### bridge_identity_link
identity_link_id, physical_asset_id, record_observation_id, source_identifier, link_type, match_method, match_confidence, evidence_source, review_status, valid_from, valid_to, adjudication_note.

### bridge_normalized_observation
record_observation_id, field_id, raw_value, normalized_value, normalized_unit, missingness_code, validity_status, mapping_rule_id, mapping_version, transformation_version.

### bridge_condition_observation
record_observation_id, physical_asset_id, condition_regime, component ratings, summary condition class, classification procedure/version, completeness status.

### bridge_inspection_event
physical_asset_id, inspection_date, inspection_type, inspection_method, interval_months, source_record_id, event_source, verification_status.

### bridge_element_observation
record_observation_id, physical_asset_id, element_number, parent_element_number, total_quantity, quantity_cs1, quantity_cs2, quantity_cs3, quantity_cs4, quantity_unit, element_spec_version.

### bridge_inventory_event
physical_asset_id, event_type, event_date_or_year, predecessor_asset_id, successor_asset_id, jurisdiction_from, jurisdiction_to, scope_change_flag, evidence_source, confidence, review_status.

### bridge_intervention_event
physical_asset_id, project_id, intervention_type, component_scope, planned_date, award_date, construction_start_date, completion_date, verified_date, cost_amount, cost_year, funding_stage, source, link_confidence.

### bridge_network_context and bridge_exposure_context
Store route/network consequence, traffic, detour, hazard, climate, flood, scour, corrosion, seismic, and other context with source, vintage, geography, units, and spatial join method. Keep time-varying context out of the static asset table.

## 8. Scope and filter rules

Filtering is a versioned analytical operation, not a destructive cleaning step.

For each source record, retain scope_rule_id and version, inclusion status, exclusion reason, scope population, source record type, and original values used in the decision.

Historical pre-2013 archives require special care. FHWA historical instructions specify a highway-bridge selection rule using multiple fields, including Items 5A, 49, 112, and 42A. **Item 5A = 1 alone is not a valid highway-bridge filter.** Implement the exact rule against the relevant vintage's coding definitions. From 2013, FHWA states only highway bridges are written to the download file, but retain source-vintage notes.

Do not mix all archive records, on records, FHWA highway-bridge scope, published condition-table populations, NHS-only populations, and element-data populations. Each is a distinct population with its own denominator.

## 9. Unit and code normalization

1. Store raw numeric strings and codes exactly as received.
2. Store normalized numeric values only after checking field format and applicable specification.
3. Store a unit code with every dimensional measure. Do not assume legacy and SNBI fields use the same units or precision.
4. Preserve original source units; add converted values as separate derived fields.
5. Version code lists by source era and effective date.
6. Never treat categorical condition codes as continuous physical measurements.
7. Never average component condition ratings unless a documented FHWA or approved model rule requires it.
8. Keep unknown, not applicable, not reported, and temporary transition values distinct.

## 10. Ingestion pipeline and acceptance gates

### Stage 1 — acquire and register
Download official source file and documentation; record retrieval date, URL, source vintage, checksum, and metadata; store unchanged; record revisions and errata.

### Stage 2 — identify source era and layout
Select legacy parser by year and record-layout version, or SNBI parser by schema version. Reject unknown schema/layout rather than guessing. Validate encoding, record length, delimiters, required JSON structure, and file integrity.

### Stage 3 — parse to raw layer
Preserve raw fields and source locator. Record parse errors without dropping source records. Do not normalize or filter during parsing.

### Stage 4 — normalize
Apply versioned field dictionary and code maps. Preserve raw alongside normalized values. Assign missingness and validity statuses. Flag temporary SNBI transition codes. Do not force partial/non-clean crosswalk items into normalized values.

### Stage 5 — scope classification
Apply year-appropriate population filters. Store inclusion/exclusion decision and rule version. Keep alternative populations available for audit.

### Stage 6 — identity resolution
Match records across years using structure-number history, location, geometry, route, feature, and other evidence. Retain candidate matches, method, confidence, and adjudication. Do not equate identifier change with construction or replacement. Do not infer physical removal solely because a record disappears.

### Stage 7 — derive model observations
Compute condition classes using correct year-specific procedure. Calculate age only where construction year is valid. Calculate deck area only with explicit versioned rule. Create stock-flow events only where evidence supports an event type. Retain unresolved residuals.

### Stage 8 — validate and update internal model
Reproduce published FHWA counts and condition totals for matching scope and vintage. Reconcile bridge count and deck-area totals separately. Check duplicates, invalid codes, missingness shifts, coverage, and year-over-year discontinuities. Generate a data-quality report before updating model tables. Keep research outputs internal until user approval.

## 11. Minimum automated quality checks

For each file/vintage:
- checksum and file size recorded;
- parser version and source layout/schema identified;
- record count and parse failure count reported;
- duplicate source-record locator test;
- valid field length, type, and code-range checks by vintage;
- missingness distribution by field and jurisdiction;
- temporary-code counts for 2026–27;
- unknown/unmapped field and code counts;
- valid state/county code checks against dated code lists;
- coordinate bounds and missing coordinate checks;
- year-built and reconstruction-year plausibility checks (flag only; do not silently correct);
- length/width/area nonnegative and unit consistency checks;
- condition component completeness and valid-code checks;
- duplicate/conflicting identity candidate report;
- scope inclusion counts by record type and rule;
- comparison with matching FHWA published aggregates;
- year-over-year count, area, and composition discontinuity report.

A failed check produces a visible flag and review record. It must not silently delete or repair an observation.

## 12. Validation targets and known cautions

First reproduce official annual FHWA aggregate totals under the same source vintage, population scope, geographic coverage, condition procedure, count or deck-area measure, and treatment of missing component ratings.

Previously audited bridge baselines and discontinuities remain documented in separate bridge research files. In particular:
- 2011–2013 historical archive scope must not use Item 5A=1 alone;
- the 2018 SD / Poor classification change must be versioned;
- state/year totals can differ slightly across FHWA and BTS publications;
- Minnesota's 2008–2009 aggregate discontinuity remains unresolved;
- raw structure numbers are not guaranteed stable physical-asset IDs;
- NBI annual records do not provide a complete project-level intervention ledger;
- NHS element-data coverage is not uniform across all bridges.

Do not force aggregate differences into new construction, removals, or deterioration. Retain a reconciliation residual until supported by evidence.

## 13. Implementation blockers before production parser

1. Obtain and archive the exact legacy Coding Guide, applicable errata, and year-specific record layouts.
2. Build a machine-readable field-position map for each legacy layout era.
3. Download the current SNBI specification with current errata and archive the exact version.
4. Download and parse the official Data Crosswalk and Detailed Code Mapping spreadsheets.
5. Confirm every legacy-to-SNBI mapping, including clean / partial / no transition status and unit conversions.
6. Confirm 2026 and 2027 temporary codes and schema handling.
7. Confirm condition-classification procedures by effective year.
8. Confirm inspection, load rating/posting, scour, and safety-related SNBI item IDs and valid values.
9. Confirm annual data packaging, file formats, and retrieval method for each vintage.
10. Test raw records from several years and jurisdictions against FHWA published aggregates before scaling.

This specification intentionally does not invent missing SNBI item IDs or legacy item positions. Candidate mappings remain provisional until verified.

## 14. Official references

All links below are official FHWA sources unless stated otherwise. Reviewed 2026-11-26.

1. FHWA, [Download NBI Data Files](https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm) — annual data, publication timing, transition notes, and historical archive links.
2. FHWA, [Download NBI ASCII Files](https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm) — legacy Coding Guide archive and transition notice.
3. FHWA, [SNBI Specifications](https://www.fhwa.dot.gov/bridge/snbi/snbi_march_2022_publication.pdf) — data item definitions, units, precision, and structure.
4. FHWA, [NBI Submittal File Schema](https://www.fhwa.dot.gov/bridge/snbi/schema.cfm) — JSON submission schema and transition-year notes.
5. FHWA, [Data Crosswalk for Over and Under Records](https://www.fhwa.dot.gov/bridge/snbi/datacrosswalk.cfm) — legacy Coding Guide to SNBI mapping.
6. FHWA, [Detailed Code Mapping for Individual Data Items](https://www.fhwa.dot.gov/bridge/snbi/codemapping.cfm) — item-level mapping and temporary transition codes.
7. FHWA, [SNBI Data Validation Logic](https://www.fhwa.dot.gov/bridge/snbi/data_validation_logic.cfm) — validation rules and temporary-code guidance.
8. FHWA, [NBI Library](https://www.fhwa.dot.gov/bridge/nbi/library.cfm) — specifications, errata, policy, and guidance.
9. FHWA, [Download NBI Element Data](https://www.fhwa.dot.gov/bridge/nbi/element.cfm) — element-data coverage and annual data.
10. FHWA, [InfoBridge Update Notes](https://infobridge.fhwa.dot.gov/Page/infobridge_update_notes) — historical structure-number and latest-year identifier context.

## 15. Change control

This document is v0.1 and must be revised as mappings are verified. Every mapping change identifies official source/version, affected years, fields, and expected impact. Never revise raw records to accommodate a changed mapping. Any change affecting scope, condition classification, asset identity, or historical trends requires an impact assessment and regression test.

This is an internal technical working document and is not approved for public release.
