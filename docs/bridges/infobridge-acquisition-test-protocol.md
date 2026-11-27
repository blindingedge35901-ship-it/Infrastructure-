# InfoBridge acquisition test protocol and portal capability clarification

**Status:** Protocol prepared; interactive export not yet executed.  
**Related audit:** `infobridge-longitudinal-data-and-condition-validation-audit.md`

## 1. Important portal distinction

The live InfoBridge pages distinguish between two different functions:

### Historical record export
The Data/Selected Bridges export interface provides:
- Latest Year
- All Years
- Year Range

The portal says exported records are based on selected data attributes. It also warns that historical NBI Item 8 Structure Number values may include previous numbers and provides a Latest Year NBI Structure Number column to help associate records.

The Data page says All Submittals filters records submitted on or after 1993. The public page warns that a bridge may have multiple NBI submittals in one year.

### Performance History and transition analytics
The Performance History page exposes aggregate historic performance and bridge/component condition transition tables. However, the page explicitly states that Performance History is based on the 2025 NBI data selection and is unavailable when the All Data option is selected.

**Consequence:** Do not treat InfoBridge's transition dashboard as an all-submittals bridge-level longitudinal extract. Use it as a separate aggregate/selected-cohort analytical feature, with its data-selection restrictions recorded. The All Years/Year Range record export is the candidate route for row-level historical data.

## 2. Controlled extraction protocol

### Phase A — establish a reproducible bridge sample
Choose a small sample from a single state, initially Colorado, with selection criteria recorded. The sample should include:
- several bridges with multiple NBI vintages;
- at least one bridge with an apparent structure-number change, if discoverable;
- at least one bridge with multiple submittals in a year, if discoverable;
- varied bridge types/materials and age ranges.

Do not assume a sample bridge has these properties until the exported records demonstrate them.

### Phase B — export minimal fields first
Use All Submittals for bridge selection, then choose All Years (or a bounded Year Range) for the record export. Begin with a small attribute set to stay below the portal's export limit.

Candidate fields:
- state code/name;
- NBI structure number;
- InfoBridge latest-year NBI structure number;
- county and location;
- year built and year reconstructed;
- owner and functional/service classification;
- structure type/material/design;
- structure length and width/deck area where available;
- deck, superstructure, substructure, and culvert condition ratings;
- scour/channel condition fields where available;
- inspection date and inspection frequency;
- bridge status/closure/load posting fields where available.

Do not assume every field exists in every vintage. Preserve absent fields and missingness distinctly.

### Phase C — separate historical graph output
For the same sample, save the Historical Condition Rating Graph CSV where available. Record:
- bridge selection;
- current data selection;
- export date;
- displayed years;
- graph component/measure;
- whether the graph is count, percentage, or deck-area weighted.

Do not use Performance History transition tables as a substitute for All Years record export. If used for a separate comparison, keep the 2025 dataset selection and dashboard scope explicit.

### Phase D — validation checks
For every export:
1. Preserve the raw CSV exactly as received.
2. Record portal page, filters, selected fields, year option, export date, and file checksum.
3. Count rows and distinct original structure numbers.
4. Count distinct latest-year structure numbers.
5. Identify bridge-years with multiple rows/submittals.
6. Compare source inspection dates with NBI vintage; calculate lag only where both are valid.
7. Detect structure-number changes without merging automatically.
8. Check condition values against the applicable year-specific code system.
9. Identify gaps and duplicate observations without deleting them.
10. Compare selected graph values to the corresponding record export only where the graph's definition and vintage match exactly.

### Phase E — go/no-go criteria
Proceed to a larger state-level export only if:
- the portal export can be repeated with the same filters and yields explainable row counts;
- all-years semantics and duplicate-submittal behavior are understood;
- original and latest-year structure-number columns are retained;
- inspection dates can be distinguished from submission vintage;
- condition fields can be interpreted under the correct historical coding regime;
- export limits and coverage are documented.

If export is truncated, filtered unexpectedly, or cannot be reproduced, do not scale it. Use the official annual NBI archives as the primary source and InfoBridge as a supplementary bridge-selection/history interface.

## 3. Current verified page behavior

- InfoBridge Data page: https://infobridge.fhwa.dot.gov/Data
- InfoBridge Performance History page: https://infobridge.fhwa.dot.gov/PerformanceDashboard
- InfoBridge Update Notes: https://infobridge.fhwa.dot.gov/Page/infobridge_update_notes

The live Data page describes filtering through all records submitted on or after 1993 when All Submittals is selected, and export options for Latest Year, All Years, and Year Range. It also identifies the latest-year structure-number column and warns about multiple NBI submittals in a year.

The live Performance History page explicitly says the historic performance graphs and transition analytics are based on the 2025 NBI data selection and are unavailable when All Data is selected.

## 4. Research limitation

This protocol is based on the public portal's rendered page documentation. It does not claim that a data export has been run, that the portal exposes a stable public API, or that the export contains every historical submittal without selection or coverage limitations. A user-interactive export and direct file inspection remain required before accepting InfoBridge as a production ingestion source.
