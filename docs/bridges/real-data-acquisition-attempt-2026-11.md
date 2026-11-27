# Bridge real-data acquisition attempt: November 2026

**Status:** Official-source acquisition route confirmed; no row-level real-world sample acquired in this session. The model remains uncalibrated.

## 1. Acquisition routes verified

### FHWA InfoBridge

The public InfoBridge Data portal documents a bridge-selection workflow and an Export Data function. It supports Latest Year, All Years, and Year Range exports. The portal states that Item 8 Structure Number may contain previous numbers after renumbering and that the export adds a Latest Year NBI Structure Number column to associate historical rows with a current structure.

The portal also explicitly warns that a bridge may have multiple NBI submittals in one year. This is a material reason to retain source submission identity and avoid collapsing rows solely by bridge number and year.

The portal's Select Data area offers 2025 NBI Data, 2020 NBI Data, and All Data. All Data is described as allowing filtering through all records ever submitted on or after 1993. The portal says its default filtering is based on 2025 data unless All Submittals is selected.

**Practical implication:** InfoBridge is the best candidate route for a deliberately selected small sample with All Years export and a latest-year association field. The current research environment can inspect the portal's rendered documentation but cannot operate its JavaScript-driven bridge selection and export controls. No export was generated.

### FHWA annual NBI downloads

FHWA confirms:
- 2025 was the final year of the legacy Coding Guide ASCII submission format.
- Historical NBI ASCII files from 1992–2025 remain available through its download page.
- 2026 and 2027 are SNBI transition years; temporary codes and null values may occur.
- The 2025 NBI data page reports 8,990 Colorado highway bridges.
- The 2026 NBI data page reports 9,018 Colorado highway bridges.
- Annual submittals can be corrected or updated throughout the year; public highway bridge data is considered final on June 15.

The FHWA download page links to a disclaimer page before the ZIP. Following the 2025 all-state highway-bridge ZIP route surfaced a link to 2025hwybronlyonefile.zip, but the retrieval endpoint returned HTTP 404 in the web retrieval environment. A direct runtime download attempt of the anticipated Colorado JSON endpoint also failed. Therefore neither route produced a local data file in this session.

### Data.gov catalog

The Data.gov National Bridge Inventory catalog identifies the dataset as public, published by FHWA, and describes annual all-state highway bridge ZIP files. Its metadata includes a 2025 distribution entry pointing to the FHWA disclaimer/download route. This confirms catalog metadata and provenance but does not itself provide a parsed bridge sample.

## 2. Why no substitute sample was fabricated

The following are not interchangeable:
- official annual aggregate condition tables;
- an annual bridge-level record;
- an InfoBridge All Years export;
- an actual inspection-event history;
- element-level condition histories.

An aggregate state table cannot test bridge identity matching or event timing. A single-year bridge row cannot validate longitudinal matching. A portal graph or summary does not automatically establish the source date of every observation. The first integration sample must retain source file/export provenance and actual row/object content.

## 3. Proposed first sample design

Once a portal export or annual file is accessible, begin with a small, reproducible sample:
1. Three to five Colorado highway bridges selected across different counties, ownerships, materials/designs, and condition classes.
2. Include at least one bridge with a structure-number history or portal multiple-submittal warning if available.
3. Export All Years for the selected bridge records, with a compact field list.
4. Preserve every source row and portal-provided latest-year structure number.
5. Include Item 8, state/county, location, year built/reconstructed, material/design, length, deck/superstructure/substructure/culvert condition, inspection date, inspection frequency, and relevant load/scour/functional fields.
6. Where available, separately save InfoBridge condition graph CSV and NBE/element history; do not merge those into one observation table.
7. Record export date, portal filter mode, selected bridge count, fields, years, units, and any warning text.

The initial sample should test source structure and temporal relationships only. It should not be used to estimate national deterioration rates.

## 4. Integration gates

Do not call the real-data pipeline validated until:
- source file/export can be retrieved and checksum recorded;
- row counts match portal/export metadata or discrepancies are explained;
- original bridge IDs and latest-year IDs remain separate;
- multiple same-year submissions remain distinct;
- field names, units, nulls, and date formats are profiled;
- historical observations are linked only with explicit evidence or marked as candidates;
- condition graph points are not assumed to be inspection dates without source support;
- synthetic unit tests still pass after real-source adapters are added.

## 5. Current limitations and next action

**Confirmed:** The InfoBridge All Years export design and key caveats; official FHWA annual data availability and source-era boundary; public catalog metadata.

**Not acquired:** An InfoBridge export, a local 2025 Colorado file, a full 2026 Colorado JSON file, or a real bridge's complete inspection-event/condition history.

**Next action:** Use an authenticated interactive browser session to operate InfoBridge's JavaScript-driven selection/export workflow, or obtain a user-supplied official export. The Streamlit dashboard is intentionally deferred until source ingestion and validation have passed the real-data integration gates.

## 6. Source register

- FHWA InfoBridge Data portal: https://infobridge.fhwa.dot.gov/Data
- FHWA InfoBridge update notes: https://infobridge.fhwa.dot.gov/Page/infobridge_update_notes
- FHWA 2025 NBI download page: https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2025.cfm
- FHWA 2026 NBI download page: https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm
- FHWA historical ASCII downloads: https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm
- Data.gov National Bridge Inventory catalog: https://catalog.data.gov/dataset/national-bridge-inventory-nbi

## 7. Evidence classification

**Source-derived:** Official portal export options and warnings; annual data formats, state counts, and publication timing; Data.gov catalog metadata.

**Observed retrieval limitation:** The web retrieval path returned HTTP 404 for the linked 2025 all-state ZIP; direct runtime retrieval of the anticipated Colorado JSON URL failed. These are environment-specific retrieval outcomes, not evidence that the source files do not exist.

**Not claimed:** No row-level source parsing, identity crosswalk validation, or real-world longitudinal test has yet occurred.
