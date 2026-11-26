# State-Level NBI Archive Discontinuity Audit

**Status:** Preliminary aggregate audit completed; record-level identity reconciliation remains open.
**Research date:** 2026-11-26
**Scope:** Mississippi 1996–1997, Minnesota 2008–2009, Pennsylvania 2010–2011.
**Use:** Internal research only; not approved for publication.

## Executive findings

1. **Mississippi, 1996–1997:** Item 5A=1 changes from 16,831 to 16,805 (-26). Item 5A=2 falls from 552 to 164, while A–Z rises from 0 to 952. This strongly suggests a record-type classification/reporting change among non-Type-1 records, not a sudden loss of 388 Type 1 bridges. The administrative reason and individual record transitions remain unverified.
2. **Minnesota, 2008–2009:** Item 5A=1 falls from 19,822 to 13,132 (-6,690; approximately -33.8%). The 2007 count was 19,737; 2010 and 2011 remain near 13,100 (13,108 and 13,117). Type 2 and A–Z counts do not show a compensating shift. This is a major unresolved archive discontinuity; do not interpret it as physical bridge removals.
3. **Pennsylvania, 2010–2011:** Item 5A=1 falls from 22,362 to 22,322 (-40; approximately -0.18%). Nearby counts are similarly stable (22,386 in 2008; 22,330 in 2009). Aggregate counts do not support a major coverage break, but cannot prove identifier continuity.

## Published FHWA archive counts

| State | Year | Item 5A=1 | Item 5A=2 | Item 5A=A–Z |
|---|---:|---:|---:|---:|
| Mississippi | 1996 | 16,831 | 552 | 0 |
| Mississippi | 1997 | 16,805 | 164 | 952 |
| Minnesota | 2007 | 19,737 | 2,025 | 846 |
| Minnesota | 2008 | 19,822 | 2,068 | 856 |
| Minnesota | 2009 | 13,132 | 2,065 | 868 |
| Minnesota | 2010 | 13,108 | 2,051 | 872 |
| Minnesota | 2011 | 13,117 | 2,067 | 874 |
| Pennsylvania | 2008 | 22,386 | 2,739 | 4,380 |
| Pennsylvania | 2009 | 22,330 | 2,706 | 4,322 |
| Pennsylvania | 2010 | 22,362 | 2,715 | 4,322 |
| Pennsylvania | 2011 | 22,322 | 2,705 | 4,351 |

These are FHWA-published archive summary counts, not a record-level reproduction and not necessarily the final filtered public-highway-bridge denominator.

## Item 5A meaning and historical filters

FHWA defines Item 5A as Record Type:
- 1: route carried on the structure;
- 2: a single route goes under the structure;
- A–Z: multiple routes go under the structure.

Type 1 is not synonymous with all NBI records, and Item 5A alone is not a complete public-highway-bridge inclusion test. FHWA's historical archive guidance for pre-2013 extracts specifies the additional highway-bridge filter: Item 5A=1, Item 49 >= 6.1 metres, Item 112=Y, and Item 42A in 1, 4, 5, 6, 7, or 8. Starting in 2013, FHWA says only highway bridges are written to the download file.

## Identifier continuity

NBI Item 8 is the Structure Number. FHWA InfoBridge notes that Item 8 can contain previous structure numbers in some years and that this does not necessarily mean the historical rows refer to different unique structures. Its export includes a Latest Year NBI Structure Number field to associate historical rows with the latest number. FHWA's SNBI Data Crosswalk says Previous Bridge Number is populated using the history of structure-number changes held in NBI Structure Number Change submittals.

Implications:
- Preserve raw Item 8 exactly as submitted for every year.
- Do not use raw Item 8 as an immutable cross-year physical-asset key.
- Where available, use official structure-number-change history / latest-year bridge number to create a versioned identity crosswalk.
- Retain predecessor and successor IDs, source vintage, and confidence; do not silently merge records.
- Without an official crosswalk, use probabilistic candidate matching based on state, county, location, intersected feature, carried facility, coordinates, route/milepoint and structure characteristics. Mark inferred links as inferred, never official.
- A structure-number change, route change, and physical replacement are separate events.

## State-specific disposition

### Mississippi 1996–1997

**Aggregate diagnosis:** Type 1 count is stable while other Item 5A categories shift sharply. The evidence supports a record-type reporting/coding discontinuity, not a Type 1 inventory collapse. Exact record transitions and the administrative reason remain unknown.

**Model treatment:** Do not flag the Type 1 denominator as discontinuous from these aggregate counts alone. Flag the Item 5A category mix as a coding/reporting break. Bridge-level identity tracking still requires raw files and structure-number-change history.

### Minnesota 2008–2009

**Aggregate diagnosis:** Large Type 1 drop in 2009, persisting through 2010–2011. Other Item 5A categories do not absorb the missing count. The public archive summary does not explain the cause.

**Model treatment:** Treat 2008–2009 as a hard unresolved series break. Exclude the raw difference from physical additions/removals and trend calibration until original state files, applicable filters, and state reporting documentation have been checked. Do not splice the two regimes with a simple adjustment factor.

**Required evidence:** Row-level comparison of the 2008 and 2009 Minnesota extracts; state bridge inventory reports or NBI submittal notes; exact filters and file variants; structure-number-change submissions.

### Pennsylvania 2010–2011

**Aggregate diagnosis:** Type 1 count is broadly stable. No major coverage break is visible in the published counts. This does not resolve identifier continuity, because structure-number changes can occur without changing the total inventory count.

**Model treatment:** Keep the state in the aggregate inventory series, but do not claim identifier continuity until record-level matching or official structure-number-change history is examined.

## Evidence limits

- Values were transcribed from FHWA annual archive summary tables. The underlying ZIP archives have not yet been downloaded and independently parsed.
- Aggregate counts cannot identify individual records added, deleted, recoded, renumbered, or replaced.
- Minnesota's cause remains unknown; any explanation beyond the observed discontinuity would be speculative.
- FHWA's InfoBridge and SNBI crosswalk material establishes that structure-number changes occur and that previous numbers can persist in historical exports. It does not itself provide the complete state/year crosswalk needed here.

## Sources

1. FHWA 1996 NBI archive: https://www.fhwa.dot.gov/bridge/nbi/ascii1996.cfm
2. FHWA 1997 NBI archive: https://www.fhwa.dot.gov/bridge/nbi/ascii1997.cfm
3. FHWA 2007 NBI archive: https://www.fhwa.dot.gov/bridge/nbi/ascii2007.cfm
4. FHWA 2008 NBI archive: https://www.fhwa.dot.gov/bridge/nbi/ascii2008.cfm
5. FHWA 2009 NBI archive: https://www.fhwa.dot.gov/bridge/nbi/ascii2009.cfm
6. FHWA 2010 NBI archive: https://www.fhwa.dot.gov/bridge/nbi/ascii2010.cfm
7. FHWA 2011 NBI archive: https://www.fhwa.dot.gov/bridge/nbi/ascii2011.cfm
8. FHWA NBI Record Format: https://www.fhwa.dot.gov/bridge/nbi/format.cfm
9. FHWA historical archive filter guidance: https://www.fhwa.dot.gov/bridge/nbi/ascii160927.cfm
10. FHWA SNBI Data Crosswalk: https://www.fhwa.dot.gov/bridge/snbi/datacrosswalk.cfm
11. FHWA InfoBridge data export notes: https://infobridge.fhwa.dot.gov/Data
12. FHWA InfoBridge update notes: https://infobridge.fhwa.dot.gov/Page/infobridge_update_notes

## Next research action

Obtain and checksum the original annual state extracts, then:
1. Parse each fixed-width/CSV file using its year-specific record layout.
2. Reproduce FHWA highway-bridge filters before comparing denominators.
3. Compare raw Item 8 IDs and normalized IDs separately.
4. Use official structure-number-change history where obtainable.
5. For unmatched records, compare location/coordinates, county, intersected feature, carried route, year built, material, design type, length, and deck area to classify likely renumbering, additions, removals, replacements, or unresolved matches.
6. Revise historical inventory series or infer physical stock flows only after this reconciliation.

**Publication status:** Internal working research only; not approved for publication.
