# Bridge Infrastructure Model — Research Status

**Status:** In progress — baseline findings and measurement risks identified; source verification and specification remain to be completed.

## Scope
Develop a national and state-level bridge model that distinguishes inventory and physical condition from safety, service importance, network consequence, investment, and workforce capacity. The model should support both counts and exposure-weighted measures where the source definitions permit them.

## Findings carried forward from prior research
The following are working findings from the preceding bridge-research work. They must be tied to exact source records, archived source vintages, and retrieval dates in the source register before they are treated as final repository evidence or publication claims.

- A 2025 FHWA baseline was reported as 624,193 public highway bridges across states, DC, Puerto Rico, and the U.S. Virgin Islands; Guam was not in that 2025 dataset.
- A CRS 2025 condition summary was reported as 272,779 Good, 309,729 Fair, and 41,685 Poor. These are bridge counts, not NHS deck-area-weighted performance measures.
- A separate FHWA 2025 cost table was reported as 4,341 Poor NHS bridges plus 37,336 Poor non-NHS bridges (41,677 total), eight fewer than the CRS count. Preserve and investigate the discrepancy rather than forcing a match.
- The same cost table was reported to estimate approximately $49.67 billion in Poor NHS replacement cost and $35.78 billion in Poor non-NHS replacement cost (about $85.45 billion combined), with a rehabilitation estimate around $58.10 billion using a 68% factor. These are estimates for the Poor inventory represented in that table, not a complete national backlog, annual funding requirement, or project list.
- A 2024-to-2025 comparison was reported as Poor bridge count 42,067 to 41,677, nominal replacement cost about $82.23 billion to $85.45 billion, and deck area about 212.83 million to 214.00 million square feet. This does not by itself establish that the backlog worsened; changes in inventory mix, prices, area, and vintage matter. The dollar figures were not inflation-adjusted.
- The 2018 change from Structurally Deficient terminology to Poor is a classification break; do not splice the labels as if they were automatically equivalent.
- The 1995 NBI Coding Guide transition affects applicability of N-code interpretation for Item 58.
- Archived 2011–2012 NBI subsets were reported to be materially below published FHWA Type 1 totals. Their cause remains unresolved; exclude those subsets from national trend fitting until reconciled.
- The 2013 NBI archive changes the highway-bridge subset workflow: pre-2013 files require user filtering to identify the highway bridge subset, while the 2013 download is already highway-bridge scoped and includes a status field. This does not resolve the 2011–2012 gap.
- FHWA warned that 2018 archive files obtained March 15 through April 16, 2019 should be re-downloaded because of measurement-data errors; the acquisition date of the copy previously reviewed is unknown.
- Potential identifier discontinuities were noted for Mississippi 1996–1997, Pennsylvania 2010–2011, and Minnesota 2008–2009. Candidate links are not official crosswalks. Preserve raw identifiers and jurisdiction/vintage context; do not silently infer asset identity.
- The SNBI transition is not a simple field rename. Preserve raw and normalized identifiers, temporary codes, and any predecessor/successor relationships with provenance.
- Routine inspection intervals may be risk-based (12, 24, 48, or 72 months); Poor bridges were reported to have a maximum 24-month interval and Fair bridges 48 months. An annual archive row is not proof of an annual inspection; use actual inspection dates and elapsed time.
- NHS performance measures use deck-area weighting, not bridge-count share; Fair is excluded from the stated Good/Poor target measure. Maintain count-based and deck-area-weighted outputs separately.
- The 2025 FHWA area calculation was reported to use length multiplied by out-to-out width when available, otherwise approach roadway width through 2027; from 2028, SNBI requires out-to-out width for all bridges, including buried bridges. Verify the applicable official technical specification before implementation.
- Condition ratings may be derived from one or more reported components; records with all four component ratings missing were reported excluded from the relevant calculation. Component completeness must be visible.
- NBI Good/Fair/Poor is not a complete engineering risk measure. Keep safety, load rating/posting, service importance, and network consequence separate.
- A 2001 FHWA visual-inspection reliability study of 49 inspectors from 25 agencies rating seven bridges was reported to find about 68% of ratings within one point of the average, 95% within two points, and as many as five different values. This is historical evidence, not proof of identical variability in current inspections.
- The FHWA Long-Term Bridge Performance primer was reported to note that NBI lacks subelement condition, extent, location, and cause detail, and that discrete condition ratings are not continuous equal increments.
- FHWA's 2024 preservation roadmap was reported to identify limited data on post-preservation deterioration, service life, costs, and effectiveness. Do not invent treatment coefficients.
- FHWA's 2026 NBIP interim metrics were reported to include 25 oversight metrics, risk-based review levels, and a general requirement for at least one intermediate/in-depth review per metric in a five-year cycle (subject to exceptions). Reported data-quality and update metrics concern inspection-program oversight, not physical condition scores; public annual panel data were not identified in the prior work.
- Bridge spending must be separated into allocation, obligation, outlay, contract award, construction start, completion, and verified bridge-level work. Federal obligations are not equivalent to cash outlays or all bridge investment. No complete national bridge-level history linking all dollars to interventions and subsequent condition was identified in the prior work.

## Modeling implications
1. Use a stock-and-flow framing for inventory, condition transitions, deterioration, preservation, rehabilitation, replacement, and removals—but estimate transition/treatment parameters only where longitudinal evidence supports them.
2. Maintain parallel count-based and deck-area-weighted condition views.
3. Separate condition from safety, load capacity, service importance, detour/network consequence, and exposure.
4. Track inspection date, interval, and data completeness; do not treat annual snapshots as annual inspections.
5. Treat classification, coding, archive, and identifier breaks as explicit discontinuities.
6. Keep investment stages separate and avoid attributing condition changes to spending without bridge-level intervention evidence.
7. Treat LTBP and other detailed samples as mechanism/validation evidence, not as a national census.

## Unresolved work before model specification
- Reopen and record exact FHWA, CRS, LTBP, and NBIP source URLs, publication dates, table names, file vintages, and retrieval dates.
- Recompute the 2025 inventory and condition counts directly from the exact source files and record filters and exclusions.
- Reconcile (or retain as unresolved) the eight-bridge difference between CRS and the FHWA cost table.
- Reproduce the 2024–2025 comparison and determine which values are nominal, revised, or vintage-dependent.
- Resolve 2011–2012 archive coverage and inspect the actual 2018 archive copy/acquisition date.
- Build an NBI-to-SNBI data dictionary and a versioned identifier crosswalk with confidence levels; do not assume cross-jurisdiction or temporal identity.
- Verify inspection interval rules and current condition-rating calculation rules against official manuals/specifications.
- Verify NHS deck-area methodology and transition to SNBI width fields.
- Build a spending taxonomy and determine which bridge-level project/intervention records are linkable to condition histories.
- Define a minimum viable model only after the above measurement audit; then test candidate deterioration and intervention parameters.

## Publication status
Internal working record only. Not approved for publication. All figures and technical details above remain provisional until source-by-source verification is completed.