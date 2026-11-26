# Data governance and provenance

## Required metadata

For every source dataset, record:

- Dataset name and publisher.
- Source URL or API endpoint (never include credentials).
- Retrieval date and covered date range.
- Geographic level and geographic identifiers.
- Units, definitions, and known revisions.
- License or terms of use, where applicable.
- Refresh frequency and responsible ingestion script.
- Transformations applied and output location.

## Data layers

- `data/raw/`: immutable snapshots of source data when licensing permits.
- `data/interim/`: cleaned or standardized intermediate data.
- `data/processed/`: analysis-ready tables used by the model.

Do not overwrite raw snapshots silently. Use dated/versioned files or a documented storage strategy. Large datasets may belong in external storage rather than Git.

## Quality checks

Check schema, types, units, missingness, duplicates, valid geographic codes, date continuity, and unexpected jumps. Keep validation results with each update run.

## Security and licensing

Never commit API keys, access tokens, passwords, personal data, or data that the project is not permitted to redistribute. Store secrets in environment variables or an approved secret manager. Review source licensing before storing or publishing datasets.
