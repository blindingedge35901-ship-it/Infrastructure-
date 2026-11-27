# InfoBridge longitudinal data access and component-rating validation audit

**Status:** Research audit; no production data downloaded or parsed.  
**Scope:** FHWA LTBP InfoBridge public portal, longitudinal NBI export behavior, historical condition timing caveats, and selected SNBI component/element validation rules.  
**Purpose:** Define a defensible route to obtain bridge-level longitudinal observations and prevent invalid condition-transition training data.

## 1. Executive findings

1. InfoBridge publicly documents a way to select bridge records and export NBI attributes for the latest year, all years, or a specified year range. Its page describes exports as bridge records based on selected attributes and year selection.
2. InfoBridge explicitly warns that historical NBI exports may contain earlier structure numbers for years in which a bridge's number changed. It adds a separate latest-year structure-number column to help associate rows with the same current structure. This is a useful crosswalk aid, not proof that every historical row has been correctly resolved to a physical asset.
3. InfoBridge supports selection across all NBI submittals since 1993, and warns that some bridges have multiple NBI submittals in one year. A model must preserve submittal/vintage identity and not assume one record per bridge-year.
4. Historical condition graphs are described as plotting condition ratings as reported in each NBI submittal. InfoBridge warns that the inspection dates for those ratings may lag by a few years for some bridges. Therefore, annual NBI vintage is an observation/submittal time, not a reliable substitute for inspection time.
5. The public portal documents graph export as CSV and selected-record export, but the current web inspection did not execute an export, retrieve a specific bridge's complete history, or establish an API endpoint. The data acquisition path is documented, but actual extract reproducibility remains untested.
6. SNBI validation makes component ratings conditional on bridge configuration and component presence. A literal numeric zero, a valid rating of 0, and the not-applicable code N must not be conflated.
7. Element-condition records have their own structural validation. For every element, the total quantity must equal the sum of quantities in condition states 1–4; values must be numeric whole numbers under the published validation rules. These are element-level quantities, not interchangeable with bridge-level component ratings.

## 2. InfoBridge longitudinal extraction capability

The public InfoBridge Data page documents the following workflow and behavior:

- The default selection can use a recent NBI submittal; the All Data option filters through records submitted on or after 1993.
- The Selected Bridges table displays one record for every bridge selected by the filters.
- Users can choose attributes and export selected bridge records.
- Export time selection includes Latest Year, All Years, and Year Range.
- The portal notes that NBI Item 8 (Structure Number) may contain previous structure numbers in some years after a number change. A separate Latest Year NBI Structure Number column is added to help identify rows belonging to the same unique structure.
- Special Projects data is documented as available only for the latest year.
- The page warns that a bridge may have multiple NBI submittals in one year.
- The Historical Condition Rating Graph offers Save as CSV.
- InfoBridge describes historical condition ratings as those reported under each NBI submittal and warns that inspection dates may lag a few years for some bridges.

**Implications for our acquisition layer**

Do not collapse the extract into one row per bridge-year before retaining:
- original submittal year and any submittal/version identifier exposed by the export;
- original structure number as reported in that year;
- latest-year structure number supplied by InfoBridge;
- inspection date as reported in that record;
- all source attributes and source units;
- duplicate/multiple-submittal status;
- export date, selected attributes, filters, and selection criteria.

Treat the InfoBridge latest-year number as a candidate identity association supplied by the portal. Preserve the historical source number and independently compare against NBI/SNBI identity history and our bridge identity-link table. It is not a substitute for the identity-resolution audit.

**Unresolved acquisition questions**
- Maximum export row/attribute limits and whether they vary by selection size.
- Whether all-year exports include every historical submittal or a selected/filtered representation when multiple submittals exist.
- Whether CSV graph exports expose the exact underlying year, submittal, and condition values with enough precision for reproducible analysis.
- Whether InfoBridge exposes a stable downloadable/API interface suitable for scheduled ingestion.
- Whether the same bridge's historical records can be extracted in bulk by state without manual bridge selection.

These questions require an actual controlled export and file inspection. They are not answered by the public page description alone.

## 3. Time model: preserve three separate clocks

For each condition observation, retain at least:

1. **Submission/vintage time:** the NBI data submittal or archive year in which the record appears.
2. **Inspection time:** the inspection date reported in the record, with source precision and uncertainty.
3. **Observation/recording time:** when the rating was assessed or entered, if explicitly available. Do not manufacture this from submission year.

For reconstructed legacy events, retain the previously specified month precision and day-01 proxy flag. The InfoBridge warning means the interval between annual condition observations must not automatically be treated as elapsed deterioration time between inspections.

A longitudinal record can be represented as:

- physical asset identity (resolved, candidate, or unresolved);
- source record identity and vintage;
- reported inspection date (possibly missing or stale);
- condition observation and component;
- inspection-to-submittal lag, where calculable;
- identity confidence;
- source completeness and revision status.

For model training, calculate elapsed time using actual inspection dates only when their relationship to the corresponding condition observation is adequately supported. Otherwise use submittal-vintage intervals as a distinct, weaker time basis and flag them. Do not silently mix the two.

## 4. Component condition validation findings

The current FHWA SNBI Validation Logic page publishes rules for B.C.01–B.C.15. Selected findings:

- B.C.01 Deck, B.C.02 Superstructure, B.C.03 Substructure, and B.C.04 Culvert are required primary component ratings under their applicable bridge configuration rules. The published range includes 0–9 and N.
- B.C.01 should be N when all span datasets indicate no deck is present (B.SP.09 = 0).
- B.C.02 should be N when all span datasets indicate the relevant culvert/void configurations and continuity code indicate no superstructure.
- B.C.03 and B.C.04 also have configuration-dependent N rules. The exact conditional logic must be implemented from the current versioned validation rules, not approximated with one generic presence test.
- B.C.05 railing and B.C.06 railing-transition ratings are conditioned on the corresponding railing/transition presence fields.
- B.C.09 channel and B.C.10 channel-protection ratings are conditioned on whether the bridge has a waterway or relief-waterway feature.
- B.C.11 scour condition rating has a waterway/relief-waterway dependency. Temporary codes MA-T, MI-T, and MO-T are accepted for 2026–27 and excluded from 2028 onward under the published validation page.
- B.C.12 Bridge Condition Classification and B.C.13 Lowest Condition Rating Code are calculated by FHWA and must not be submitted as source observations.
- B.C.14 NSTM inspection condition is required when B.IR.01 indicates NSTM inspection is required; it should not be reported otherwise.
- B.C.15 underwater inspection condition is required when B.IR.03 indicates underwater inspection is required; it should not be reported when not required.

**Modeling consequence:** N means the component is not applicable/not present under the defined SNBI semantics; it is not a numeric rating and must not be treated as zero, failure, or missing-at-random. A valid component rating of 0 is a distinct and severe state. Temporary codes are transition-era values with field-specific semantics and must not be numerically coerced.

## 5. Element-condition validation findings

The current validation page also establishes checks for the Elements dataset:

- B.E.01 element number must be valid under the SNBI element-number list.
- B.E.02 parent-element number has conditional requirements for wearing-surface/protective-coating element numbers.
- B.E.03 element total quantity must be numeric, nonzero, no longer than eight digits, and a whole number.
- B.CS.01 through B.CS.04 condition-state quantities must be numeric whole numbers and are required for each reported element.
- B.E.03 total quantity must equal the sum of B.CS.01, B.CS.02, B.CS.03, and B.CS.04 for that element.

These are data integrity constraints, not evidence that condition-state quantities are directly comparable across different element definitions, units, inspection practices, or reporting coverage. Retain element number, parent element, unit, total quantity, all four state quantities, bridge identity, source vintage, and source record lineage.

The public InfoBridge page also presents National Bridge Elements with total quantity, CS1–CS4, and a Health Index, plus historical NBE Health Index graphs. This provides a potential bridge between SNBI element data and longitudinal condition-state analysis. The exact Health Index formula, normalization, aggregation, and vintage comparability must be checked in InfoBridge documentation before adopting it as a model target or composite measure.

## 6. Implications for predictive model design

### Required observation distinctions
- Bridge-level component condition snapshot.
- Element-level condition-state quantity snapshot.
- Inspection event.
- Inspection date and interval metadata.
- NBI/SNBI submission vintage.
- Physical intervention/work event.
- Identity-link event or uncertainty.

### Prohibited shortcuts
- Do not use annual NBI submittal year as an assumed inspection date.
- Do not assume one submission per bridge-year.
- Do not use InfoBridge's latest-year structure-number field as an unquestioned immutable asset key.
- Do not treat component rating N as zero or as a numeric ordinal state.
- Do not report FHWA-calculated B.C.12/B.C.13 as observed values.
- Do not equate element CS quantities with component ratings.
- Do not assume InfoBridge's Health Index is a validated deterioration target until its calculation and comparability are verified.
- Do not interpret a change in condition rating as a repair without independent intervention evidence.

### Recommended next controlled test
Select a small, documented sample of bridges with multiple NBI vintages, including at least one bridge with a structure-number change and one with multiple submittals in a year if available. Export all years and a narrow set of fields: structure number, latest-year structure number, state, year built, structure type/material, length/area, inspection date, deck/superstructure/substructure/culvert ratings, scour/channel ratings, and relevant work/intervention fields if exposed. Separately save the historical condition graph CSV. Compare row counts, dates, rating values, duplicates, and identity associations. Record the exact filters and export settings.

Do not scale to state/national bulk ingestion until this test proves the export semantics and limits.

## 7. Source register

- FHWA LTBP InfoBridge Data portal: https://infobridge.fhwa.dot.gov/Data
  - Publicly documents selection across NBI submittals since 1993, export options, historical structure-number caveat, multiple-submittal warning, historical condition graph CSV, NBE condition-state display, and inspection-date lag warning.
- FHWA InfoBridge Update Notes: https://infobridge.fhwa.dot.gov/Page/infobridge_update_notes
  - January 2021 update documents the All Submittals option for historical NBI data since 1993 and historical-data selection.
- FHWA SNBI Data Validation Logic, version 1.2: https://www.fhwa.dot.gov/bridge/snbi/data_validation_logic.cfm
  - Component rating, conditional applicability, temporary scour codes, and element quantity validation rules.
- FHWA Specifications for the National Bridge Inventory, March 2022 with Errata No. 1: https://www.fhwa.dot.gov/bridge/snbi/errata1_to_snbi_march_2022_publication.pdf
  - Component rating definitions and FHWA-calculated bridge condition classification.
- FHWA NBI Data Downloads: https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm
  - Annual submission/update/finalization caveats and 2026–27 SNBI transition notes.

## 8. Evidence classification and limits

**Source-reported:** InfoBridge portal functions and warnings; FHWA validation requirements; SNBI component and element field semantics.

**Derived design recommendations:** Separate submission time from inspection time; preserve multiple submittals; treat identity crosswalks as candidate associations; maintain separate component and element condition datasets.

**Not established:** Successful export, actual row-level history, bulk/API access, completeness of historical inspection dates, InfoBridge Health Index formula suitability, and state/national longitudinal coverage.

This audit is a research/design artifact. It does not constitute a calibrated deterioration model or a production ingestion implementation.
