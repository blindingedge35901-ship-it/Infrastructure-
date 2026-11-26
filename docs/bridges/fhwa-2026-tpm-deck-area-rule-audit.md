# FHWA 2026–2027 TPM Deck-Area Calculation Rule Audit

**Status:** Source-specific rule verified; conflicting public-page description retained as an unresolved documentation inconsistency.  
**Research date:** 2026-11-26  
**Scope:** FHWA computation of NHS bridge-condition performance measures during the 2026–2027 SNBI transition. This is not a universal deck-area rule for every analytical purpose.

## Executive finding

FHWA's November 3, 2025 *Computation Procedure for the Transportation Performance Management Bridge Condition Measures* specifies that, for the 2026 and 2027 NBI transition datasets:

1. If reported Bridge Width Out-to-Out (BG05) is greater than zero, calculate deck area as Total Bridge Length (BG02) × BG05.
2. Otherwise, calculate deck area as BG02 × Approach Roadway Width (BG09).
3. Round the result to the nearest 0.1 square foot using half-up rounding.
4. Exclude a record from the federal measure if both BG05 and BG09 are missing or zero.

A separate FHWA Frequently Requested NBI Information page describes the 2026–2027 fallback using a 10-foot threshold: BG05 is used when it is at least 10 feet; otherwise BG09 is used. These rules differ for records with a positive BG05 below 10 feet.

**Model decision:** Preserve both source descriptions. When reproducing FHWA's formal NHS performance measure, implement the dedicated November 2025 computation procedure as the procedure-specific authority, while recording the public-page discrepancy. Do not silently substitute the 10-foot rule. For general bridge inventory analytics, retain BG02, BG05, BG09 and the computed area method as separate fields so alternative definitions can be tested.

## Source-specific rule

The November 3, 2025 procedure (FHWA-HIF-25-010), Section 2.1.3 and Table 5, states that during the 2026 and 2027 transition datasets:
- BG05 > 0: BG16 = ROUND(BG02 × BG05, 1)
- Otherwise: BG16 = ROUND(BG02 × BG09, 1)
- If both BG05 and BG09 are null or zero, exclude the record from the measure.

The document specifies half-up rounding to one decimal place. This matters for reproducibility; do not rely on a language's default rounding behavior without verifying its tie-breaking convention.

The same document distinguishes the transition period from 2028 onward. Beginning with the 2028 dataset, the SNBI method uses BG02 × BG05, with BG15 Irregular Deck Area used when reported. The 2026–2027 fallback must not be carried forward as a permanent rule.

## Conflicting FHWA public description

FHWA's Frequently Requested NBI Information page describes the transition rule as:
- BG05 >= 10 feet: use BG05;
- BG05 < 10 feet or null: use BG09.

That differs from the computation procedure's BG05 > 0 condition. The disagreement is material for records where 0 < BG05 < 10 feet. No evidence reviewed in this audit establishes whether the general page is stale, simplified, or intended for a different use. Keep it logged as a source inconsistency until FHWA clarifies or updates the page.

## Separate the federal measure from the broader model

The FHWA procedure is specifically for NHS bridge-condition performance measures and the related minimum-condition and significant-progress determinations. It is not a reason to overwrite raw geometry or impose the federal deck-area calculation on every bridge-level analytical product.

Recommended stored fields:
- `total_bridge_length_bg02`
- `bridge_width_out_to_out_bg05`
- `approach_roadway_width_bg09`
- `irregular_deck_area_bg15` (when available)
- `fhwa_calculated_deck_area_bg16` (source-reported/derived field as applicable)
- `model_deck_area_value`
- `model_deck_area_method`
- `model_deck_area_rule_version`
- `area_calculation_exclusion_reason`

For each derived value, preserve source values, units, source vintage, retrieval date, formula version, rounding method, and any exclusion reason. Do not use a single generic field called `deck_area` without its method/version metadata.

## Additional transition details relevant to reproducibility

The November 2025 procedure also specifies:
- 2026 and 2027 are transition-period datasets; their data can contain Coding Guide-derived information converted to SNBI and some information collected or verified under SNBI.
- For the 2026–2027 NHS query, the procedure uses state code, NBIS bridge length >=20 feet, and at least one highway feature carried on the bridge with NHS designation.
- Condition classification uses the minimum of the four reported component ratings: deck, superstructure, substructure, and culvert. A record can be classified from one or more reported component ratings; records with all four missing are excluded from the measure.
- For 2028 onward, the NHS query uses NBIS Bridge Length >20 feet, rather than the transition-period >=20 feet criterion. The 2028+ area method also changes.

These rules are measure-specific. They should not be confused with the broader NBI inventory scope or a general physical bridge definition.

## Implications for the 2025–2026 baseline comparison

The published 2025 and 2026 aggregate condition tables must not be interpreted as a direct physical deterioration or repair series without controlling for:
- source-era and transition status;
- the area calculation rule actually applied;
- changes in data completeness and missing component ratings;
- inventory scope and bridge-length culvert treatment;
- bridge identity continuity and reporting changes.

The difference between aggregate Poor counts or deck areas is therefore not, by itself, evidence of a corresponding number of repairs, deteriorations, additions, or removals.

## Sources

1. FHWA, *Computation Procedure for the Transportation Performance Management Bridge Condition Measures*, FHWA-HIF-25-010, November 3, 2025, especially Sections 1.3, 2.1.1–2.1.4, Tables 3–6, and Section 2.2: https://www.fhwa.dot.gov/tpm/guidance/hif25010.pdf
2. FHWA, *Tables of Frequently Requested NBI Information*, bridge deck area definition: https://www.fhwa.dot.gov/bridge/britab.cfm
3. FHWA, *Download NBI Data Files 2026*: https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm

## Evidence classification

- **Source-reported:** The two different descriptions of the 2026–2027 deck-area rule; the transition and post-transition procedures.
- **Derived:** The discrepancy affects records with positive BG05 values below 10 feet.
- **Model recommendation:** Store raw dimensions and formula provenance; implement the dedicated computation procedure when reproducing the federal NHS measure.
- **Unresolved:** Why FHWA's general NBI information page and its dedicated computation procedure describe different transition-period thresholds.
