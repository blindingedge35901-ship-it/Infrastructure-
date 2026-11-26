# FHWA Bridge Field Mapping Verification Audit v0.1

**Reviewed:** 2026-11-26  
**Status:** Official-page and indexed-table verification; not a full spreadsheet-row extraction.  
**Purpose:** Correct and extend the provisional bridge data dictionary before parser implementation.  
**Publication:** Internal technical research only.

## 1. Executive findings

1. FHWA's current NBI Record Format page specifies a 445-character record with explicit field positions and lengths.
2. The 445-character record contains agency-submitted fields and three FHWA download-only fields at positions 434–445: CAT10 Bridge Condition, CAT23 Lowest Condition Code, and CAT29 Deck Area. These must not be mistaken for original agency-submitted values.
3. The legacy NBI ASCII era ends with the 2025 data submission. FHWA says 2026 and later use SNBI JSON; 2026–27 transition records may contain temporary codes and nulls.
4. The crosswalk identifies non-clean transitions and requires care with bridge-number normalization. For B.ID.01, leading/trailing spaces are trimmed, but handling leading zeroes is an explicit user/agency decision; original legacy data must remain preserved.
5. SNBI has one-to-many and many-to-one relationships. A flat one-row-per-bridge parser would lose feature and route structure.
6. FHWA has published a 2026 dataset landing page and reports 624,939 highway bridges in its displayed national total; Guam did not submit 2026 data.

## 2. Legacy 445-character record format — verified fields

FHWA's current NBI Record Format page specifies a 445-character record. Positions below are one-based and inclusive.

| Item | Name | Positions | Length / type |
|---|---|---:|---|
| 1 | State Code | 1–3 | 3/N |
| 8 | Structure Number | 4–18 | 15/AN |
| 5A | Record Type | 19 | 1/AN |
| 5B | Route Signing Prefix | 20 | 1/N |
| 5C | Designated Level of Service | 21 | 1/N |
| 5D | Route Number | 22–26 | 5/AN |
| 5E | Directional Suffix | 27 | 1/N |
| 2 | Highway Agency District | 28–29 | 2/AN |
| 3 | County (Parish) Code | 30–32 | 3/N |
| 4 | Place Code | 33–37 | 5/N |
| 6A | Features Intersected | 38–61 | 24/AN |
| 6B | Critical Facility Indicator | 62 | 1/AN |
| 7 | Facility Carried by Structure | 63–80 | 18/AN |
| 9 | Location | 81–105 | 25/AN |
| 10 | Inventory Route Minimum Vertical Clearance | 106–109 | 4/N |
| 11 | Kilometerpoint | 110–116 | 7/N |
| 12 | Base Highway Network | 117 | 1/N |
| 13A | LRS Inventory Route | 118–127 | 10/AN |
| 13B | Subroute Number | 128–129 | 2/N |
| 16 | Latitude | 130–137 | 8/N |
| 17 | Longitude | 138–146 | 9/N |
| 19 | Bypass/Detour Length | 147–149 | 3/N |
| 20 | Toll | 150 | 1/N |
| 21 | Maintenance Responsibility | 151–152 | 2/N |
| 22 | Owner | 153–154 | 2/N |
| 26 | Functional Class of Inventory Route | 155–156 | 2/N |
| 27 | Year Built | 157–160 | 4/N |
| 28A | Lanes on Structure | 161–162 | 2/N |
| 28B | Lanes Under Structure | 163–164 | 2/N |
| 29 | Average Daily Traffic | 165–170 | 6/N |
| 30 | Year of Average Daily Traffic | 171–174 | 4/N |
| 31 | Design Load | 175 | 1/N |
| 32 | Approach Roadway Width | 176–179 | 4/N |
| 41 | Structure Open/Posted/Closed | 199 | 1/AN |
| 42A | Type of Service on Bridge | 200 | 1/N |
| 42B | Type of Service Under Bridge | 201 | 1/N |
| 43A | Main Structure Kind of Material/Design | 202 | 1/N |
| 43B | Main Structure Type of Design/Construction | 203–204 | 2/N |
| 44A | Approach Span Kind of Material/Design | 205 | 1/N |
| 44B | Approach Span Type of Design/Construction | 206–207 | 2/N |
| 45 | Number of Spans in Main Unit | 208–210 | 3/N |
| 46 | Number of Approach Spans | 211–214 | 4/N |
| 48 | Length of Maximum Span | 218–222 | 5/N |
| 49 | Structure Length | 223–228 | 6/N |
| 50A | Left Curb/Sidewalk Width | 229–231 | 3/N |
| 50B | Right Curb/Sidewalk Width | 232–234 | 3/N |
| 51 | Bridge Roadway Width Curb-to-Curb | 235–238 | 4/N |
| 52 | Deck Width Out-to-Out | 239–242 | 4/N |
| 58 | Deck | 259 | 1/AN |
| 59 | Superstructure | 260 | 1/AN |
| 60 | Substructure | 261 | 1/AN |
| 61 | Channel/Channel Protection | 262 | 1/AN |
| 62 | Culverts | 263 | 1/AN |
| 63 | Method Used to Determine Operating Rating | 264 | 1/N |
| 64 | Operating Rating | 265–267 | 3/N |
| 65 | Method Used to Determine Inventory Rating | 268 | 1/N |
| 66 | Inventory Rating | 269–271 | 3/N |
| 67 | Structural Evaluation | 272 | 1/AN |
| 68 | Deck Geometry | 273 | 1/AN |
| 69 | Underclearance, Vertical & Horizontal | 274 | 1/AN |
| 70 | Bridge Posting | 275 | 1/N |
| 71 | Waterway Adequacy | 276 | 1/AN |
| 72 | Approach Roadway Alignment | 277 | 1/AN |
| 75A | Type of Work Proposed | 278–279 | 2/N |
| 75B | Work Done By | 280 | 1/AN |
| 76 | Length of Structure Improvement | 281–286 | 6/N |
| 90 | Inspection Date | 287–290 | 4/N |
| 91 | Designated Inspection Frequency | 291–292 | 2/N |
| 92A | Fracture Critical Details | 293–295 | 3/AN |
| 92B | Underwater Inspection | 296–298 | 3/AN |
| 92C | Other Special Inspection | 299–301 | 3/AN |
| 93A | Fracture Critical Details Date | 302–305 | 4/AN |
| 93B | Underwater Inspection Date | 306–309 | 4/AN |
| 93C | Other Special Inspection Date | 310–313 | 4/AN |
| 94 | Bridge Improvement Cost | 314–319 | 6/N |
| 95 | Roadway Improvement Cost | 320–325 | 6/N |
| 96 | Total Project Cost | 326–331 | 6/N |
| 97 | Year of Improvement Cost Estimate | 332–335 | 4/N |
| 98A | Neighboring State Code | 336–338 | 3/AN |
| 98B | Percent Responsibility | 339–340 | 2/N |
| 99 | Border Bridge Structure Number | 341–355 | 15/AN |
| 100 | STRAHNET Highway Designation | 356 | 1/N |
| 101 | Parallel Structure Designation | 357 | 1/AN |
| 102 | Direction of Traffic | 358 | 1/N |
| 103 | Temporary Structure Designation | 359 | 1/AN |
| 104 | Highway System of Inventory Route | 360 | 1/N |
| 105 | Federal Lands Highways | 361 | 1/N |
| 106 | Year Reconstructed | 362–365 | 4/N |
| 107 | Deck Structure Type | 366 | 1/AN |
| 108A | Type of Wearing Surface | 367 | 1/AN |
| 108B | Type of Membrane | 368 | 1/AN |
| 108C | Deck Protection | 369 | 1/AN |
| 109 | Average Daily Truck Traffic | 370–371 | 2/N |
| 110 | Designated National Network | 372 | 1/N |
| 111 | Pier/Abutment Protection | 373 | 1/N |
| 112 | NBIS Bridge Length | 374 | 1/AN |
| 113 | Scour Critical Bridges | 375 | 1/AN |
| 114 | Future Average Daily Traffic | 376–381 | 6/N |
| 115 | Year of Future Average Daily Traffic | 382–385 | 4/N |
| 116 | Minimum Navigation Vertical Clearance, Vertical Lift Bridge | 386–389 | 4/N |

The format page also shows download-only fields, not part of the NBI submittal file:
- Federal Agency Indicator: position 390;
- Submitted By: positions 391–392;
- Washington Headquarters Use: positions 393–433;
- CAT10 Bridge Condition: position 434;
- CAT23 Lowest Condition Code: position 435;
- CAT29 Deck Area: positions 436–445.

**Parser rule:** do not interpret positions 390–445 as ordinary agency-submitted legacy NBI fields. Preserve them as FHWA download augmentation with provenance. CAT10, CAT23, and CAT29 are derived/download fields, not raw inspection submissions.

**Layout caution:** FHWA's older Coding Guide Appendix E search result shows a 432-character record. The current format page shows 445 characters. This proves a single timeless parser is unsafe. Determine the applicable layout and amendments by vintage before parsing historical files; do not apply the current 445-position map blindly back to 1992.

## 3. Verified legacy-to-SNBI mappings

The following mappings are explicitly visible in FHWA's indexed Data Crosswalk tables for “Over” records or “Under” records applying to the whole bridge.

| Legacy item | Legacy name | SNBI item | SNBI name | Transition status / note |
|---|---|---|---|---|
| 8 | Structure Number | B.ID.01 | Bridge Number | Clean; trim leading/trailing spaces. Leading-zero handling is an explicit choice; preserve original legacy values |
| N/A | — | B.ID.02 | Bridge Name | No legacy equivalent; no direct transition |
| N/A | — | B.ID.03 | Previous Bridge Number | Populate from NBI structure-number-change history |
| 1 | State Code | B.L.01 | State Code | Direct mapping shown |
| 3 | County Code | B.L.02 | County Code | Direct mapping shown |
| 4 | Place Code | B.L.03 | Place Code | Direct mapping shown |
| 7 | Facility Carried | B.F.03 | Feature Name | “Under” record whole-bridge mapping; retain feature context |
| 9 | Bridge Location | B.L.11 | Bridge Location | “Under” record whole-bridge mapping |
| 16 | Latitude | B.L.05 | Latitude | Direct mapping shown |
| 17 | Longitude | B.L.06 | Longitude | Direct mapping shown |
| 20 | Toll | B.CL.05 | Toll | “Under” record whole-bridge mapping |
| 27 | Year Built | B.W.01 | Year Built | Direct mapping shown |
| 28A | Lanes on Structure | B.H.08 | Number of Lanes on the Highway | Applies to highway feature |
| 42A | Type of Service on Bridge | B.F.01 / B.F.02 | Feature Type / Feature Location | Mapping is to two feature items |
| 43 | Structure Type, Main | Multiple | Multiple SNBI items | Not a single-field mapping |
| 48 | Length of Maximum Span | B.G.03 / B.G.04 | Maximum Span Length / Minimum Span Length | Two destination items; verify detailed transformation logic |
| 49 | Structure Length | B.G.01 / B.G.02 | NBIS Bridge Length / Total Bridge Length | Two destination items; do not assume identical definitions |
| 103 | Temporary Structure Designation | B.PS.01 | Load Posting Status | Crosswalk entry requires detailed semantic review before encoding |

The table is intentionally limited to mappings visible in the indexed FHWA crosswalk result. It is not a complete transcription of the spreadsheet.

### 3.1 Verified transformation-sensitive cases

**B.ID.01 Bridge Number**
- Legacy Item 8 maps to B.ID.01.
- FHWA instructs trimming leading and trailing spaces.
- For the transition tool, FHWA says to provide an option for handling leading zeroes, including retaining all, trimming all, or trimming all but one leading zero; no default selection is prescribed.
- Preserve original legacy identifier.
- Do not silently strip zeroes or treat normalization as proof of physical identity.

**B.ID.03 Previous Bridge Number**
- No legacy Coding Guide item directly maps to it.
- FHWA says it is populated using structure-number-change history held in the NBI.
- This is identity history, not a simple field rename.

**B.ID.02 Bridge Name**
- No legacy equivalent is shown.
- Do not synthesize a historical bridge name from route or feature text and label it source-reported.

**B.G.03 / B.G.04 and B.G.01 / B.G.02**
- Crosswalk maps legacy maximum span and structure length into multiple SNBI geometry concepts.
- Retain separate concepts; do not assume one-to-one numerical carryover.
- Verify detailed transformation rules and units against current SNBI specification and crosswalk workbook.

**B.PS.01**
- Crosswalk table lists legacy Item 103 as a source for this item. Since the SNBI label is Load Posting Status, this mapping requires close reading of detailed transition notes and specification before semantic transformation is encoded. Do not rely on a superficial name match.

## 4. Verified SNBI item families

### 4.1 Geometry items

FHWA SNBI specification lists:
- B.G.01 NBIS Bridge Length
- B.G.02 Total Bridge Length
- B.G.03 Maximum Span Length
- B.G.04 Minimum Span Length
- B.G.05 Bridge Width Out-to-Out
- B.G.06 Bridge Width Curb-to-Curb
- B.G.07 Left Curb or Sidewalk Width
- B.G.08 Right Curb or Sidewalk Width
- B.G.09 Approach Roadway Width
- B.G.10 Bridge Median
- B.G.11 Skew
- B.G.12 Curved Bridge
- B.G.13 Maximum Bridge Height
- B.G.14 Sidehill Bridge
- B.G.15 Irregular Deck Area
- B.G.16 Calculated Deck Area

B.G.16 is calculated by FHWA using other SNBI data items and is not reported by the submitting agency. Preserve it as a calculated FHWA output, not a source-reported geometry observation.

### 4.2 Condition items

FHWA SNBI specification lists:
- B.C.01 Deck Condition Rating
- B.C.02 Superstructure Condition Rating
- B.C.03 Substructure Condition Rating
- B.C.04 Culvert Condition Rating
- B.C.05 Bridge Railing Condition Rating
- B.C.06 Bridge Railing Transitions Condition Rating
- B.C.07 Bridge Bearings Condition Rating
- B.C.08 Bridge Joints Condition Rating
- B.C.09 Channel Condition Rating
- B.C.10 Channel Protection Condition Rating
- B.C.11 Scour Condition Rating
- B.C.12 Bridge Condition Classification
- B.C.13 Lowest Condition Rating Code
- B.C.14 NSTM Inspection Condition
- B.C.15 Underwater Inspection Condition

B.C.12 and B.C.13 are calculated by FHWA from other items and are not intended to be reported by inspectors or agency personnel. Treat them as calculated outputs with provenance.

Condition ratings are based on type, location, severity, extent, and effect on strength/performance. They are not simple continuous measures of physical damage.

### 4.3 Location / identity items confirmed in validation logic

Current FHWA validation logic identifies:
- B.ID.01 Bridge Number;
- B.ID.02 Bridge Name;
- B.ID.03 Previous Bridge Number;
- B.L.01 State Code;
- B.L.02 County Code;
- B.L.03 Place Code;
- B.L.04 Highway Agency District;
- B.L.05 Latitude;
- B.L.06 Longitude;
- B.L.07 Border Bridge Number;
- B.L.08 Border Bridge State or Country Code.

Validation requires B.ID.03 to have a value or 0 when no previous bridge number exists. Do not interpret the zero sentinel as an actual prior identifier. Preserve raw value and normalize it to a specific no-previous-number status.

### 4.4 Other SNBI IDs visible in FHWA validation logic

- B.RT.01 Route Designation
- B.RT.02 Route Number
- B.RT.03 Route Direction
- B.RT.04 Route Type
- B.RT.05 Service Type
- B.H.01 Functional Classification
- B.H.02 Urban Code
- B.H.03 NHS Designation
- B.H.04 National Highway Freight Network
- B.H.17 Bypass Detour Length
- B.H.18 Crossing Bridge Number
- B.LR.01 Design Load
- B.LR.02 Design Method
- B.LR.03 Load Rating Date
- B.LR.04 Load Rating Method
- B.LR.05 Inventory Load Rating Factor
- B.LR.06 Operating Load Rating Factor
- B.AP.01 Approach Roadway Alignment
- B.AP.02 Overtopping Likelihood
- B.AP.03 Scour Vulnerability
- B.AP.04 Scour Plan of Action

Use the current validation workbook for allowed values, conditional requirements, and critical/error/flag classification. This list is not a substitute for the full SNBI item catalogue.

## 5. Transition-year temporary codes and nulls

FHWA's current validation logic page is version 1.2, updated 2026-09-16. It states:
- 2026 and 2027 datasets may contain temporary codes and null values for items not collected under the Coding Guide.
- Temporary codes are accepted in 2026 and 2027 for designated fields.
- Temporary codes are excluded from accepted values in 2028, when permanent SNBI codes are in effect.
- Validation distinguishes critical errors, general errors, and flags. Critical errors require correction and resubmission within 15 business days; general errors have different correction expectations; flags require review.

The code map is item-specific. Do not implement a global rule that any value ending in “-T” is valid without checking item, vintage, and current validation version.

Examples visible in FHWA validation table include temporary values for:
- B.SP.04 Span Material;
- B.SP.05 Span Continuity;
- B.SP.06 Span Type;
- B.SP.09 Deck Material and Type;
- B.RH.01 Bridge Railings;
- B.RH.02 Transitions;
- B.RT.03 Route Direction;
- B.H.01 Functional Classification;
- B.H.02 Urban Code;
- B.H.04 National Highway Freight Network;
- B.AP.02 Overtopping Likelihood;
- B.AP.03 Scour Vulnerability.

This is illustrative, not a complete temporary-code inventory. Acquire and parse the official Detailed Coding Map and current Validation Logic workbook for the complete machine-readable list.

## 6. 2026 dataset observation

FHWA's 2026 download landing page reports:
- displayed national total: 624,939 highway bridges;
- Guam did not submit 2026 data;
- state download formats include Excel, JSON, and GeoJSON;
- the all-highway-bridges Excel download is packaged as a ZIP due to Excel limitations.

This is a published aggregate and source-availability fact, not yet a row-level validation. Preserve the 2026 download vintage and checksums when acquired.

## 7. Parser design implications

### Legacy parser
- Build a year-versioned fixed-width parser.
- The current 445-character map is confirmed, not permission to apply it to all 1992–2025 records.
- Acquire and archive applicable Coding Guide versions, errata, record format revisions, and annual file notes.
- Treat positions 390–445 as download augmentation, not submitted fields.
- Keep fixed-width raw strings before numeric parsing.
- Handle subitems (28A/28B and 43A/43B) as separate normalized fields while retaining parent item structure.

### SNBI parser
- Parse JSON using the applicable published schema version.
- Preserve arrays and parent-child relationships for bridge, feature, route, span, and element datasets.
- Maintain separate bridge-level, feature-level, route-level, span-level, and element-level records with foreign keys.
- Store exact schema, SNBI specification, Errata No. 1 / No. 2, Data Crosswalk, Detailed Coding Map, and Validation Logic versions.
- Do not flatten one-to-many or many-to-one records into a single bridge row.

### Cross-era model
- Preserve original legacy values, transitioned values, and normalized model values as separate layers.
- For every mapped value, store transition status, source/destination item IDs, transformation rule, temporary-code status, and provenance.
- Do not backfill historical fields from later SNBI-only fields without marking them as derived or historically unavailable.

## 8. Remaining acquisition / verification work

This audit did not fully inspect the binary Excel workbooks. FHWA identifies:
- datacrosswalk.xlsx
- codemapping.xlsx
- current SNBI validation logic workbook v1.2 (2026-09-16)
- current SNBI specification with Errata No. 2 (2026-06-26)

The web retrieval surface exposed indexed tables but rejected direct XLSX downloads. The full spreadsheets still need acquisition and parsing in a file-capable environment.

Outstanding:
1. Retrieve exact 2026 state-level JSON / GeoJSON files and schema; inspect nested relationships.
2. Archive current SNBI specification PDF with Errata No. 2 and extract item definitions/units/precision.
3. Parse full Data Crosswalk and Detailed Coding Map workbooks into machine-readable tables.
4. Parse validation logic workbook v1.2 into item-specific rule tables.
5. Verify each legacy record layout era, including 432 vs 445 characters and intermediate revisions.
6. Reproduce FHWA's 2026 total from acquired records and reconcile coverage, submissions, and exclusions.
7. Resolve exact mappings for inspection, scour, load rating, work history, and safety fields before implementation.

## 9. Official FHWA references

Reviewed 2026-11-26.

1. FHWA, [NBI Record Format](https://www.fhwa.dot.gov/bridge/nbi/format.cfm) — 445-character format and field positions; identifies download-only appended fields.
2. FHWA, [Download NBI ASCII Files](https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm) — 2025 final legacy ASCII year and transition explanation.
3. FHWA, [2025 NBI ASCII Data](https://www.fhwa.dot.gov/bridge/nbi/ascii2025.cfm) — final legacy annual data page and download formats.
4. FHWA, [Data Crosswalk](https://www.fhwa.dot.gov/bridge/snbi/datacrosswalk.cfm) — legacy-to-SNBI mapping and transition notes.
5. FHWA, [Detailed Code Mapping](https://www.fhwa.dot.gov/bridge/snbi/codemapping.cfm) — item-specific code transitions.
6. FHWA, [SNBI Data Validation Logic v1.2](https://www.fhwa.dot.gov/bridge/snbi/data_validation_logic.cfm) — transition codes, null handling, validation rules.
7. FHWA, [SNBI Library](https://www.fhwa.dot.gov/bridge/nbi/library.cfm) — Errata No. 2 dated 2026-06-26, Errata No. 1, base specification.
8. FHWA, [SNBI Specifications](https://www.fhwa.dot.gov/bridge/snbi/snbi_march_2022_publication.pdf) — geometry and condition item definitions.
9. FHWA, [2026 NBI Data Download](https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm) — 2026 formats and displayed inventory totals.

## 10. Audit conclusion

The field dictionary can now be tightened for the legacy fixed-width format, core identity/location mappings, geometry, and condition item families. It is not yet safe to write a complete cross-era production parser because the full Excel crosswalk/code-map workbooks, current Errata No. 2 PDF, and year-specific historical record layouts still require direct acquisition and parsing.

Do not label the dictionary complete. The next milestone is acquisition and machine-readable extraction of official FHWA workbooks and current 2026 data schema.
