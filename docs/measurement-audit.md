# Shared Measurement Audit

Use this audit before an indicator enters a sector model or a cross-sector composite. Complete each section for each source series and each material revision.

## 1. Identity and provenance
- Publisher and dataset/table name:
- Exact source URL/API endpoint:
- Retrieval date and source vintage:
- Covered years/date range:
- Geographic coverage and exclusions:
- Unit of observation (asset, component, route, system, jurisdiction, project, worker, dollar, etc.):
- Update frequency and revision policy:

## 2. Definition and scope
- Exact published definition:
- Inclusion and exclusion rules:
- Asset/system boundary:
- Status categories and thresholds:
- Denominator and aggregation method:
- Whether counts, area, length, capacity, value, or population are weighted:
- Changes in definition, collection method, reporting population, or coding over time:

## 3. Data quality
- Missingness and its pattern:
- Duplicates and identifier stability:
- Coverage changes and discontinuities:
- Plausibility/range checks:
- Internal consistency checks:
- Independent validation or audit evidence:
- Known measurement error and uncertainty:

## 4. Comparability
- Are observations comparable across years?
- Are jurisdictions comparable?
- Are asset classes and reporting populations comparable?
- Are nominal values adjusted for inflation where appropriate?
- Are source revisions/backfills available?
- Which years, jurisdictions, or categories must be excluded or separately flagged?

## 5. Model treatment
- Raw variable retained:
- Normalized variable and transformation:
- Missing-data treatment:
- Weighting/aggregation rationale:
- Confidence/quality flag:
- Sensitivity tests required:
- Whether the measure is descriptive, diagnostic, predictive, or a proxy:

## 6. Decision record
- Decision: use / use with qualification / exclude pending resolution:
- Rationale and evidence:
- Remaining unknowns:
- Reviewer and date:
- Model version affected:

## Mandatory rules
1. Preserve source-reported values; never overwrite them with normalized values.
2. Do not treat a changed label as proof that a definition stayed constant, or that a new label is equivalent to an old one.
3. Do not interpret missing records as zero assets, zero risk, or zero activity.
4. Do not infer annual inspections, treatments, spending, or condition changes from annual snapshots unless the underlying event data supports that inference.
5. Keep count-based and exposure-weighted measures separate when they answer different questions.
6. Keep asset condition separate from safety, service importance, network consequence, and failure probability.
7. Record unresolved discrepancies explicitly; do not force totals to reconcile.