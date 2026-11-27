# Bridge identity and longitudinal observation test cases

**Status:** Design/test specification; fixtures are synthetic unless explicitly identified as source-derived.  
**Purpose:** Prevent false asset creation/removal, false condition transitions, and false inspection-to-condition links before building longitudinal bridge cohorts.

## 1. Source-derived rules that the tests enforce

1. InfoBridge All Years export can include historical NBI records with previous Item 8 structure numbers. It adds a Latest Year NBI Structure Number column to help associate rows with a current structure. This is a candidate association, not proof of immutable physical identity.
2. InfoBridge warns that a bridge may have multiple NBI submittals in one year. Preserve every submittal row and its source identity.
3. InfoBridge historical condition graphs plot condition ratings as reported under each NBI submittal; for some bridges, the inspection dates behind those ratings may lag by a few years.
4. SNBI inspection events are many-to-one with a bridge. Each performed inspection is reported as an event; different inspection types on the same date are separate event datasets. Previously accepted events need not be resubmitted unless corrected.
5. FHWA's rulemaking response states that element-level and component condition data are inclusive of the results of all inspections performed since the last data submission to FHWA. These condition observations are therefore not necessarily one-to-one with a single inspection event.
6. Legacy inspection-event reconstruction uses a day-01 proxy for MMYY dates and deduplicates repeated MMYY dates across annual datasets, using the most recent data for a single date. This is a transition mapping rule, not proof that the exact inspection day is known.
7. Current SNBI B.ID.03 Previous Bridge Number is limited to 15 characters under Validation Logic v1.2; report 0 when no previous bridge number exists. Errata No.2 redlined multi-predecessor proposals are not operative current rules.
8. Legacy NBI Item 8 is not an immutable physical-asset key. Structure-number history and identity resolution must be modeled explicitly.

## 2. Identity resolution test cases

All identifiers and records in this section are invented fixtures designed to test logic. They are not real bridge histories.

| ID | Synthetic input | Expected behavior | Failure prevented |
|---|---|---|---|
| ID-01 | Same source structure number, same location and attributes, consecutive vintages | Candidate continuity link; retain each annual observation | Treating snapshots as new assets |
| ID-02 | Structure number changes; InfoBridge latest-year number associates both rows | Preserve both original numbers and candidate portal association; create versioned identity link with method/source/confidence | False removal plus false construction |
| ID-03 | Same structure number reused at a different location after a bridge is removed | Do not auto-merge; flag collision and require corroboration | Two physical bridges collapsed into one |
| ID-04 | Same location but materially different span/geometry and overlapping records | Do not assume identity from location alone; evaluate replacement/parallel bridge possibilities | Replacement misclassified as rehabilitation |
| ID-05 | SNBI BID03 contains previous number and BID01 current number | Store predecessor relation; validate current 15-character rule; preserve raw values | Lost lineage or invalid parsing |
| ID-06 | BID03 is 0 | Normalize to explicit no-reported-predecessor state while preserving raw 0 | False predecessor asset named zero |
| ID-07 | Two bridges merge into one reported structure, or one structure splits into two | Identity graph must support one-to-many and many-to-one lineage internally, but only encode source-supported links; unresolved topology remains unresolved | Forced one-to-one identity |
| ID-08 | State/jurisdiction ownership changes but physical structure continues | Record jurisdiction/ownership event; no national physical entry/exit | False national inventory change |
| ID-09 | Bridge falls out of one year's archive and reappears later with same or changed number | Mark gap; do not infer demolition/reconstruction from absence | False asset exit and entry |
| ID-10 | InfoBridge latest-year ID conflicts with independently observed location/geometry continuity | Retain conflict; downgrade confidence; do not overwrite source identifiers | Blind trust in derived crosswalk |
| ID-11 | Leading zeros differ (0007 vs 7) | Preserve source strings; do not normalize away zeros without a documented year/source-specific rule | Identifier collision |
| ID-12 | Duplicate rows within one source file with same record key | Retain raw rows, flag duplicate, resolve only under documented duplicate policy | Silent data loss |

### Identity-link record requirements

Every link should retain:
- predecessor source identifier and successor/current source identifier;
- source system and source vintage;
- relationship type (renumbered, replaced, partially retained, split, merged, jurisdiction transfer, candidate only, unresolved);
- matching method and evidence fields;
- confidence class and reason;
- reviewer/decision provenance where manually resolved;
- effective or observed dates where known;
- raw source identifiers unchanged.

Never let a confidence score replace the evidence description. A high-scoring probabilistic match is still a match hypothesis until corroborated.

## 3. Longitudinal observation test cases

| ID | Synthetic input | Expected behavior | Failure prevented |
|---|---|---|---|
| OBS-01 | Condition rating repeats across annual submissions, but inspection date is unchanged | Treat as repeated/reported snapshot unless source indicates a new observation; do not create a new inspection | Inflated inspection count |
| OBS-02 | Condition changes in annual vintage, but inspection date is old/unchanged | Flag timing ambiguity; do not assign transition to vintage-to-vintage elapsed time as a physical deterioration interval | False deterioration rate |
| OBS-03 | New inspection event occurs between submissions; next condition snapshot reflects it | Associate temporally as candidate only unless source explicitly links it; retain event and snapshot separately | False one-to-one event link |
| OBS-04 | Multiple inspection types on same date | Store separate event records keyed by bridge + inspection type + begin date | Event collision |
| OBS-05 | Multiple inspections since last FHWA submission contribute to one condition snapshot | Store all inspection events and one submission-level condition snapshot; association is many-to-many/ambiguous unless documented | False single-event attribution |
| OBS-06 | Component rating improves, no verified work event exists | Record rating change; do not label as repair or rehabilitation | False intervention inference |
| OBS-07 | Verified repair is completed, but rating does not improve immediately | Retain intervention and unchanged rating; allow future effect to be estimated | Assumption that work must instantly improve rating |
| OBS-08 | Bridge replaced; successor has new age/geometry/area and predecessor link | Close predecessor, create successor; do not treat successor as predecessor's rating improvement | Artificial condition recovery |
| OBS-09 | Legacy MMYY inspection date repeated in adjacent annual archives | Deduplicate event per canonical asset + type + month under documented mapping; use latest data for that date; preserve all source appearances | Duplicate reconstructed inspections |
| OBS-10 | Legacy Item 8 changes but MMYY date repeats | Do not create new event solely because identifier changed; use identity crosswalk and preserve uncertainty | Duplicate event due to renumbering |
| OBS-11 | Two different inspection types share MMYY | Keep separate events by inspection type | Incorrect deduplication |
| OBS-12 | Exact inspection day unavailable; legacy date is MMYY | Store month precision and day-01 proxy flag; never imply observed day 01 | False date precision |
| OBS-13 | Annual file has condition snapshot but no usable inspection date | Keep condition observation with unknown inspection timing; no fabricated event date | Fabricated temporal anchor |
| OBS-14 | New submission corrects a previously accepted SNBI inspection event using same type and begin date | Preserve source submission history and current accepted representation; do not count correction as a second physical inspection | Duplicate inspection count |
| OBS-15 | Component is N (not applicable) in one vintage and numeric later | Validate configuration changes and source-era mapping; do not treat N as numeric zero or ordinary deterioration transition | Invalid ordinal transition |
| OBS-16 | Component rating is numeric 0 | Preserve as valid severe rating where applicable; never conflate with N or null | Misclassified missingness |
| OBS-17 | 2026–27 temporary code appears in an applicable field | Preserve raw value and transition status; use field-specific mapping; do not numeric-coerce | Invalid numeric rating |
| OBS-18 | 2028+ record contains a transition-only temporary code | Flag validation failure/unsupported code under the applicable post-transition rules | Silent acceptance of invalid value |

## 4. Required data model keys

### Source record
source_record_id should be a stable internal key derived from source file/vintage + row or JSON object identity. Retain:
- source file checksum and filename;
- source vintage/submittal;
- source row/object ordinal;
- original bridge number;
- raw payload or immutable raw-row reference;
- ingestion timestamp and parser/schema version.

Ordinal is provenance, not a durable physical-asset identifier.

### Physical asset
bridge_asset_id is an internal, stable identifier created by the model. It must not be equated with NBI Item 8, SNBI BID01, or InfoBridge's latest-year bridge number.

### Identity link
bridge_identity_link_id links two source identifiers or asset hypotheses with a relationship type, evidence, method, confidence, and provenance.

### Condition observation
condition_observation_id identifies a condition snapshot:
- bridge asset candidate / identity confidence;
- component code;
- raw rating value;
- normalized categorical state, only where semantics support it;
- source era and source vintage;
- inspection date as reported, with precision;
- submission/vintage date;
- date-lag indicator or unknown status;
- source mapping/validation rule version;
- observation coverage and quality flags.

### Inspection event
inspection_event_id identifies an event by source-supported identity. For SNBI, use bridge + inspection type + inspection begin date as the core natural-key candidate, while preserving source event/submission provenance and correction history.

### Event-observation association
Use a separate association table:
- condition observation ID;
- inspection event ID;
- association type (explicit, source-mapped, temporal candidate, ambiguous, no link);
- evidence and confidence;
- association rule/version.

Do not force every condition snapshot to one inspection event. One condition snapshot may reflect several inspections; one inspection may contribute to multiple condition fields.

### Intervention event
Store physical work separately from ratings and inspections:
- intervention type/scope/component;
- planned/funded/obligated/awarded/started/completed/verified stage;
- source and evidence;
- bridge identity and confidence;
- completion date and uncertainty;
- pre/post observation windows.

## 5. Validation and cohort admission gates

A record can be retained in the research database without being admitted to a predictive training cohort.

### Identity gate
- confirmed or explicitly bounded candidate identity;
- no unresolved identifier collision that could merge two assets;
- predecessor/successor events separately represented.

### Time gate
- source vintage known;
- inspection date precision retained;
- no assumption that vintage year equals inspection year;
- observation timing class assigned (actual date, month proxy, vintage-only, unknown).

### Measurement gate
- source-era coding system known;
- component and element condition kept separate;
- N, null, blank, temporary code, and numeric 0 remain distinct;
- no numeric interpolation across ordinal categories without validation.

### Event gate
- repeated archive appearances distinguished from new inspections;
- multiple types on one date preserved;
- corrections distinguished from new physical inspections;
- no repair inferred from rating improvement.

### Training cohort policy
Classify observations:
- A — eligible: identity and observation timing adequately supported, measurement semantics compatible.
- B — conditional: usable only in sensitivity analysis or a model that explicitly accommodates uncertainty.
- C — excluded from transition calibration: unresolved identity, incompatible measurement regimes, unknown timing for elapsed-time estimation, or invalid/unresolved source values.

Excluded observations remain in the research store with exclusion reasons. Never delete difficult records to make a cleaner-looking trend.

## 6. Synthetic unit-test fixture plan

Build a small machine-readable fixture set with:
- source records for two or three fictional bridges;
- multiple vintages;
- one structure-number change;
- one reused identifier collision;
- one annual archive gap;
- multiple inspections between submissions;
- repeated legacy MMYY date;
- two inspection types on one date;
- one correction to a prior SNBI event;
- one valid zero rating, one N, one null, and one temporary code;
- one replacement with predecessor/successor lineage;
- one jurisdiction transfer.

Expected outputs should include:
- physical asset candidates;
- identity links and confidence;
- inspection events;
- condition observations;
- event-observation associations;
- inventory events;
- training eligibility and exclusion reasons.

All fixtures must be clearly labeled synthetic. They are software tests, not empirical evidence or calibration data.

## 7. Acceptance criteria before real-world longitudinal training

The test harness passes only if:
1. No synthetic identity collision is silently merged.
2. No identifier change alone creates physical entry/exit.
3. No archive absence alone creates physical removal.
4. Multiple same-year submittals remain distinguishable.
5. Multiple inspection types on one date remain separate.
6. Repeated legacy MMYY events are deduplicated according to the documented mapping rule without losing source appearances.
7. Inspection corrections are not counted as additional physical inspections.
8. Condition snapshots are not forced into one-to-one inspection links.
9. No repair is inferred from rating improvement alone.
10. N, null, blank, temporary code, and numeric zero remain distinct.
11. Replacement creates a new successor asset with its own baseline.
12. Every exclusion from a training cohort has a reproducible reason.

## 8. Source register

- InfoBridge Data: https://infobridge.fhwa.dot.gov/Data
- InfoBridge Performance History: https://infobridge.fhwa.dot.gov/PerformanceDashboard
- InfoBridge Update Notes: https://infobridge.fhwa.dot.gov/Page/infobridge_update_notes
- FHWA SNBI Data Validation Logic v1.2: https://www.fhwa.dot.gov/bridge/snbi/data_validation_logic.cfm
- FHWA SNBI March 2022, Section 6.2 Inspection Events and Section 7 condition data: https://www.fhwa.dot.gov/bridge/snbi/snbi_march_2022_publication.pdf
- Federal Register, FHWA response on condition data reflecting inspections since last submission: https://www.govinfo.gov/content/pkg/FR-2022-05-06/pdf/2022-09512.pdf
- FHWA legacy-to-SNBI Detailed Coding Map: https://www.fhwa.dot.gov/bridge/snbi/codemapping.cfm

## 9. Evidence classification and limitations

**Source-derived:** InfoBridge export caveats, SNBI inspection event structure, legacy inspection-event reconstruction behavior, condition data's relationship to all inspections since the prior FHWA submission, current B.ID.03 validation, and field-specific temporary-code rules.

**Design recommendations:** Internal asset IDs, identity graph, observation-event association table, training admission gates, and test cases.

**Synthetic only:** Every example record in Sections 2, 3, and 6. No synthetic fixture is a claim about a real bridge.

**Not yet established:** Real InfoBridge export row semantics in a downloaded sample, actual bulk export limits, complete historical identity lineage, or the empirical frequency of ambiguous observation-event relationships.
