# 2026 FHWA Bridge Condition Baseline — published aggregate audit

Date reviewed: 2026-11-26  
FHWA table date: August 4, 2026  
Primary source: https://www.fhwa.dot.gov/bridge/nbi/no10/condition26.cfm

## National all-bridge totals
FHWA's 2026 Bridge Condition by Highway System table reports:

| Measure | Good | Fair | Poor | Total |
|---|---:|---:|---:|---:|
| Bridge count | 268,737 | 315,054 | 41,148 | 624,939 |
| Bridge area (sq ft) | 1,854,647,561 | 2,476,504,198 | 217,000,522 | 4,548,152,281 |

The count categories sum exactly to 624,939. The area categories sum exactly to 4,548,152,281 square feet.

Derived from FHWA published totals:
- Poor bridges by count: 41,148 / 624,939 = approximately 6.58%.
- Poor bridge area: 217,000,522 / 4,548,152,281 = approximately 4.77%.

These are separate measures and should remain separate in model outputs. The count proportion is not a deck-area exposure measure.

## National NHS subset
FHWA reports 147,243 NHS bridges:

| Measure | Good | Fair | Poor | Total |
|---|---:|---:|---:|---:|
| Bridge count | 62,083 | 81,016 | 4,144 | 147,243 |
| Bridge area (sq ft) | 984,291,343 | 1,510,838,933 | 102,912,580 | 2,598,042,855 |

Derived:
- Poor NHS bridges by count: approximately 2.81%.
- Poor NHS bridge area: approximately 3.96%.

Do not mix NHS subset and all-bridge denominators.

## Colorado published baseline
FHWA reports Colorado:
- Total bridges: 9,018
- Good: 2,882
- Fair: 5,736
- Poor: 400
- Total bridge area: 57,468,269 sq ft
- Good area: 20,790,697 sq ft
- Fair area: 34,600,507 sq ft
- Poor area: 2,077,065 sq ft

Derived:
- Poor by count: approximately 4.43%.
- Poor by area: approximately 3.61%.

These are source-reported aggregate results, not independently reproduced from the Colorado JSON file.

## 2026 deck-area definition — important transition rule
FHWA's Tables of Frequently Requested NBI Information definition page says Bridge Deck Area is calculated using SNBI Item BG02 (Total Bridge Length) multiplied by width. During 2026 and 2027 transition:
- If SNBI BG05 Bridge Width is at least 10 feet, use BG05.
- If BG05 is below 10 feet or null, use BG09 Approach Roadway Width.
- Beginning in 2028, use BG05 alone regardless of value.

Source: https://www.fhwa.dot.gov/bridge/britab.cfm

This is a material definition change and must be explicitly versioned in the historical deck-area series. Do not assume 2026 deck-area totals are calculated using the same width fallback as earlier vintages, or that 2028 will preserve the 2026 fallback.

FHWA says the condition classification is the lowest of SNBI BC01 deck, BC02 superstructure, BC03 substructure, or BC04 culvert ratings. Good is lowest rating >=7, Poor <=4, and Fair 5 or 6.

## Comparability caution
The 2025 published condition baseline was 624,193 bridges with 41,685 Poor; the 2026 published baseline is 624,939 bridges with 41,148 Poor. These aggregate differences alone do not demonstrate physical repair, deterioration, or inventory growth. The 2026 release is the first SNBI-era transition dataset, with new schema, transition codes, nulls, and updated bridge-area computation. A valid year-over-year explanation requires record-level identity matching, definition/version controls, and event reconciliation.

## Model ingestion and validation implications
1. Store official annual published aggregate tables as a separate benchmark dataset, with source URL, publication date, measure, geography, system scope, unit, classification procedure, and calculation version.
2. Use these totals as independent acceptance targets when the complete state JSON files are acquired and parsed.
3. Reproduce national totals by summing the state/jurisdiction outputs; identify scope/geography exceptions (e.g., Guam did not submit 2026 data).
4. Reproduce count and area distributions independently.
5. Implement bridge-area calculation as a vintage-aware derived measure, including 2026–27 BG05/BG09 fallback and the 2028 BG05-only rule.
6. Retain component condition ratings separately from derived Good/Fair/Poor class.
7. Keep NHS and all-bridge populations distinct.

## Evidence status
- **Source-reported:** 2026 national, NHS, and Colorado condition counts and areas; classification thresholds; deck-area calculation rule.
- **Calculated:** percentages above and arithmetic checks of totals.
- **Not established:** full raw-record reproduction, causal explanation of 2025–26 changes, or longitudinal asset matching.

Internal research only; not approved for publication.
