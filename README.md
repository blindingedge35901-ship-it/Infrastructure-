# Infrastructure Model

A research and analytical project for assessing infrastructure condition, workforce capacity, demographic pressure, investment needs, and regional resilience across the United States.

## Project status

This repository is being organized as the home for the Infrastructure Model. The initial commit establishes documentation and a predictable project layout; it does **not** yet contain the model implementation or source datasets.

## Model objectives

- Track infrastructure systems and their condition, age, maintenance burden, and investment needs.
- Measure the capacity of the workforce that builds, operates, inspects, maintains, and repairs infrastructure.
- Examine demographic and training pipelines that affect future workforce availability.
- Compare conditions nationally and by state over time.
- Present indicators in a transparent, reproducible way, with clear definitions and source provenance.

## Workforce accounting

The project distinguishes three groups and should not combine them into one workforce total without an explicit reason:

1. **Primary infrastructure workforce** — employees and contractors directly involved in building, operating, inspecting, maintaining, and repairing physical infrastructure and essential control systems.
2. **Adjacent, infrastructure-dependent workforce** — workers who rely on infrastructure to deliver other societal services. Track separately from the primary asset-workforce total.
3. **Supporting workforce** — upstream suppliers and enabling industries. Track separately so dependencies are visible without double-counting.

## Suggested repository layout

- `docs/` — model scope, methodology, assumptions, data dictionary, and decisions.
- `data/` — documented locations for raw, interim, and processed datasets. Do not commit secrets or restricted data.
- `src/infrastructure_model/` — reusable model code.
- `notebooks/` — exploratory analysis and research notebooks.
- `scripts/` — repeatable ingestion, validation, and update jobs.
- `tests/` — automated checks for data quality and model behavior.
- `config/` — non-secret configuration and source registries.

## Working principles

- Preserve source URLs, retrieval dates, units, geographic coverage, and transformation history for every dataset.
- Separate observed data, estimates, assumptions, and model outputs.
- Keep national and state-level calculations reproducible.
- Avoid silently changing historical values or definitions; document revisions.
- Never commit API keys, credentials, personal information, or private datasets.
- Treat forecasts as scenarios with uncertainty, not certainties.

## Getting started

The repository is currently documentation-first. Implementation choices (Python version, dependency manager, database format, dashboard framework, and update orchestration) should be confirmed against the existing model files and workflow before code is added.

See [`docs/model-overview.md`](docs/model-overview.md) for the initial scope and [`docs/data-governance.md`](docs/data-governance.md) for data-handling conventions.
