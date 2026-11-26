# Bridge Model — Source Register

Sources below were checked during the November 26, 2026 research pass. Retrieval date is recorded here; publication/data vintage is given separately. This is a working register, not a claim that every source has been fully extracted or every result independently reproduced.

| ID | Publisher / source | Publication or data vintage | Use in model | URL |
|---|---|---|---|---|
| BR-001 | FHWA, Bridge Condition by Highway System | 2025 data, finalized 2025-06-15 | National/state bridge counts and bridge-area condition; Guam submission caveat | https://www.fhwa.dot.gov/BRIDGE/nbi/no10/condition25.cfm |
| BR-002 | FHWA, Bridge Condition by Owner | 2025 data | Independent national total by owner class; count and area totals | https://www.fhwa.dot.gov/bridge/nbi/no10/owner25e.cfm |
| BR-003 | BTS, Condition of U.S. Highway Bridges | National Transportation Statistics Table 1-28; source as of 2026-10-02 | Historical count/area series; geography and comparability notes | https://www.bts.gov/content/condition-us-highway-bridges |
| BR-004 | CRS, Highway Bridges: Conditions, Funding Programs, and Issues for Congress | R47194; 2025 condition data | Context and independently presented condition totals; not a substitute for underlying NBI | https://www.everycrsreport.com/reports/R47194.html |
| BR-005 | FHWA, Download NBI Data Files | Current page, accessed 2026-11-26 | Archive cadence, finalization date, NBI/SNBI transition, route-clearance caution | https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm |
| BR-006 | FHWA, Download NBI ASCII Files | Current page, accessed 2026-11-26 | Historical archives; 2018 classification change | https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm |
| BR-007 | FHWA, Download NBI ASCII Files 2018 | 2018 archive note | Measurement-data error warning for files downloaded 2019-03-15 to 2019-04-16 | https://www.fhwa.dot.gov/bridge/nbi/ascii2018.cfm |
| BR-008 | FHWA, Computation Procedure for the Transportation Performance Management Bridge Condition Measures, FHWA-HIF-25-010 | 2025-11-03; applies to 2026+ computation | Official NHS deck-area measures, SNBI transition, area computation, incomplete-record exclusions | https://www.fhwa.dot.gov/tpm/guidance/hif25010.pdf |
| BR-009 | FHWA, Frequently Asked Questions — Transportation Performance Management | Current FAQ, accessed 2026-11-26 | Summary of NHS Good/Poor deck-area measures and rating logic | https://www.fhwa.dot.gov/tpm/faq.cfm |
| BR-010 | 23 CFR 650.311, Inspection interval | 2025 CFR edition | Routine inspection intervals and risk-based exceptions | https://www.govinfo.gov/content/pkg/CFR-2025-title23-vol1/pdf/CFR-2025-title23-vol1-sec650-311.pdf |
| BR-011 | FHWA, 2026 Interim National Bridge Inspection Program Metrics | April 2026 | Federal oversight, Metric 22 data quality, Metric 23 timely updates, review cycle | https://www.fhwa.dot.gov/bridge/pubs/NBIP_Metrics_2026_INTERIM.pdf |
| BR-012 | FHWA, LTBP Bridge Performance Primer | FHWA-HRT-13-051, 2013 | NBI limitations; discrete condition ratings; need for element-level data | https://www.fhwa.dot.gov/publications/research/infrastructure/structures/ltbp/13051/index.cfm |
| BR-013 | FHWA, Reliability of Visual Inspection for Highway Bridges | FHWA-RD-01-021, 2001 | Historical study of rating variability; contextualize measurement uncertainty | https://www.fhwa.dot.gov/publications/research/nde/01021.cfm |
| BR-014 | FHWA, Bridge Replacement Unit Costs 2025 | 2025 cost estimate table; accessed 2026-11-26 | Poor bridge replacement/rehabilitation estimates and unit-cost methodology | https://www.fhwa.dot.gov/bridge/nbi/sd2025.cfm |
| BR-015 | FHWA, SNBI Data Crosswalk | SNBI transition documentation | Mapping legacy Coding Guide items to SNBI data items; temporary/partial mapping notes | https://www.fhwa.dot.gov/bridge/snbi/datacrosswalk.cfm |
| BR-016 | FHWA, 1995 Recording and Coding Guide | Legacy coding guide PDF; accessed 2026-11-26 | Item-level definitions and code applicability; detailed version comparison still pending | https://www.fhwa.dot.gov/BRIDGE/mtguide.pdf |
| BR-017 | FHWA, NBI Condition Tables and Definitions | Current tables page | Definition and table directory | https://www.fhwa.dot.gov/bridge/britab.cfm |

## Notes on source use
- BR-001/002 provide 2025 source-vintage cross-checks; retain table-specific geography and submission notes.
- BR-003 is a secondary statistical presentation of FHWA data. Its geography and pre-/post-2020 comparability notes must travel with any historical series.
- BR-008 supersedes older computation logic for 2026 and later datasets; do not apply it retroactively to the 2025 and earlier archive years.
- BR-010 is a regulatory source. Use the applicable current CFR version when implementing inspection interval rules.
- BR-011 is a non-binding FHWA oversight guidance document; its compliance thresholds describe sampled program oversight, not the condition of all bridges.
- BR-013 is historical and sample-based; do not use its observed variability as a current national error distribution without validation.
- BR-014 cost estimates are modelled estimates based on reported inventory, deck area, and unit costs; do not describe them as funded projects, annual needs, or the entire deferred-maintenance backlog.
- BR-016's exact version history and affected NBI code fields remain to be checked before historical recoding.

## Retrieval and audit
Checked 2026-11-26. Before using downloaded files in a reproducible pipeline, record the exact file name, archive year, retrieval date, SHA-256 checksum, licensing/terms, and any post-download transformations. Do not rely on a live webpage alone to reproduce historical results.