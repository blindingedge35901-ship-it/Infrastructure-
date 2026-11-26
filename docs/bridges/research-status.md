# Bridge Infrastructure Model — Research Status

**Status:** In progress — baseline and key measurement rules verified against official sources; historical archive continuity, identifier reconciliation, cost estimates, and predictive parameters remain under investigation.

## Model scope
Develop a national and state-level bridge model that distinguishes inventory and physical condition from safety, load capacity, service importance, network consequence, investment, and workforce capacity. Maintain both count-based and exposure-weighted measures where source definitions support them.

## Verified source findings

### 2025 inventory and condition baseline
FHWA's 2025 Bridge Condition by Highway System table is dated June 15, 2025. It reports national counts of 624,193 bridges: 272,779 Good, 309,729 Fair, and 41,685 Poor. Its national bridge-area total is 409,265,353 m², comprising 170,258,454 m² Good, 219,125,109 m² Fair, and 19,881,790 m² Poor. These values are reproduced in the FHWA 2025 Bridge Condition by Owner table and are also reported by CRS using BTS Table 1-28.

**Geographic caveat:** FHWA's 2025 condition-by-highway-system page explicitly says Guam did not submit data for 2025. Some FHWA table headings list all states, DC, Guam, Puerto Rico, and the U.S. Virgin Islands as the possible reporting geography; that heading must not be interpreted as proof of a Guam submission. BTS notes that U.S. totals include Guam from 2018 onward and the U.S. Virgin Islands from 2019 onward, but the actual 2025 FHWA page says Guam did not submit. Record actual submission coverage for each vintage rather than assuming the geographic heading equals the data population.

These are public-road bridge inventory and condition measures as reported in the cited sources. Do not treat a bridge count as a deck-area measure or infer safety/failure probability directly from the Poor category.

### Condition classification and performance measurement
FHWA's archive documentation states that, effective with the 2018 data archive, the term Structurally Deficient was eliminated and Poor condition adopted. The Poor classification is based on any of the deck, superstructure, substructure, or culvert component ratings being coded 4 or less. This is a classification/definition break; do not join pre-2018 Structurally Deficient and post-2018 Poor as if they were automatically identical series.

For the NHS performance measures, FHWA reports two measures: percentage of NHS bridges in Good condition and percentage in Poor condition. Both are expressed as percentages of deck area, not bridge counts. Condition classification uses the lowest applicable component rating; Fair bridges do not enter either Good or Poor target measure. Keep the count distribution (Good/Fair/Poor) and the NHS deck-area-weighted measures as separate outputs.

FHWA's November 3, 2025 computation procedure is important for the SNBI transition. It states that the procedure applies to the 2026 NBI dataset and subsequent years; 2025 and earlier use the April 2018 Coding Guide-based procedure. The first SNBI-based submittal is March 2026. The 2026 and 2027 datasets are transition-period datasets; the 2028 dataset is the first computed under the SNBI-based procedure. In 2026–2027, approach roadway width is used when bridge width out-to-out is not reported for bridge-length culverts. From 2028 onward, if reported, irregular deck area is used instead of length multiplied by out-to-out width.

FHWA's 2025 computation procedure explicitly excludes an NHS bridge record from the performance-measure computation if all four component condition metrics are missing. It also excludes records with no usable bridge width out-to-out and no usable approach roadway width during the transition period. For SNBI-based records, exclusion applies if both irregular deck area and bridge width out-to-out are missing or zero. This exclusion rule affects the denominator and must be documented in any reproduction of FHWA's official measure.

### Inspection intervals and annual archive interpretation
FHWA's current NBI download page says the public highway bridge dataset is finalized and published by June 15 each year, and warns that NBI data should not be used for route-clearance purposes because inspections are generally every 24 months and displayed clearance information may not be current.

The current federal rule for routine inspections is risk-based. Under Method 1, the regular interval is generally no more than 24 months; certain bridges with a component or scour rating of 3 or less must be inspected at intervals no greater than 12 months; qualifying bridges meeting all specified conditions may use intervals no greater than 48 months. The regulation also permits other risk-based Method 2 intervals where approved. Thus, an annual NBI archive row is not evidence that every bridge received an inspection in that calendar year. Use actual inspection dates and elapsed time where available.

### Limits of NBI condition data and inspection variability
FHWA's Long-Term Bridge Performance primer explains that NBI does not provide detailed condition data for the many individual bridge subelements (such as beams, pier columns, and abutments), quantitative extent/location of differing conditions, or underlying causes before surface damage appears. It also notes that condition ratings are discrete integer codes, not continuous measurements suitable for treating each one-point change as an equal physical increment.

FHWA's 2001 visual-inspection reliability study involved 49 inspectors from 25 state agencies performing ten inspection tasks on seven test bridges. It found significant variability: condition ratings varied across as many as five different rating values; the study estimated 68% within one rating point of the average and 95% within two. This is historical evidence from a limited study, not a measured error distribution for today's entire NBI inventory. It supports treating ratings as measurements with uncertainty, not discarding them.

### Data quality oversight
FHWA's April 2026 interim NBIP Metrics document describes the federal oversight process for state bridge inspection programs. It identifies Metric 22 (Inventory — Bridge Data Quality) and Metric 23 (Inventory — Timely Updating of Data). Metric 22's compliance criterion requires at least 95% of sampled NBI data items to be within acceptable tolerances and correctly assigned for full compliance; at least 90% for substantial compliance. Metric 23 requires inspection-related inventory updates within three months after the month of field inspection, and specified updates for bridge modifications/new openings and load restriction/closure status within three months of the relevant event. These are program oversight/compliance metrics, not physical-condition scores and not a guarantee that every individual record is error-free.

## Findings retained as provisional pending direct reproduction
The following were reported in prior research but still require exact archive files, extraction code, and source-vintage reconciliation before being promoted to verified results:

- A CRS 2025 count of 41,685 Poor bridges versus 41,677 Poor bridges in a separate FHWA 2025 replacement-cost table (4,341 NHS plus 37,336 non-NHS), an eight-bridge discrepancy.
- The reported 2025 Poor-bridge replacement-cost estimate of approximately $85.45 billion and rehabilitation estimate of approximately $58.10 billion (using FHWA's 68% rehabilitation factor). These are estimated costs for the Poor inventory represented in the cost table, not a complete national backlog, annual funding need, or project list.
- The reported 2024-to-2025 cost-table comparison: Poor count 42,067 to 41,677; nominal replacement cost approximately $82.23 billion to $85.45 billion; deck area approximately 212.83 million to 214.00 million square feet. Do not interpret nominal cost change as real deterioration or inflation-adjusted backlog growth.
- The 2011–2012 archive subset discrepancy against published FHWA Type 1 totals. Its cause remains unresolved. Exclude affected subsets from national trend fitting until the original archives and published totals are reconciled.
- Potential identifier discontinuities previously noted for Mississippi 1996–1997, Pennsylvania 2010–2011, and Minnesota 2008–2009. Candidate record links are not official crosswalks.
- The reported 1995 Coding Guide transition effects on Item 58 N-code applicability. The exact coding-guide provisions and affected years still need direct comparison before implementing any recode.
- The 2018 archive warning: FHWA recommended re-downloading 2018 files obtained between March 15 and April 16, 2019 because of an error in bridge measurement data. The acquisition date of the previously examined archive copy remains unknown.
- The reported 2024 FHWA preservation roadmap finding that data on post-preservation deterioration, service life, cost, and treatment effectiveness are limited. Verify exact source and passage before assigning treatment coefficients.
- The lack of a complete national bridge-level history connecting all funding stages to specific interventions and subsequent condition. This requires a targeted data availability review before being stated as a definitive national absence.

## Modeling implications
1. Use a stock-and-flow framing for inventory, condition transitions, deterioration, preservation, rehabilitation, replacement, and removals—but estimate transition and treatment parameters only where longitudinal evidence supports them.
2. Maintain parallel bridge-count and deck-area-weighted condition views.
3. Separate condition from safety, load capacity, service importance, detour/network consequence, and exposure.
4. Track inspection date, interval, component completeness, and reporting vintage; do not treat annual snapshots as annual inspections.
5. Treat classification, coding, archive, identifier, and SNBI transitions as explicit discontinuities.
6. Keep allocation, obligation, outlay, award, construction, completion, and verified bridge-level intervention separate.
7. Treat LTBP and other detailed samples as mechanism/validation evidence, not as a national census.
8. Do not invent deterioration or treatment coefficients. Use calibrated estimates only after data suitability and uncertainty are demonstrated.

## Remaining research before model specification
- Reproduce 2025 counts and deck-area totals from the exact archived data files and document filters, geographic coverage, and exclusions.
- Reconcile (or retain as unresolved) the eight-bridge difference between the CRS condition count and FHWA cost-table count.
- Reproduce the 2024–2025 cost comparison and identify the exact price basis, unit-cost averaging, and data vintages.
- Investigate 2011–2012 archive scope and the actual acquisition date of the 2018 archive copy.
- Compare Coding Guide versions and Item 58 coding rules, including the 1995 transition.
- Build a versioned NBI-to-SNBI data dictionary and identifier crosswalk with confidence levels; preserve raw identifiers and temporary codes.
- Build inspection-history and component-completeness measures.
- Define separate condition, safety/load, service importance, network consequence, and investment modules.
- Assess available bridge-level project/intervention records before attempting causal treatment-effect estimates.
- Only then define a minimum viable predictive model and test candidate deterioration parameters.

## Publication status
Internal working record only. Not approved for publication. All provisional findings above require source-by-source verification.