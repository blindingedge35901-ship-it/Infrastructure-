# Bridge Condition Ratings: Measurement Scale, Inspector Variability, and Predictive Use Audit

**Status:** FHWA SNBI definitions and FHWA research on NBI condition-rating limitations reviewed.  
**Research date:** 2026-11-26  
**Scope:** Measurement properties and modeling treatment of component condition ratings and element condition states.

## Executive finding

NBI/SNBI component condition ratings are discrete, judgment-based ordinal codes, not continuous physical measurements. FHWA's Long-Term Bridge Performance (LTBP) Bridge Performance Primer explicitly cautions that the 0–9 scale is not readily amenable to rigorous mathematical analysis that treats every one-point change as an equal physical increment.

The SNBI requires condition ratings to reflect defect type, location, severity, extent, and effects on component strength or performance. Ratings may change after each inspection. The NBI does not provide all underlying defect locations, quantities, causes, or incipient deterioration.

**Model decision:** Preserve ratings as ordinal categories and model transitions probabilistically or with ordinal methods. Do not assume a one-point rating change represents a constant amount of physical deterioration or improvement. Keep component ratings, element condition quantities, inspection events, and physical interventions separate.

## 1. What the rating measures

SNBI Section 7.1 says component condition ratings provide information about existing field condition of the bridge and waterway. The rating considers:
- type of defect;
- location of defect;
- severity of defect;
- extent of defects throughout the evaluated component;
- degree to which defects affect strength and/or performance.

The SNBI defines a defect broadly as a problem that may be caused by deterioration, damage, or an inherent defect. An inherent defect is not necessarily damage or deterioration; it can be characteristic of the material or result from normal construction practice.

The specification distinguishes:
- minor defect: deterioration or damage has initiated but is not significant;
- moderate defect: significant deterioration/damage, but strength and performance are not affected;
- major defect: affects strength and/or performance, as determined by structural and/or hydraulic review; for joints, bearings, railings, and railing transitions, it prevents the component functioning as intended.

**Implication:** A rating is an engineering judgment about the existing condition of a defined component, not a direct measurement of material loss, remaining service life, load capacity, or probability of failure.

## 2. Discrete ordinal rating scale

The legacy NBI condition rating scale runs from 0 (failed) to 9 (excellent), with definitions tied to qualitative condition descriptions. The LTBP primer notes that ratings 4–7 are most common for bridges in service.

The qualitative descriptions are not equal-interval physical units. A move from 8 to 7 is not established as the same physical deterioration increment as a move from 5 to 4. The LTBP primer explicitly warns that discrete integer codes are not continuous measurements suitable for treating each one-point change as an equal increment.

**Model treatment:**
- Store the raw rating as an ordered category.
- Use transition matrices, ordinal regression, or other models appropriate to ordered discrete outcomes.
- If using a numeric score for display or a composite index, document that it is a coding convention, not a physical interval scale.
- Do not compute linear deterioration rates by simply dividing rating-point change by elapsed years unless a separately validated model supports that interpretation.
- Keep category thresholds and source-era definitions versioned.

## 3. Inspector variability and measurement uncertainty

FHWA's 2001 *Reliability of Visual Inspection for Highway Bridges* study involved 49 inspectors from 25 State agencies and seven test bridges. It found that assigned condition ratings varied across as many as five different rating values. The study estimated 68% of ratings would fall within one point of the average and 95% within two points.

This is historical evidence from a limited study, not a current national error distribution. It should not be applied as a universal error model or used to mechanically adjust individual ratings.

**Model treatment:**
- Treat observed ratings as measurements with uncertainty.
- Preserve inspector and QC/QA metadata where supplied.
- Do not assume every rating change is a physical change.
- When available, use repeated inspections, element-level detail, photos, owner inspection files, and independent evaluations to help distinguish physical change from rating variability.
- Use sensitivity analysis to assess how plausible rating uncertainty affects transition estimates.

## 4. Limits of NBI component condition data

FHWA's LTBP Bridge Performance Primer identifies important limitations:
- NBI does not describe condition of every individual subelement such as beams, pier columns, and abutments.
- It does not quantify the extent and location of different conditions relative to the geometry of the inspected element.
- In most cases, ratings are based on visual inspection.
- Underlying causes such as rebar corrosion may not be identified until surface damage appears.
- NBI ratings do not reflect incipient degradation.

**Implication:** The NBI component rating series is suitable for national/state inventory and broad condition-trend analysis, but it is not a complete mechanistic deterioration dataset. It cannot, by itself, identify the onset or cause of deterioration or estimate precise remaining service life.

## 5. Component ratings versus element condition states

These are different measurement systems and must not be conflated.

### Component ratings
- Bridge-level items such as deck, superstructure, substructure, culvert, bearings, joints, channel, and scour.
- In the SNBI Primary Data Set, component ratings have a one-to-one relationship with the bridge.
- Values may change after each inspection.
- B.C.12 and B.C.13 are FHWA-calculated summary values, not inspector-reported values.

### Element condition states
- Element-level quantities assigned to four states: CS1 Good, CS2 Fair, CS3 Poor, CS4 Severe.
- Reported for each element present on a bridge.
- Each element's four quantities must sum to its total quantity.
- Element reporting is required for NHS bridges and optional for non-NHS bridges under the SNBI.
- Element condition data may change after each inspection.

**Implication:** Element-level data can add severity and extent information, but national coverage is not uniform. Do not treat absence of element data as good condition, nor compare NHS and non-NHS element coverage without accounting for reporting eligibility.

## 6. Component summary classification

SNBI B.C.12 Bridge Condition Classification and B.C.13 Lowest Condition Rating Code are calculated by FHWA from component ratings. They are not intended to be reported by inspectors.

For applicable component ratings:
- Good: lowest rating is 7, 8, or 9.
- Fair: lowest rating is 5 or 6.
- Poor: lowest rating is 0 through 4.

The NHS performance measures use deck-area weighting for Good and Poor condition; Fair is not part of either target measure.

**Model treatment:** Retain all individual component ratings and the FHWA-calculated classification. Do not use the single Good/Fair/Poor category as a substitute for the component vector. It loses information about which component controls the classification and the condition of the other components.

## 7. Avoiding false deterioration and repair signals

A rating can change because of:
- physical deterioration;
- new damage;
- rehabilitation, repair, or replacement;
- changed inspection access or coverage;
- inspector judgment or rating variability;
- updated guidance, definitions, or source coding;
- data correction or transition mapping;
- bridge identity or reporting changes.

A rating improvement does not prove a repair occurred. A rating decline does not prove deterioration was the only cause.

The model should maintain separate linked histories for:
- inspection events;
- component condition observations;
- element condition observations;
- work/intervention events;
- asset identity and geometry changes;
- source and coding-rule changes.

Intervention effects should be estimated only when completed work can be linked to the affected bridge/component and followed by comparable observations.

## 8. Predictive modeling implications

Recommended initial model:
1. Reproduce observed ordinal transition counts by component and elapsed inspection time.
2. Stratify by bridge type, material, age, geography/environment, traffic/exposure, inspection interval, and source era where data support it.
3. Separate verified and transition-derived observations.
4. Track missingness and inspection coverage.
5. Compare simple persistence/transition baselines with candidate ordinal or multi-state models.
6. Validate on later time periods and holdout bridges, not only random rows.
7. Quantify uncertainty and sensitivity to rating variability and source breaks.
8. Introduce intervention effects only after reliable work-event linkage.

Do not use fixed coefficients or linear rating-point deterioration rates without empirical validation.

## 9. Sources

1. FHWA, *Specifications for the National Bridge Inventory* (SNBI), March 2022, Sections 6.2 and 7.1–7.3: https://www.fhwa.dot.gov/bridge/snbi/snbi_march_2022_publication.pdf
2. FHWA, *LTBP Bridge Performance Primer*, FHWA-HRT-13-051, especially the discussion of NBI condition data limitations and discrete rating codes: https://www.fhwa.dot.gov/publications/research/infrastructure/structures/ltbp/13051/
3. FHWA, *Reliability of Visual Inspection for Highway Bridges*, FHWA-RD-01-021: https://www.fhwa.dot.gov/publications/research/nde/01021.cfm
4. FHWA, *Bridge Condition Performance Measures FAQ*: https://www.fhwa.dot.gov/tpm/faq.cfm
5. FHWA, *NBI annual data download page*: https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm

## Evidence classification

- **Source-reported:** SNBI rating criteria and relationships; FHWA primer's limitations; 2001 study findings and sample.
- **Derived:** Ratings should be treated as ordinal observations with measurement uncertainty, not continuous equal-interval measurements.
- **Model recommendation:** Use ordinal/multi-state methods and separate physical intervention evidence from rating changes.
- **Unresolved:** Current national distribution of inspector rating variability and the availability of consistent field-level inspection documentation across owners.
