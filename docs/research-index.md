# Research Index

This index tracks the infrastructure model workstreams. Status describes documentation/research maturity, not the condition of the real-world infrastructure sector.

| Workstream | Current status | Next research focus |
|---|---|---|
| Bridges | Active research; baseline and measurement issues identified in prior analysis | Complete source-by-source verification, measurement audit, data continuity review, and model specification |
| Electrical grid | Research stream established | Define asset/system boundaries, demand and capacity measures, reliability, generation/transmission/distribution distinctions, workforce and investment data |
| Water and wastewater | Planned / not yet assessed in this repository | Establish system inventory, condition, treatment capacity, compliance, workforce, funding, and service-risk measures |
| Roads and highways | Planned / not yet assessed in this repository | Define roadway asset scope, condition measures, traffic/service exposure, maintenance, workforce, and funding measures |
| Integrated infrastructure model | Existing broader model work to be reconciled, not rebuilt by default | Map existing indicators and code to sector models; document normalization, weighting, missingness, and validation |

## Shared repository conventions
- `docs/`: research governance, model methods, sector findings, and decisions.
- `data/`: data dictionaries and approved datasets; follow `docs/data-governance.md` before adding raw data.
- `src/infrastructure_model/`: reusable model implementation.
- `notebooks/`: exploratory and reproducible analysis.
- `scripts/`: repeatable ingestion, validation, and build tasks.
- `config/`: non-secret configuration and documented parameters.
- `tests/`: automated checks and validation tests.

Do not create parallel directory structures without a demonstrated need. Large source files and datasets belong in managed storage when unsuitable for Git; record their provenance and location without committing restricted content.

## Research status labels
- **Not started:** no substantive work documented.
- **In progress:** active evidence collection or analysis.
- **Measurement audit:** definitions, scope, quality, and comparability under review.
- **Specification:** model structure and variables documented, implementation pending.
- **Implemented:** code exists and is reproducible.
- **Validated:** performance and limitations tested against stated criteria.
- **Publication-ready:** user has approved the specific public-facing material.

A status may be split into evidence, specification, implementation, and validation when a single label would be misleading.