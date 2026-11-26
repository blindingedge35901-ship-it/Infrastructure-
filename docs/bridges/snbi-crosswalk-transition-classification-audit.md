# SNBI Data Crosswalk: Transition Classification and Model Use Audit

**Status:** FHWA field-level transition classifications reviewed; actual per-record verification history remains unresolved.  
**Research date:** 2026-11-26

## Executive finding

FHWA's Data Crosswalk is more than a field-name mapping. It documents how legacy Coding Guide items are converted into SNBI items and classifies transitions as:
- **Yes / clean transition:** Coding Guide values map into permanent SNBI codes. FHWA says these items should still be verified on the established timeline.
- **Partial:** Some legacy values do not map directly, may become temporary codes, or require significant assumptions. FHWA says temporary codes must be replaced, transitioned codes verified, and items that did not populate must be populated.
- **No:** The SNBI item cannot be populated from Coding Guide data and must be populated under the implementation timeline.
- **Calculate:** FHWA calculates the item from legacy inputs during transition; the crosswalk says this value is calculated for each data submittal and need not be verified.

This supplies a useful *field-level transition-risk classification*. It does not establish that a specific bridge's value was actually inspected, reviewed, corrected, or verified. Do not turn a crosswalk category into a record-level verification flag.

## General transition assumptions

FHWA's crosswalk warns that the Coding Guide does not identify multiple instances of certain feature types carried on or below a bridge. The transition therefore assumes, among other things:
- one instance of a given feature type;
- one route per highway;
- one main span set;
- one approach span set.

FHWA says these assumptions may be correct for many bridges but should be adjusted after transition where they do not apply.

The crosswalk also states:
- "Over" records carrying a highway and meeting the NBIS bridge-length designation are transitioned regardless of bridge length.
- "Under" records are transitioned only when a corresponding "over" record is transitioned.
- "Under" records without a corresponding transitioned "over" record are not transitioned.
- Values not noted in the crosswalk result in null values.

These are scope and structural assumptions, not merely code substitutions. They matter when comparing counts, feature relationships, and historical inventory structure.

## Examples of item-level transition treatment

The following examples are drawn from the public FHWA crosswalk. They are not a complete item audit.

| SNBI item | Tag | Legacy source / transition treatment | Crosswalk class | Model implication |
|---|---|---|---|---|
| Bridge Number | BID01 | Item 8; trim spaces; zero handling requires user choice | Yes | Preserve original ID and normalization choice |
| Previous Bridge Number | BID03 | NBI structure-number-change history | Yes | Preserve raw source and lineage provenance |
| Border Bridge Inspection Responsibility | BL09 | Legacy Item 98B is funding responsibility; transition assumes funding and inspection responsibility are the same | Partial | Do not treat as verified inspection responsibility |
| Border Bridge Designated Lead State | BL10 | Both bordering states designated as lead during transition | Yes, with later update required | Preserve transition assumption |
| Span Configuration | BSP01 | Items 43/44 partially populate span configurations; multiple configurations and culvert extension/widening cannot be fully transitioned | Partial | Avoid assuming full span topology from legacy data |
| Number of Spans | BSP02 | Items 45/46 populate main/approach configurations; limits apply | Partial | Preserve source configuration and completeness |
| Functional Classification | BH01 | Item 26; temporary codes may be used | Partial | Retain temporary-code status and do not treat as final classification |
| Urban Code | BH02 | Item 26; assigned to all highway features; temporary codes may be used | Partial | Transition assumptions affect feature-level attribution |
| NHS Designation | BH03 | Item 104; assigned to H01 feature | Yes | Preserve feature assignment context |
| National Highway Freight Network | BH04 | Item 110; temporary codes may be used | Partial | Treat temporary code separately from permanent designation |
| Load Posting Status | BPS01 | Item 41; partial transition and temporary codes | Partial | Do not assume full equivalence to legacy status |
| Calculated Deck Area | BG16 | Calculated from legacy dimensions during transition | Calculate | Retain source dimensions and formula/version |
| Highway Average Daily Truck Traffic | BH10 | Legacy Item 109 percentage multiplied by Item 29 traffic | Yes | Derived value; preserve both inputs and calculation |
| Year Work Performed | BW02 | Item 106 Year Reconstructed, direct if greater than zero | Yes | Do not assume all preservation work is captured |
| Work Performed | BW03 | "RECONSTRUCTED" assigned when Item 106 > 0; note says this is not an SNBI code for this item | Partial | Treat as a transition-generated descriptor, not a verified work taxonomy |

## Distinguish transition class from actual verification

The FHWA implementation memorandum says that during the first inspection cycle after transition, agencies should verify that data items transitioned correctly for each bridge, update incorrect values and temporary codes, and populate missing/new items. It further states that all transitioned data should be verified and corrected if necessary before the March 2028 submittal.

The FHWA Q&A defines verified data as transitioned data validated by inspection or review. The crosswalk class and the actual verification status are therefore different dimensions:

1. **Transition class:** How safely can the legacy item be mapped to the SNBI item?
2. **Record-level verification status:** Has this bridge's value actually been validated by inspection or review?
3. **Value status:** Is the current value permanent, temporary, null, calculated, or otherwise incomplete?
4. **Observation vintage:** When was the underlying inspection, measurement, or administrative value actually observed?

Do not collapse these into one status flag.

## Recommended model metadata

Add a versioned item-level transition metadata table with:
- `snbi_item_id`
- `data_tag`
- `legacy_item_id`
- `transition_class` (CLEAN, PARTIAL, NO_TRANSITION, CALCULATED)
- `transition_rule_summary`
- `transition_assumption_flag`
- `temporary_code_possible`
- `null_expected_from_transition`
- `source_crosswalk_version`
- `effective_submission_year_start`
- `effective_submission_year_end`
- `verification_requirement`
- `record_level_verification_status` (unknown unless sourced)
- `record_level_verification_date` (null unless sourced)

For each observation, retain:
- raw legacy value and raw SNBI value where available;
- original source record and source file;
- transformed value and transformation version;
- transition class copied from the applicable crosswalk version;
- explicit record-level verification evidence, if present;
- unresolved status where evidence is absent.

## Consequences for longitudinal analysis

A clean transition is not proof of physical comparability or record-level verification. It only indicates that the crosswalk provides a direct mapping to permanent SNBI codes. Even clean transitions may involve unit conversions, field assignment to a particular feature, or other documented transformation.

Partial transitions should be excluded from unqualified trend comparisons until their temporary codes and assumptions are resolved or separately modeled.

Non-transitioned items should not be backfilled with invented historical values. A new SNBI item may have no legacy equivalent; its historical series begins only when actual collection or other authoritative source data exists.

Calculated items should be recomputed only from preserved source inputs and a versioned formula. Keep FHWA's calculated value separate from any model-specific recalculation.

## Sources

1. FHWA, *Data Crosswalk for "Over" Records and "Under" Records*, including general transition notes, field mappings, and transition classifications: https://www.fhwa.dot.gov/bridge/snbi/datacrosswalk.cfm
2. FHWA, *Questions and Answers on the Specification for the National Bridge Inventory*, Topic T: Transitioning Data: https://www.fhwa.dot.gov/bridge/snbi/qanda/03.cfm
3. FHWA, *Memorandum – Implementation of the Specifications for the National Bridge Inventory*, especially transition timeline and agency verification expectations: https://www.fhwa.dot.gov/bridge/pubs/Memo-Implementation_Specifications_National_Bridge_Inventory_FINAL.pdf

## Evidence classification

- **Source-reported:** Crosswalk transition classes and documented assumptions.
- **Source-reported:** Agencies are expected to verify transitioned values and resolve temporary codes before March 2028.
- **Derived:** Crosswalk class can support field-level transition-risk metadata but cannot establish the verification history of a particular bridge value.
- **Model recommendation:** Keep transition class, record-level verification, value status, and observation vintage as separate dimensions.
- **Unknown:** Whether public 2026 download files provide an authoritative record-level flag or history for actual verification.
