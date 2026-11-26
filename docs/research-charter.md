# Infrastructure Research Charter

## Purpose
Develop a traceable suite of infrastructure models that evaluates asset condition, service capacity, workforce capacity, investment, demographic pressure, supply constraints, and regional resilience. Sector models are developed separately and integrated only after their definitions, data, and limitations are documented.

## Research integrity
Every material statement must be classified as one of:
- **Observed/source-reported:** directly reported by an identified source, with its date, scope, and definition.
- **Calculated/derived:** computed from identified source data using a documented method.
- **Estimated:** an approximation with method and uncertainty stated.
- **Assumption/scenario:** a chosen input or conditional future pathway, not an observed fact.
- **Hypothesis:** a proposition to be tested.
- **Unknown/unresolved:** a gap, ambiguity, or inconsistency not yet resolved.

Do not silently reconcile conflicting source totals, definitions, vintages, or geographic coverage. Preserve the original values and document the discrepancy and any decision to include, exclude, or qualify them.

## Model boundaries
Keep asset condition, operational capacity, safety, service importance, network consequence, workforce, finance, and material constraints analytically distinct until a documented method justifies combining them. Avoid double-counting assets, workers, spending, and events across datasets or sectors.

For workforce accounting, retain the project's three categories:
1. **Primary infrastructure workforce:** employees and contractors directly building, operating, inspecting, maintaining, and repairing physical infrastructure and essential control systems.
2. **Adjacent, infrastructure-dependent workforce:** workers who rely on infrastructure to provide other societal services. Track separately from the primary asset-workforce total.
3. **Supporting workforce:** upstream suppliers and enabling industries. Track separately to avoid double-counting.

## Evidence and reproducibility
For every source, retain publisher, title, exact URL or API endpoint, retrieval date, covered period, geographic scope, units, definitions, revisions, licensing/usage terms, and transformations. Preserve raw values where permitted. Version derived data, code, model specifications, and outputs. Record missingness, exclusions, quality checks, and changes between runs.

Forecasts must be presented as scenarios with explicit assumptions, ranges, sensitivity tests, and limitations. Do not present a model score as a probability of failure or as a substitute for engineering inspection unless independently validated for that purpose.

## Validation
Use historical back-testing where suitable, independent comparison datasets, sensitivity analysis, and documented error analysis. Distinguish data-quality validation from physical-condition validation and predictive validation. A model is not considered validated merely because its calculations are internally consistent.

## Publication boundary
Research, working notes, datasets, and model outputs remain internal during development. Nothing is to be published to The Foundry or another public channel until the user explicitly approves the specific material and its presentation.

## Security and handling
Never commit credentials, API keys, access tokens, passwords, personal data, or source data that cannot legally be redistributed. Keep secrets in approved secret storage or environment variables. Use Dropbox for working source documents and larger files; use GitHub for version-controlled specifications, code, and concise research records. Maintain appropriate backups.

## Decision control
Model assumptions, thresholds, weights, exclusions, and interpretations that materially affect results must be visible and reviewable. Do not silently choose them on the user's behalf. Record the decision, rationale, date, and affected model version.