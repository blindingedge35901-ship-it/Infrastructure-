# NBI 2011–2013 Archive Scope and Count Reconciliation

**Research status:** Official FHWA archive instructions and published condition tables checked 2026-11-26. The scope/filter explanation is strongly supported by FHWA documentation. Direct row-level reproduction from the ZIP archives is still pending; do not describe this audit as a completed raw-file validation.

## Executive finding
A major source of the apparent 2011–2012 inventory mismatch is a scope error: **Item 5A = 1 is not, by itself, the definition of a highway bridge.** Item 5A is Record Type. Code 1 means the inventory route is carried on the structure; code 2 and A–Z identify routes passing under a structure. FHWA's pre-2013 archive instructions require additional fields to identify the highway-bridge subset.

FHWA's archived download instructions specify the following highway-bridge filter for pre-2013 data:

- Item 5A = 1
- Item 49 >= 6.1 metres
- Item 112 = Y
- Item 42A = 1, 4, 5, 6, 7, or 8

FHWA states that, beginning in 2013, only highway bridges are written to the download file and an additional status field is added. Therefore, a raw count of every Item 5A=1 record in a 2011 or 2012 archive is not directly comparable with the 2013 download's highway-bridge count.

## Published count comparison

| Year | FHWA archive page: Item 5A=1 records | FHWA condition table: all highway bridges | Difference (raw 5A=1 minus condition count) | BTS Table 1-28 count |
|---|---:|---:|---:|---:|
| 2011 | 608,488 | 605,103 | 3,385 | 605,087 |
| 2012 | 609,908 | 607,380 | 2,528 | 607,378 |
| 2013 | 607,751 | 607,751 | — | 607,708 |

Interpretation:
- The first two archive-page figures are the Item 5A=1 column totals on FHWA's 2011 and 2012 archive pages. They are not the final highway-bridge subset totals after the full filter.
- The FHWA condition-table totals are the appropriate published comparator for all public highway bridges in those years.
- The 2013 archive page explicitly lists only highway bridges; its total agrees with the 2013 FHWA condition table.
- The raw-to-condition differences of 3,385 (2011) and 2,528 (2012) are consistent with the need to apply additional highway-bridge filters. They are not evidence that thousands of bridges disappeared between years.
- BTS Table 1-28 differs slightly from the FHWA condition table: 16 bridges in 2011, 2 in 2012, and 43 in 2013. Treat these as separate source-vintage/revision discrepancies until the exact BTS download vintage and FHWA table snapshots are reconciled. Do not silently replace one series with the other.

## The 10-year rule: separate issue
FHWA describes the 2011 archive as prior data applying the cancelled 10-year rule, under which bridges built or reconstructed in the previous ten years were excluded because they were generally not eligible for Highway Bridge Program funding. The 2012 archive note says the downloaded data include status both considering and not considering the 10-year rule.

However, FHWA's published 2011 and 2012 Bridge Condition by Highway System pages each explicitly state: **“10-Year Rule does not apply.”** This establishes that the condition-table totals shown above are not using the 10-year rule for the condition presentation.

The evidence therefore supports two distinct analytical questions:
1. **Inventory inclusion:** Which records qualify as public highway bridges? Use the FHWA highway-bridge filter for the 2011–2012 archives, not Item 5A=1 alone.
2. **Deficiency status:** How did applying the 10-year rule change a bridge's program/deficiency status? Use the separate 2012 status fields to test this. Do not treat a status-policy change as a change in physical inventory or bridge count.

The 10-year rule may affect eligibility/deficiency classification, but the published pages reviewed here do not support using it as the explanation for the raw Item 5A=1 versus highway-bridge inventory count difference.

## What is now established
- Item 5A is Record Type, not a standalone highway-bridge flag.
- FHWA's pre-2013 filter is explicit and includes Items 5A, 49, 112, and 42A.
- FHWA's 2013 archive download is pre-filtered to highway bridges.
- FHWA's 2011 and 2012 condition pages state that the 10-year rule does not apply to those published condition totals.
- The 2011 and 2012 raw Item 5A=1 counts exceed the corresponding FHWA condition totals by 3,385 and 2,528, respectively.
- The 2013 archive and FHWA condition totals both equal 607,751.

## What remains unresolved
1. Download the original FHWA 2011, 2012, and 2013 single-file ZIP archives and preserve their exact filenames, retrieval date, and SHA-256 hashes.
2. Parse each archive using its vintage-specific record layout; count unique structure identifiers and Item 5A values before filtering.
3. Apply the full highway-bridge filter to the 2011 and 2012 files and verify that row counts reproduce the FHWA condition-table totals (605,103 and 607,380). Check whether the 2011 archive page's “highway bridges” ZIP is already partially filtered in any way; the official instruction says users must still distinguish the highway subset.
4. Compare the 2012 status fields with and without the 10-year rule, holding the inventory population constant. Quantify the change in deficiency status, not just raw record count.
5. Compare 2013 raw records and status fields to the 2012 filtered population, and inspect additions, removals, duplicates, and identifier changes.
6. Reconcile the small FHWA-versus-BTS differences (16, 2, and 43 records) using dated source files and documented revisions.
7. Verify the exact item positions and field definitions for Items 42A, 49, and 112 in the applicable record layouts before coding the parser.

## Modeling decision
Until the raw files are downloaded and the filters reproduced, use the FHWA condition-table totals for descriptive national trend context, clearly tagged as published aggregate data. Do not use raw 5A=1 totals as the national highway-bridge denominator. Do not infer bridge loss, additions, or physical deterioration from the unfiltered count differences. Keep the 10-year-rule status comparison separate from inventory scope.

## Sources
- FHWA, Download NBI ASCII Files (historical filter instructions and 2013 transition): https://www.fhwa.dot.gov/bridge/nbi/ascii160927.cfm
- FHWA, 2011 NBI archive page: https://www.fhwa.dot.gov/bridge/nbi/ascii2011.cfm
- FHWA, 2012 NBI archive page: https://www.fhwa.dot.gov/bridge/nbi/ascii2012.cfm
- FHWA, 2013 NBI archive page: https://www.fhwa.dot.gov/bridge/nbi/ascii2013.cfm
- FHWA, 2011 Bridge Condition by Highway System: https://www.fhwa.dot.gov/bridge/nbi/no10/condition11.cfm
- FHWA, 2012 Bridge Condition by Highway System: https://www.fhwa.dot.gov/bridge/nbi/no10/condition12.cfm
- FHWA, 2013 Bridge Condition by Highway System: https://www.fhwa.dot.gov/bridge/nbi/no10/condition13.cfm
- FHWA, NBI Record Format: https://www.fhwa.dot.gov/bridge/nbi/format.cfm
- FHWA, Recording and Coding Guide (Item 5A definition): https://www.fhwa.dot.gov/bridge/mtguide.pdf
- BTS, Table 1-28 historical series: https://www.bts.gov/archive/publications/national_transportation_statistics/table_01_28

**Internal research record only. Not approved for publication.**