# Bridge longitudinal utilities

The initial module contains conservative, dependency-free data-governance helpers for bridge identity, inspection-event reconstruction, condition observation handling, element quantity checks, and training-cohort admission.

These utilities do not resolve real-world physical bridge identity automatically, do not infer repairs, and do not estimate deterioration coefficients. All ambiguous links remain explicit. Synthetic unit tests are in `tests/bridges/`.
