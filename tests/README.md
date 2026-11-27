# Tests

The repository uses Python's standard-library `unittest` for its initial test suite so that the first data-governance tests do not require third-party dependencies.

Run from the repository root after making `src` importable:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Bridge longitudinal tests use explicitly synthetic fixtures. They test identity preservation, event deduplication, condition-state semantics, observation/inspection association, element quantity reconciliation, and training-cohort admission gates. They are not empirical bridge data and do not calibrate a deterioration model.

Do not treat a passing synthetic suite as validation against FHWA production files. Real-data integration tests remain gated on acquiring and inspecting representative official NBI/SNBI exports.
