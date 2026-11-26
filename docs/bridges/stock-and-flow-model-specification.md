# Bridge Inventory Stock-and-Flow Model — Specification v0.1

**Status:** Structural specification; not calibrated and not approved for publication.  
**Date:** 2026-11-26  
**Scope:** Public-road bridge inventory, national and state levels, with bridge-level records where available.  
**Purpose:** Define the accounting system and model interfaces before estimating deterioration, treatment, or replacement parameters.

## 1. Design principles

The bridge model is an asset-accounting and condition-transition system. It must explain separately:

- how many physical bridge assets are in the inventory;
- how much bridge deck area is represented;
- how condition changes over time;
- which assets enter or leave the inventory;
- which interventions occur and what evidence exists about their effects;
- how safety, load capacity, network importance, exposure, workforce, materials, and finance affect risk and consequences.

Do not collapse these into one variable. A bridge count, deck area, condition rating, load restriction, network consequence, and funding amount measure different things.

The model is designed to support national and state reporting. Bridge-level records are the preferred analytical unit; state/year aggregates are validation and reporting outputs, not substitutes for asset histories.

## 2. Asset identity and observation model

Maintain two identifiers:

1. **Record identifier:** the exact jurisdiction/year structure number and source record key as submitted.
2. **Physical asset identifier:** a stable internal ID representing the best-supported identity of the physical bridge through time.

Never overwrite the raw identifier. Store a versioned crosswalk with predecessor/successor IDs, matching method, source, confidence, and adjudication status. A renumbering is not automatically a new bridge. A replacement is a physical asset event, even if the route and general location remain the same.

Each annual observation must also retain:
- reporting jurisdiction and owner;
- source dataset, vintage, retrieval date, file checksum, and record-layout version;
- inclusion/filter decision and reason;
- observation/submittal year and actual inspection date where available;
- raw values, normalized values, missingness, and validation flags.

NBI annual files are annual submissions and may be corrected during the year; FHWA identifies June 15 as the final public-highway-bridge data publication point for the annual vintage. Preserve the chosen vintage rather than silently replacing it with a later revision.

## 3. Core stocks

For each year t, jurisdiction j, and (where useful) bridge class g, maintain:

### 3.1 Physical inventory stock

- N(j,t): number of in-scope physical bridge assets.
- A(j,t): total in-scope deck area, in a consistent area unit.
- Optional stratifications: owner, highway system, functional class, rural/urban, age cohort, material, design type, climate/exposure class, and traffic class.

Count and area are parallel measures. Do not use one as a proxy for the other. A small rural bridge and a large interchange each count as one asset but contribute very different area and network consequences.

### 3.2 Condition stocks

Maintain bridge counts and deck area separately in each condition class:

- G(j,t): Good
- F(j,t): Fair
- P(j,t): Poor
- U(j,t): Unknown / not classifiable under the selected rule

For each class, keep both number of bridges and deck area. Retain component ratings (deck, superstructure, substructure, culvert) separately when available. The bridge-level summary condition is a derived classification under the applicable year-specific rule, not a replacement for the component data.

Pre-2018 Structurally Deficient and post-2018 Poor are not automatically interchangeable. The definition and coding regime must be versioned. Likewise, preserve the calculation procedure and area denominator used for NHS performance measures.

### 3.3 Other states that must not be conflated with condition

Keep separate dimensions for:
- inspection status and elapsed time since inspection;
- load posting/restriction and operating/inventory ratings;
- scour status/vulnerability;
- functional adequacy and geometric constraints;
- closure status;
- network criticality, detour consequence, traffic exposure;
- intervention history;
- data completeness and confidence.

A bridge can be in Fair condition and still have a serious load or scour concern. A Poor bridge is not, by that label alone, a quantified probability of failure.

## 4. Inventory stock-flow accounting

At the physical-asset level:

N(t+1) = N(t) + E(t) - X(t)

Where:
- E(t): new physical bridge assets entering the in-scope inventory during the interval;
- X(t): physical bridge assets leaving the in-scope inventory during the interval.

At the deck-area level:

A(t+1) = A(t) + A_E(t) - A_X(t) + A_M(t)

Where:
- A_E(t): deck area entering with new assets;
- A_X(t): deck area removed with retired assets;
- A_M(t): net area change on continuing assets due to widening, extension, geometry changes, or corrected measurement.

The last term must be decomposed into actual physical modification and data correction wherever possible. A revised area measurement is not construction.

### 4.1 Event taxonomy

Each apparent inventory change must be assigned one of the following event classes, with confidence:

- New construction / new route crossing;
- Physical replacement (old asset retired, new asset commissioned);
- Removal / permanent closure without replacement;
- Transfer into or out of reporting scope;
- Jurisdiction or ownership transfer;
- Bridge definition / reporting rule change;
- Structure-number change / administrative renumbering;
- Record correction, duplicate removal, or data-quality correction;
- Unresolved.

A physical replacement is normally recorded as one exit and one entry, not as a condition improvement to the old asset. A jurisdiction transfer is not a national addition or removal. A reporting-scope change is not a physical asset event.

### 4.2 Accounting checks

For each jurisdiction/year:
- reconcile beginning stock + entries - exits to ending stock;
- reconcile count and deck-area balances independently;
- show unresolved and scope-change counts separately;
- compare bridge-level event totals with published aggregate totals;
- never force the residual to zero by assigning unexplained differences to construction or removals.

If the record history cannot explain the aggregate change, retain an explicit reconciliation residual.

## 5. Condition transition model

For a bridge observed in class i at t, estimate the probability of class j at t+1:

P(C(t+1)=j | C(t)=i, X(t), H(t), Z(t))

Where:
- C is the versioned condition class;
- X contains bridge attributes (age, material, design, size, traffic, environment, owner, etc.);
- H contains inspection history and elapsed time;
- Z contains intervention history and exposure variables.

The transition matrix is not assumed to be constant across all bridges or all years. It may vary by asset class, exposure, age, and treatment history, subject to sufficient evidence.

Condition classes are ordinal/categorical. Do not treat a one-point rating change as a fixed physical increment, and do not average component ratings without a justified rule.

### 5.1 Minimum transition accounting

For each year and class, report:
- remained in class;
- improved one or more classes;
- deteriorated one or more classes;
- became unclassifiable;
- entered the observed sample;
- left the observed sample;
- was retired/replaced;
- unresolved identity or classification.

A bridge absent in the next annual file is not automatically deteriorated, demolished, or replaced. First check reporting scope, identifier history, missingness, and submission status.

### 5.2 Inspection timing and observation uncertainty

Annual NBI snapshots are not annual inspections. Store actual inspection dates and inspection types where available. Transition intervals must use elapsed time, not assume exactly one year between physical inspections.

The observed rating is a measurement made during inspection. It may contain inspector and coding variability. Model the latent physical condition separately from the observed rating only if the available evidence supports such a measurement model. Otherwise, report observed transitions with an uncertainty caveat rather than pretending the latent condition is known.

## 6. Intervention model

Use distinct intervention classes:

### 6.1 Preservation / preventive maintenance

FHWA defines bridge preservation as actions that prevent, delay, or reduce deterioration, restore function, keep bridges in good or fair condition, and extend service life. It may be cyclical or condition-driven.

Model preservation initially as an event/exposure that may alter future deterioration risk or service-life distribution. Do not automatically assign an immediate improvement in the NBI condition class. The intervention may protect an element without changing the bridge-level worst-component rating.

### 6.2 Rehabilitation

FHWA describes rehabilitation as major work to restore structural integrity and correct major safety defects; examples include partial or complete deck replacement, superstructure replacement, and substructure/culvert strengthening or replacement.

Record rehabilitation scope by component/element, project dates, cost basis, and completion status. Condition uplift, capacity change, and service-life extension must be estimated from observed post-project histories, not assigned as universal constants.

### 6.3 Replacement

FHWA defines replacement as total replacement of a bridge with a new facility in the same general traffic corridor. Represent replacement as retirement of the old physical asset and commissioning of a new asset with a linked predecessor/successor relationship.

The new asset receives its own construction year, material/design attributes, geometry, deck area, and baseline condition record. Do not carry the old asset's age or condition history forward as though it were the same physical structure.

### 6.4 Routine maintenance and project evidence

Separate routine maintenance, preservation, rehabilitation, and replacement. Also distinguish:
- planned;
- funded/allocated;
- obligated;
- awarded;
- construction started;
- completed;
- verified on the bridge record.

A funding obligation is not proof that a bridge received a completed intervention. Intervention-effect estimation requires a defensible link to the actual asset and completion date.

## 7. Risk, consequence, and prioritization modules

Do not blend these into condition transitions until the relationships are evidenced.

Maintain separate modules for:
- **Condition/deterioration:** observed and forecast physical condition.
- **Safety/structural risk:** reliability, load capacity, scour and other hazard-specific indicators.
- **Service importance:** traffic volume, freight role, emergency access, network centrality.
- **Consequence:** detour length, alternate-route capacity, isolation effects, economic/social disruption.
- **Exposure:** climate, flood, salt, corrosion, seismic and other relevant hazards.
- **Delivery capacity:** workforce, engineering capacity, contractor availability, materials and equipment.
- **Finance:** needs, programmed funding, obligations, outlays, project costs and price basis.

A later composite stress index may combine validated dimensions with transparent weights. Until then, publish the dimensions separately.

## 8. Data architecture and minimum tables

Recommended logical tables (physical implementation may differ):

1. `bridge_asset`: stable internal physical asset ID and long-lived attributes.
2. `bridge_record_observation`: one row per source record per vintage; raw and normalized fields.
3. `bridge_identity_link`: old/new IDs, link type, method, confidence, provenance.
4. `bridge_condition_observation`: component ratings, summary class, rule version, observation date.
5. `bridge_inspection_event`: actual inspection dates, type, scope, inspector/program fields if available.
6. `bridge_intervention_event`: treatment type, components, project identifiers, dates, status, costs and source.
7. `bridge_inventory_event`: additions, removals, replacement, transfer, scope and correction events.
8. `bridge_network_context`: traffic, routes, detours, criticality and network relationships.
9. `bridge_exposure_context`: climate, scour/flood, corrosion and other hazards with source/vintage.
10. `bridge_model_output`: forecasts, scenarios, parameter versions, uncertainty and run metadata.

Every derived field must retain source fields and transformation version. Do not overwrite raw observations with cleaned values.

## 9. Calibration and validation sequence

No deterioration or treatment coefficient is assigned in this specification.

Recommended order:

1. Reproduce official annual inventory and condition totals from source files, including scope filters and geographic coverage.
2. Build the record-to-physical-asset identity crosswalk and quantify match confidence.
3. Reconcile additions, removals, transfers, replacements, and unresolved stock-flow residuals.
4. Build observed bridge-level condition transition cohorts with actual elapsed time and stable identity.
5. Stratify by material, design, age, climate/exposure, traffic, owner, and inspection interval where sample size permits.
6. Link completed interventions to assets and compare post-treatment trajectories with defensible comparison groups.
7. Estimate candidate transition models; test out-of-sample performance across years and states.
8. Calibrate uncertainty and sensitivity; retain a baseline without treatment effects as a comparator.
9. Only after validation, expose forecasts and stress scores in the national/state dashboard.

Do not infer treatment causality from a simple before/after rating change. Treatment selection is not random: agencies often intervene on bridges already deteriorating or at higher risk.

## 10. Forecast outputs

Minimum outputs by state and nationally:
- inventory count and deck area;
- Good/Fair/Poor/Unknown count and area;
- annual entries, exits, replacements, transfers and unresolved residual;
- observed and forecast transition matrices;
- age/material/design cohort distribution;
- intervention counts by class and completion status;
- load posting/closure/scour indicators as separate dimensions;
- forecast ranges and scenario assumptions;
- data coverage, identity-match confidence and model uncertainty.

Forecast horizons should be configurable. A long-range scenario must show uncertainty widening over time and must not present point estimates as certainties.

## 11. Known limitations and unresolved research

- NBI is an annual submitted inventory, not a complete project-level intervention ledger.
- NBI condition ratings are discrete and do not provide full element-level deterioration mechanisms or quantified damage extent.
- Identifier continuity requires explicit reconciliation; raw structure number alone is not a guaranteed stable physical-asset key.
- Historical coding and classification changes must be versioned.
- Minnesota 2008–2009 inventory discontinuity remains unresolved.
- State-level intervention linkage and project completion evidence remain to be assessed.
- Deterioration and treatment parameters remain unestimated pending suitable longitudinal data.

## 12. Official reference sources

- FHWA, NBI Download Data Files and annual submission/vintage notes: https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm
- FHWA, NBI ASCII archives, 2018 Poor-condition definition change and archive notes: https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm
- FHWA, Bridge Preservation Guide (preservation definition and action hierarchy): https://www.fhwa.dot.gov/bridge/preservation/guide/guide.pdf
- FHWA, Bridge Replacement and Rehabilitation definitions under 23 CFR 650.405: https://www.fhwa.dot.gov/bridge/brr/20210119.cfm
- FHWA, Bridge Management overview: https://www.fhwa.dot.gov/bridge/management/index.cfm
- FHWA InfoBridge update notes (latest-year NBI structure number and historical identity association): https://infobridge.fhwa.dot.gov/Page/infobridge_update_notes
- FHWA, Tables of Frequently Requested NBI Information: https://www.fhwa.dot.gov/bridge/britab.cfm

## 13. Decisions required before implementation

This specification intentionally leaves the following choices open for user approval:
- exact in-scope bridge definition and treatment of border/interstate/agency-owned structures;
- whether the first operational model runs at bridge level, state aggregate level, or both;
- preferred forecast horizons;
- how to handle unknown condition and incomplete component ratings in the headline outputs;
- whether and how to create a composite infrastructure stress score from separate modules;
- acceptable identity-match confidence threshold for inclusion in transition calibration.

**Publication status:** Internal technical specification only. Not approved for publication.
