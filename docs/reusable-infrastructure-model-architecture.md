# Reusable Infrastructure Model Research and Data Architecture

**Status:** Shared architecture proposal derived from the bridge-model research process.  
**Date:** 2026-11-26  
**Purpose:** Reuse validated data-governance, ingestion, identity, measurement, and forecasting practices across infrastructure sectors without forcing different physical systems into one inappropriate schema.

## 1. Design principle

Build one reusable research and data-engineering foundation, with separate sector-specific models on top.

The shared foundation should standardize:
- source registration and provenance;
- immutable raw-data retention;
- versioned parsing and normalization;
- entity identity and lineage;
- time-aware observations and events;
- missingness and data-quality classification;
- measurement-definition versioning;
- validation and reconciliation;
- uncertainty and forecast governance;
- model-run reproducibility.

It should **not** force bridges, electric assets, water systems, roads, ports, pipelines, or workforce datasets into identical physical-condition variables. Shared architecture; sector-specific semantics.

## 2. Four-layer data architecture

### Layer 1 — Source archive (immutable)

Store each acquired source file or API response as received.

Required metadata:
- source ID and publisher;
- source URL or API endpoint;
- retrieval timestamp;
- publication/release date where available;
- reporting period or observation period;
- geographic and organizational scope;
- file format and declared schema/version;
- byte count and cryptographic checksum;
- license/access restrictions;
- acquisition method and retrieval status.

Never overwrite a prior source vintage. A corrected release becomes a new source artifact linked to the prior version.

### Layer 2 — Raw parsed records

Parse source artifacts while preserving original field names, values, types, record boundaries, nested structures, and source location.

For every raw record, retain:
- source artifact ID;
- source record key, if supplied;
- source row/object ordinal;
- original field/tag;
- original raw value;
- parser version;
- parse status and error details.

Do not normalize away leading zeroes, whitespace, date formats, precision, code suffixes, or nested relationships before retaining the original value.

### Layer 3 — Normalized observations and events

Map raw source items into canonical, sector-specific observations using versioned mapping rules.

A normalized observation should distinguish:
- entity ID;
- attribute/measure ID;
- value and unit;
- observation time or interval;
- publication/reporting vintage;
- source artifact and raw record;
- transformation rule/version;
- transition or mapping classification;
- verification status, if explicitly documented;
- missingness/value-status reason;
- quality/confidence metadata.

Events should be separate from observations. Examples include inspection, repair, replacement, retirement, outage, break, treatment, construction start, commissioning, closure, funding award, and ownership transfer. Event types and required attributes remain sector-specific.

### Layer 4 — Derived analytical data and model outputs

Derived values must be reproducible from retained raw and normalized inputs plus versioned transformations.

Each model run should record:
- code commit/version;
- data snapshot/source vintages;
- parameter set;
- assumptions/scenario;
- feature definitions;
- training/calibration period;
- validation method and results;
- run timestamp;
- output schema/version;
- uncertainty representation.

Do not overwrite historical model runs when new data arrives. Preserve forecast vintages so forecast accuracy can be assessed later.

## 3. Shared entity identity and lineage

A single identifier is rarely sufficient across long histories and multiple source systems.

Use a canonical internal entity ID with versioned source identifiers and explicit identity links:
- source system and source identifier;
- identifier validity period;
- canonical entity ID;
- predecessor/successor entity IDs;
- relationship type;
- matching method;
- match confidence;
- evidence source;
- reviewer/decision status where applicable.

Keep these concepts separate:
- physical asset identity;
- reporting record identity;
- administrative/jurisdiction identity;
- network or service relationship.

A renumbering or jurisdiction transfer is not automatically a physical asset addition or removal. A replacement may represent an old asset's retirement and a new asset's commissioning. Sector-specific lineage rules must define partial replacement, mergers, splits, and network reconfiguration.

## 4. Time is multidimensional

Do not use one generic `year` field.

Where applicable, retain:
- observation/event date;
- effective date or interval;
- reporting period;
- submission year;
- publication/release date;
- retrieval date;
- source vintage;
- model-run date.

An annual file may contain observations made on different dates. A reporting-year change does not prove that the physical asset changed during that year.

## 5. Missingness, transition, and verification

Missing values should carry reasons where the source supports them. A shared missingness vocabulary can include:
- PRESENT;
- SOURCE_NULL;
- BLANK;
- NOT_REPORTED;
- NOT_APPLICABLE;
- NOT_COLLECTED;
- NOT_TRANSITIONED;
- TEMPORARY_CODE;
- INVALID_SOURCE_VALUE;
- UNKNOWN_REASON.

Do not infer a reason when the source does not provide one.

For datasets that change definitions or schemas, keep at least four independent dimensions:
1. **Mapping/transition class:** clean, partial, no transition, calculated, or sector-specific equivalent.
2. **Record-level verification:** verified, not verified, or unknown, based only on evidence.
3. **Value status:** permanent, temporary, missing, calculated, invalid, or other source-defined status.
4. **Observation vintage:** when the underlying information was observed.

These dimensions must not be collapsed into a single data-quality score.

## 6. Measurement definitions and versioning

Every analytical measure needs a definition record:
- measure ID and name;
- conceptual definition;
- unit and scale;
- numerator/denominator where relevant;
- inclusion/exclusion rules;
- geographic and asset scope;
- weighting method;
- aggregation method;
- missing-data treatment;
- source item mappings;
- effective dates;
- formula/code version;
- authoritative source and evidence status.

When a publisher changes a definition, create a new version and test whether old and new values are comparable. Do not splice a new measure into an old series merely because the label is unchanged.

Keep raw components available so alternative definitions can be reproduced and sensitivity-tested.

## 7. Validation and reconciliation layers

Apply validation in stages:
1. **File/transport:** checksum, byte count, encoding, decompression, completeness.
2. **Structural:** schema version, required fields, record/object structure, nested arrays.
3. **Type/domain:** data types, units, allowed values, ranges, code lists.
4. **Conditional:** rules that depend on other fields or asset types.
5. **Referential:** parent-child links, cross-record references, entity identity.
6. **Quantitative:** sums, totals, ratios, dimensional consistency, stock-flow balances.
7. **Temporal:** date order, elapsed time, impossible overlaps, reporting-vintage consistency.
8. **Aggregate reproduction:** reproduce publisher totals before building forecasts.
9. **Longitudinal continuity:** explain additions, removals, reclassifications, source changes, and unexplained residuals.

Passing validation means a record is internally consistent under a rule set; it does not prove that the underlying physical-world measurement is correct.

## 8. Stock-flow accounting

For countable physical asset populations, use an explicit balance:

`Closing stock = Opening stock + Entries - Exits + Scope/measurement adjustments`

Keep physical entries/exits distinct from:
- reporting-rule changes;
- jurisdiction transfers;
- identifier changes;
- duplicate corrections;
- asset boundary changes;
- measurement corrections.

For non-countable systems, define an appropriate sector-specific conservation or balance identity rather than forcing this equation onto inappropriate data.

Unexplained residuals should remain visible and be investigated; do not distribute them across events without evidence.

## 9. Sector-specific model modules

The shared platform should support, but not merge, sector-specific domains.

| Sector | Examples of sector-specific entities and measures |
|---|---|
| Bridges | Bridge assets, spans, elements, inspections, condition ratings, load restrictions, scour, deck area |
| Electric grid | Generators, substations, transformers, transmission/distribution circuits, capacity, loading, outage events, interconnection queues |
| Water/wastewater | Treatment plants, wells, pipes, pumps, storage, capacity, leakage, compliance, service interruptions |
| Roads/highways | Road segments, pavement condition, lane-miles, traffic, closures, functional class, maintenance |
| Workforce | Occupations, employers, contractors, licenses, retirements, training pipelines, vacancies, geographic labor pools |
| Finance/materials | Funding stages, project costs, procurement, commodity inputs, delivery lead times, supplier concentration |

A shared workforce model may connect sectors, but must define primary, adjacent, and supporting workforce populations separately to avoid double counting.

## 10. Forecasting and model governance

Keep descriptive measurement separate from predictive inference.

Before publishing a forecast:
- reproduce source aggregates;
- establish a defensible historical series;
- identify structural breaks and data discontinuities;
- define target variables and forecast horizons;
- separate observed data from assumptions and scenarios;
- test against held-out periods and, where possible, independent evidence;
- compare against simple baselines;
- quantify uncertainty and sensitivity;
- document failure modes and known blind spots.

Do not assign deterioration, failure, replacement, workforce-retirement, or funding-response coefficients without evidence or an explicitly labeled scenario assumption.

A composite infrastructure stress score should not hide its components. Publish component measures, weights, normalization, missing-data treatment, and uncertainty. If weights are not empirically validated, label them as a transparent scenario or decision framework, not an objective physical fact.

## 11. What the bridge work has already contributed

The bridge research has exposed reusable issues:
- historical record formats can change without physical assets changing;
- record identifiers may not be immutable physical-asset identifiers;
- annual submission files are not necessarily annual observations;
- transition crosswalks carry assumptions and partial mappings;
- temporary codes and missing values require field-specific rules;
- calculated measures can change formula across reporting eras;
- aggregate counts and areas can disagree across official sources;
- condition, safety, service importance, network consequence, finance, and workforce are distinct dimensions;
- funding obligations are not proof of completed physical work;
- a parser must be versioned and tested before production use.

These are now design requirements for other sector models, not merely bridge-specific lessons.

## 12. Implementation sequence

1. Preserve the current repository's research charter and bridge specification.
2. Define shared source registry, raw record, observation, event, identity-link, definition-version, validation-result, and model-run schemas.
3. Build and test shared utilities only after representative sector source formats are acquired.
4. Keep bridge-specific parsing and normalization separate from common infrastructure.
5. Apply the shared framework to the electrical-grid model as the next candidate, reusing the existing grid research rather than restarting it.
6. Apply the same audit method to water/wastewater and roads.
7. Integrate sector outputs only after units, scope, time, uncertainty, and workforce definitions are reconciled.

## 13. Explicit non-goals

- No claim that every sector can use the same physical-condition scale.
- No automatic conversion of all data into a single 0–100 score.
- No assumption that correlation establishes causation.
- No hidden imputation of missing observations.
- No publication to The Foundry without explicit approval.
- No production parser based only on a webpage summary or partial record excerpt.

## Evidence classification

- **Derived from bridge research:** The reusable data-governance and validation requirements.
- **Architecture recommendation:** The four-layer data model and shared metadata schemas.
- **Sector-specific work outstanding:** Actual schemas, definitions, sources, and validation rules for each non-bridge sector.
- **User decision required later:** Shared implementation priorities, forecast horizons, integrated stress-score design, and publication boundaries.
