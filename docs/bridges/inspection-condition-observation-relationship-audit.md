# Bridge Inspection Events and Condition Observation Relationship Audit

**Status:** Base SNBI relationship rules reviewed directly in FHWA March 2022 specification; implications for longitudinal modeling documented.  
**Research date:** 2026-11-26  
**Scope:** Relationship between inspection-event records, bridge-level condition ratings, element-level condition observations, and annual submissions.

## Executive finding

The SNBI does not describe inspection events and component condition ratings as one unified event record.

It defines:
- **Inspection Events Data Set:** many-to-one relationship with a bridge; each inspection performed is reported as an event. Multiple inspection types on the same date are reported as separate inspection data sets.
- **Primary Data Set component condition ratings:** one-to-one relationship with a bridge; these values may change after each inspection.
- **Elements Data Set condition quantities:** many-to-one relationship with a bridge; reported for each element and may change after each inspection.

The specification therefore supports the interpretation that condition data are updated in relation to inspections, but it does not establish from the public annual record alone a guaranteed direct foreign-key link from every condition observation to a specific inspection event.

**Model decision:** Keep inspection events and condition observations as separate entities. Associate them only through explicit source linkage where available or through a documented temporal matching method with confidence and ambiguity flags. Never fabricate a direct event link.

## 1. Inspection Events Data Set

The March 2022 SNBI, Section 6.2, states that inspection-event data provide information about each inspection performed on a bridge and have a many-to-one relationship with a bridge.

The specification says:
- Data items are reported for each inspection performed.
- If more than one type of inspection occurs on a given date, a separate inspection data set is reported for each type.
- This identifies multiple inspection types that may occur during a calendar year or between FHWA data submittals.
- Previously accepted inspection events need not be resubmitted unless accepted data were incomplete or incorrect.
- To correct an event for a given date and type, submit a new complete event data set using the originally submitted inspection type and begin date as the event identity.

Core inspection event items include:
- B.IE.01 Inspection Type;
- B.IE.02 Inspection Begin Date;
- B.IE.03 Inspection Completion Date;
- B.IE.04 Nationally Certified Bridge Inspector;
- B.IE.05 Inspection Interval;
- B.IE.06 Inspection Due Date (calculated by FHWA);
- B.IE.07 Risk-Based Inspection Interval Method;
- B.IE.08 Inspection Quality Control Date;
- B.IE.09 Inspection Quality Assurance Date;
- B.IE.10 Inspection Data Update Date;
- B.IE.11 Inspection Note;
- B.IE.12 Inspection Equipment.

The specification's event key is based on inspection type and begin date within the bridge context. More than one inspection type on one date is not a duplicate; it is a separate event.

## 2. Component condition ratings in the Primary Data Set

Section 7.1 states that component condition ratings provide condition information for the bridge and waterway(s), are part of the Primary Data Set, and have a one-to-one relationship with a bridge. The data may change after each inspection.

Items include:
- B.C.01 Deck Condition Rating;
- B.C.02 Superstructure Condition Rating;
- B.C.03 Substructure Condition Rating;
- B.C.04 Culvert Condition Rating;
- B.C.05 Bridge Railing Condition Rating;
- B.C.06 Bridge Railing Transitions Condition Rating;
- B.C.07 Bridge Bearings Condition Rating;
- B.C.08 Bridge Joints Condition Rating;
- B.C.09 Channel Condition Rating;
- B.C.10 Channel Protection Condition Rating;
- B.C.11 Scour Condition Rating;
- B.C.12 Bridge Condition Classification (calculated by FHWA);
- B.C.13 Lowest Condition Rating Code (calculated by FHWA);
- B.C.14 NSTM Inspection Condition;
- B.C.15 Underwater Inspection Condition.

The specification says ratings must consider defect type, location, severity, extent throughout the evaluated item, and effects on strength or performance. A defect can result from deterioration, damage, or an inherent defect. An inherent defect is not necessarily evidence of damage or deterioration.

**Model implication:** A condition rating is a bridge-level condition observation, not automatically a direct measure of deterioration rate. Its change may reflect deterioration, damage, repair, changed inspection coverage, rating judgment, or source/reporting changes. The model needs additional event and work evidence before assigning cause.

## 3. Element-level condition data

Section 7.3 defines element condition quantities as part of the Elements Data Set with a many-to-one relationship to a bridge. Data are reported for each element and may change after each inspection.

Four condition-state quantities are reported:
- B.CS.01 Condition State One (general intent: Good);
- B.CS.02 Condition State Two (general intent: Fair);
- B.CS.03 Condition State Three (general intent: Poor);
- B.CS.04 Condition State Four (general intent: Severe).

The sum of all four condition-state quantities must equal the Element Total Quantity (B.E.03) for that element.

Element data are required for bridges carrying NHS routes; reporting is optional for bridges not carrying NHS routes. The specification refers to AASHTO MBEI for element defect and condition-state definitions. It also notes that specific material defects in the AASHTO MBEI are not themselves reported to FHWA.

**Model implication:** Element condition coverage is not uniform across the full national bridge inventory. Missing element data on a non-NHS bridge cannot be interpreted as good condition or a missing inspection. Element data provide more granular condition distribution than component ratings but have a different reporting scope.

## 4. FHWA-calculated values must remain distinct

B.C.12 Bridge Condition Classification and B.C.13 Lowest Condition Rating Code are calculated by FHWA from other SNBI items and are not intended to be reported by inspectors or designated agency personnel.

The lowest condition rating code is the minimum among the applicable deck, superstructure, substructure, and culvert ratings. The Good/Fair/Poor classification is based on the lowest applicable rating:
- Good: 7, 8, or 9;
- Fair: 5 or 6;
- Poor: 0, 1, 2, 3, or 4.

Store source-reported component ratings separately from calculated FHWA summary fields and any model-specific derived measure.

## 5. Event-to-condition association

The SNBI specification states that condition ratings may change after each inspection, but the public specification sections reviewed do not define a universal explicit event foreign key linking each bridge-level condition snapshot to one particular inspection event.

The annual NBI submission can include:
- a current Primary Data Set condition state;
- one or more inspection events since the previous submission;
- element condition records;
- corrections to previously accepted event records.

The condition snapshot and inspection-event history must therefore be modeled separately.

Recommended association hierarchy:
1. **Explicit source link:** use when a source record directly identifies the inspection event associated with the condition observation.
2. **Exact date/type match:** use when the condition observation has a source inspection date and type matching an event.
3. **Date-only temporal match:** associate only if one plausible event exists in the relevant time window; record the matching method and confidence.
4. **Ambiguous or no match:** leave condition-to-event link unresolved.

Do not force a one-to-one match when multiple event types occur on the same date or when only month-level legacy dates are available.

## 6. Recommended data model

### Inspection event table
One row per bridge + inspection type + begin date, with source provenance and event fields.

### Condition observation table
One row per bridge + condition observation vintage + component/measure, with:
- condition item;
- raw rating;
- normalized rating;
- source submission year;
- source artifact and record;
- inspection/observation date if explicitly supported;
- date precision;
- transition class and verification status;
- source and formula version.

### Element condition observation table
One row per bridge + element + observation vintage, with:
- element number and parent number;
- element total quantity and unit;
- CS1–CS4 quantities;
- source inspection/event association if known;
- source vintage and provenance;
- coverage/eligibility status.

### Condition-event association table
Separate relationship table:
- condition observation ID;
- inspection event ID;
- association method;
- temporal distance;
- match confidence;
- supporting source evidence;
- unresolved/conflict flag.

### Work/intervention event table
Separate from inspections and condition:
- event type;
- affected asset/component/element;
- event dates;
- work scope;
- completion/verification status;
- source evidence.

A rating improvement alone must not be classified as a repair. An inspection alone must not be classified as a physical intervention.

## 7. Longitudinal modeling implications

For each bridge, preserve:
- the annual submitted condition snapshot;
- actual inspection-event history;
- event type and date precision;
- component condition values;
- element condition distributions where reported;
- transition and verification metadata;
- work/intervention events;
- asset identity and reporting lineage.

A condition transition model should only calculate elapsed time from defensible observation dates. If the date is reconstructed from legacy MMYY, use month precision and propagate uncertainty. If the annual submission contains no direct inspection-to-condition link, do not assume that the latest event is the event that produced the reported condition values.

Condition transition cohorts should be stratified by:
- source era (legacy Coding Guide, transition SNBI, post-transition SNBI);
- condition item and component;
- bridge type/material/design where available;
- inspection interval and event type;
- transition class and verification status;
- NHS/element reporting eligibility;
- intervention history;
- identity-match confidence.

No deterioration or intervention-effect coefficients are assigned in this audit.

## 8. Validation requirements

1. Enforce one current component condition record per bridge in a given Primary Data Set vintage, while preserving prior vintages.
2. Permit multiple inspection events per bridge and multiple inspection types on one date.
3. Validate event identity using bridge + inspection type + begin date.
4. Preserve accepted historical event records when not resubmitted; absence from a later submission is not automatically deletion.
5. Check element CS1–CS4 sum equals element total quantity.
6. Flag element-data coverage separately from condition rating.
7. Verify B.C.12/B.C.13 calculations from component ratings and applicable rules.
8. Keep source-reported and FHWA-calculated fields separate.
9. Do not infer repairs from rating improvement without intervention evidence.
10. Do not assign a condition observation to an inspection event without an explicit or documented association method.

## 9. Sources

1. FHWA, *Specifications for the National Bridge Inventory* (SNBI), March 2022, Sections 6.2 and 7.1–7.3: https://www.fhwa.dot.gov/bridge/snbi/snbi_march_2022_publication.pdf
2. FHWA, Detailed Code Mapping for Individual Data Items, inspection event reconstruction: https://www.fhwa.dot.gov/bridge/snbi/codemapping.cfm
3. FHWA, NBI annual data downloads and reporting-vintage notes: https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm
4. FHWA, 2022 NBIS Q&A, inspection interval methods and tolerances: https://www.fhwa.dot.gov/bridge/nbis2022/qanda/07.cfm

## Evidence classification

- **Source-reported:** SNBI dataset relationships, event key, inspection type codes, condition item definitions, frequency of condition updates, element reporting scope, and element quantity reconciliation.
- **Derived:** A public annual condition snapshot cannot always be unambiguously assigned to a specific inspection event.
- **Model recommendation:** Store inspection events and condition observations separately and associate through explicit or confidence-scored evidence.
- **Unknown/unresolved:** Whether every jurisdiction's internal systems preserve a richer direct inspection-to-condition relationship than is available in the public NBI submittal.
