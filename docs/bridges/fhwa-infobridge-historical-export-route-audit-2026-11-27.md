# FHWA InfoBridge Historical NBI Export Route Audit

**Audit date:** 2026-11-27  
**Status:** Official historical export route confirmed from portal documentation; actual export not yet executed or retrieved.

## Finding

FHWA's LTBP InfoBridge Data portal provides a historical-submittal selection mode and an export interface that explicitly supports selecting **All Years** or a year range. The portal describes All Submittals as records ever submitted on or after 1993. This is a promising official route for building a longitudinal NBI panel without manually downloading every annual ZIP archive.

Primary portal:
- https://infobridge.fhwa.dot.gov/Data

## Directly observed portal details

The page states:
- Default filtering uses the 2025 NBI submittal unless All Submittals is selected.
- All Submittals includes records ever submitted on or after 1993.
- The selected-bridges table shows one record for every bridge selected by the filters.
- The export interface offers Latest Year, All Years, and Year Range.
- Export is based on selected data attributes and the selected year option.
- The portal warns that NBI Item 8 (Structure Number) may include previous structure numbers in certain years and could incorrectly imply information applies to different unique structures.
- The portal adds a Latest Year NBI Structure Number column to help identify rows related to each unique structure.
- An export limit exists and may require reducing selected attributes.
- Special Projects data is available only for the latest year.

These details were confirmed on the rendered page at https://infobridge.fhwa.dot.gov/Data, especially the Select Data section and Export Data section.

Related FHWA update note:
- https://infobridge.fhwa.dot.gov/Page/infobridge_update_notes
- January 2021 update note says the All Submittals selection was introduced to include historical data submitted since 1993 and to view historical records in the selected-bridges table and NBI data tab.

## Why this route is valuable

This is an official FHWA portal, and its export is explicitly designed to present historical records. It may avoid the current runtime's difficulty downloading large annual FHWA ZIP/JSON files. It also exposes an FHWA-provided latest-year structure-number association field, which is directly useful for investigating identifier continuity.

Potential use:
1. Start with a bounded Colorado selection to establish export behavior and file structure.
2. Select a compact set of high-value attributes first: state, county, structure number, latest-year structure number, year, bridge length, year built/reconstructed, material/design, component condition ratings, inspection date, inspection frequency, traffic, load posting, scour, and relevant geometry.
3. Export All Years for the bounded selection.
4. Inspect the actual file, headers, row count, year coverage, multiple-submittal cases, nulls, and duplicate keys.
5. Compare portal records and aggregates against published FHWA annual baselines.
6. Expand to all states or broader attribute selections only after export limits and semantics are understood.

## Important limitations and cautions

- The portal's latest-year structure-number field is a useful source-provided association aid, not proof that every historical record is the same physical asset. Preserve original Item 8 and the added latest-year key separately.
- Do not assume one record per physical bridge per year. The portal itself warns that a bridge can have multiple NBI submittals in one year.
- All Submittals means records submitted since 1993; it does not imply complete pre-1993 history.
- A selected-attribute export is not the same thing as the full annual raw NBI archive. It may be excellent for a panel but cannot validate every field or the legacy fixed-width parser.
- Historical data may contain schema, field definition, coding, reporting, and source-vintage discontinuities already documented in the bridge audits.
- The portal page is JavaScript-driven. The web page inspection confirms the interface and options but does not execute the interactive export.
- No actual export file has been downloaded or inspected as part of this audit. No record-level test, row count, hash, or panel has been produced yet.

## Recommended next test

Attempt the smallest useful export first: Colorado, all historical submittals available in InfoBridge, and a deliberately narrow set of fields. Record the export date, selected filters, selected attributes, year coverage, source labels, and raw file hash. Do not build identity links from the added latest-year key until its behavior is inspected against known structure-number changes and the existing FHWA identity documentation.

## Source hierarchy

1. FHWA annual NBI ASCII/JSON files remain the primary raw source of record.
2. FHWA InfoBridge historical export is an official FHWA-derived analytical extract and a strong candidate for longitudinal panel construction.
3. Third-party republications may be used as secondary checks only, with lineage and discrepancies retained.
