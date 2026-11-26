# Data directory

This directory is reserved for model datasets. Keep source data, intermediate transformations, and analysis-ready outputs separate.

- `raw/` — original source extracts or immutable snapshots, where permitted.
- `interim/` — cleaned and standardized intermediate files.
- `processed/` — model-ready tables.

Do not commit credentials, restricted data, or large files without first agreeing on a storage strategy. Document provenance for every dataset in `docs/data-governance.md` and a future data catalog.
