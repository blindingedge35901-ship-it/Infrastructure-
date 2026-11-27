# Historical Inspection Event Reconstruction from Legacy NBI Data

**Status:** FHWA transition mapping reviewed; event reconstruction requirements documented.  
**Research date:** 2026-11-26  
**Scope:** Conversion of legacy Coding Guide inspection fields into SNBI inspection-event records.

## Executive finding

FHWA's Detailed Code Mapping defines how inspection events are created from historical Coding Guide data. It uses legacy inspection type/date/interval fields and requires comparison with previous annual NBI datasets to determine whether an observation represents an initial or routine inspection event.

The legacy inspection date is recorded only as month and year. The transition constructs an SNBI date using day 01 as a proxy. This is not an observed day-of-month.

The mapping also instructs agencies to repeat the process against prior NBI datasets, year by year, and not to create a duplicate inspection event when the same inspection date appears in multiple consecutive annual datasets. The most recent data for a single date should be used.

**Model implication:** The bridge model can build a historical inspection-event series from annual snapshots, but those events must carry reconstructed-date precision and source-vintage lineage. Annual NBI rows are not themselves annual inspections.

## 1. FHWA's mapped inspection fields

For routine and initial inspection events, the detailed map uses:
- Coding Guide Item 90: inspection date, MMYY;
- Coding Guide Item 91: inspection frequency, XX;
- Coding Guide Item 8: structure number, used to compare the bridge with prior-year data.

The mapping creates:
- B.IE.01 Inspection Type;
- B.IE.02 Inspection Begin Date;
- B.IE.05 Inspection Interval.

The transition logic shown by FHWA is:
- If Item 8 matches a previous year of data, classify the event as Routine (B.IE.01 = 2).
- Otherwise, classify it as Initial (B.IE.01 = 1).
- Convert MMYY into 20YYMM01 for the date.
- Transfer the interval from Item 91, dropping a leading zero where directed.

This is a transition rule, not proof that every first appearance of a bridge in the archive is its actual first inspection in the physical asset's life. It is an initial event within the reconstructed historical series under the FHWA mapping logic.

## 2. Deduplication across annual snapshots

FHWA's note instructs the user to repeat the actions for previous NBI datasets, going back year by year, until the first dataset. It further states:
- Do not create an inspection event for an MMYY date already used.
- The same inspection date may appear in multiple consecutive datasets.
- Use the most recent data for a single date.

This is essential because annual NBI files are repeated inventory snapshots, not independent inspection-event logs. Treating every row/year as a separate inspection would overcount inspections and distort inspection intervals.

Recommended deduplication key:
- canonical bridge asset ID;
- inspection type;
- reconstructed inspection year/month (MMYY).

Do not deduplicate solely by the raw structure number across all time because bridge structure numbers can change. Use the identity crosswalk and preserve the source structure number used in each annual file.

If multiple records for the same asset/type/month contain conflicting interval or inspection metadata, retain the most recent source vintage as FHWA directs, but preserve the prior versions and log the conflict rather than deleting history.

## 3. Date precision and event-time uncertainty

The generated SNBI date uses day 01 because the legacy Coding Guide date contains only month and year.

Store at least:
- inspection_date_reconstructed (YYYY-MM-01);
- inspection_date_precision = MONTH;
- inspection_month;
- inspection_year;
- inspection_day_observed = false;
- date_reconstruction_rule and version;
- source_item_90_raw;
- source_submission_year;
- source_vintage.

Do not treat the first day of the month as the actual inspection day. For elapsed-time calculations, use month-level precision or represent an interval bounded by the month rather than claiming exact day-level elapsed time.

## 4. Initial versus routine classification caveat

The FHWA mapping uses whether Item 8 matches a previous year of data to classify Routine versus Initial. This is a transition reconstruction rule. It does not establish:
- the bridge's first-ever inspection;
- whether the asset was physically new;
- whether the inspection type was independently confirmed;
- whether an inspection occurred exactly on the constructed day;
- whether an identifier change or historical gap caused the first appearance.

The asset identity crosswalk must be applied before interpreting first appearance as a new asset or initial inspection event. An identifier discontinuity may otherwise create a false "initial" event.

## 5. Other inspection-event types

The detailed mapping separately describes NSTM, underwater, and special inspection events using their corresponding legacy fields and dates. The mapping includes cases where a qualifying type indicator and date create an event, and cases where no qualifying type/date combination results in no event.

The routine/initial, NSTM, underwater, and special event logic should be implemented as separate event-type rules. Do not infer that an absence of one event type means no inspection of any kind occurred.

The source text contains a possible typographical inconsistency in one NSTM description ("NTSM"). This should be checked against the actual spreadsheet and authoritative SNBI definitions before the label is encoded.

## 6. Recommended event table

A normalized event table should include:
- inspection_event_id (internal stable ID);
- canonical_asset_id;
- source_structure_number;
- inspection_type_code;
- inspection_type_description;
- inspection_date_value;
- inspection_date_precision;
- inspection_date_is_reconstructed;
- inspection_interval_value;
- inspection_interval_unit;
- source_item_90_raw;
- source_item_91_raw;
- source_item_type_indicator_raw;
- source_submission_year;
- source_artifact_id;
- source_record_id;
- deduplication_group_id;
- selected_source_vintage;
- event_reconstruction_rule_version;
- identity_match_confidence;
- conflict_or_ambiguity_flag.

Do not assume that inspection interval is always in months until the item definition and source unit are applied. Preserve the raw source code and its defined unit.

## 7. Model uses and limitations

A reconstructed event history can support:
- inspection-frequency distributions;
- elapsed time since last recorded inspection, with month-level precision;
- cohorts by inspection type;
- comparison of inspection intervals with risk-based requirements;
- identification of gaps and anomalous histories;
- linking inspection events to condition observations and interventions.

It cannot, by itself, support:
- exact inspection-day analysis;
- proof of an inspection when source fields are incomplete or invalid;
- direct measurement of inspector workload;
- inference that every annual inventory change represents a new inspection;
- causal estimates of inspection effects on deterioration or failure.

For inspection interval compliance, the model must compare actual event dates and type-specific requirements where possible. The recorded Item 91 interval is not itself evidence that inspections occurred at every scheduled interval.

## 8. Validation and tests required before implementation

Build tests for:
1. A bridge with the same MMYY date repeated across several annual files: one event only.
2. Same asset/date with updated interval metadata: select latest vintage but preserve prior values and conflict history.
3. Structure number changes with a verified identity link: do not create a false new-asset event.
4. A bridge first appearing in the archive: classify as initial under the transition rule, but mark first observed in archive rather than first-ever inspection.
5. Missing Item 90 or Item 91: apply source-defined null handling; do not fabricate an event date or interval.
6. Different inspection types on the same month: retain distinct events.
7. Month-level date precision: never expose day 01 as observed fact.
8. Multiple annual records and conflicting dates: preserve provenance and log resolution.

## Sources

1. FHWA, Detailed Code Mapping for Individual Data Items, inspection event mappings for routine/initial, NSTM, underwater, and special inspections: https://www.fhwa.dot.gov/bridge/snbi/codemapping.cfm
2. FHWA, Data Crosswalk for Over Records and Under Records: https://www.fhwa.dot.gov/bridge/snbi/datacrosswalk.cfm
3. FHWA, SNBI Data Validation Logic: https://www.fhwa.dot.gov/bridge/snbi/data_validation_logic.cfm
4. FHWA, SNBI, March 2022, definitions for inspection event data items: https://www.fhwa.dot.gov/bridge/snbi/snbi_march_2022_publication.pdf

## Evidence classification

- **Source-reported:** Inspection event fields, reconstructed date format, initial/routine mapping, repeated historical processing, and deduplication instruction.
- **Derived:** Annual NBI records must be treated as snapshots and deduplicated into inspection events to avoid overcounting.
- **Model recommendation:** Preserve month-level date precision, source vintage, identity links, and event reconstruction rules.
- **Unresolved:** Verify the apparent NSTM/NTSM text inconsistency against the detailed workbook and base SNBI item definitions.
