# SNBI JSON Schema Version Audit — 2026-11-26

## Official schema page
FHWA NBI Submittal File Schema:
https://www.fhwa.dot.gov/bridge/snbi/schema.cfm

FHWA describes this schema as the organization/file structure for the March 15, 2026 NBI data submittal and future submittals. It is JSON, uses attribute-value pairs and arrays to represent relationships, and supports inventory and element data in a single submittal.

However, the schema artifact linked on the page is dated **July 18, 2024**, and the example submittal data file is dated **February 26, 2025**. FHWA's page says the 2024 schema revision accommodated SNBI Errata No. 1 and transition temporary codes. It also says a new schema will be published in advance of the 2028 submittal, when temporary codes are no longer allowed.

This means the page does not currently establish that a newly revised 2026 schema artifact exists. The 2024 schema is explicitly the schema FHWA identifies for the 2026 transition period, but the current public 2026 data must still be checked against it and against later Errata No. 2.

## Confirmed schema field-length changes

### Errata No. 1-related changes
| Item | Tag | Existing format | 2026–27 schema format | Name |
|---|---|---|---|---|
| B.EP.01 | BEP01 | AN(3) | AN(15) | Legal Load Configuration |
| B.EP.03 | BEP03 | AN(1) | AN(17) | Posting Type |
| B.EP.04 | BEP04 | N(2,0) | AN(15) | Posting Value |

### Transition-code length changes
| Item | Tag | Original format | 2026–27 format | Name |
|---|---|---|---|---|
| B.SP.04 | BSP04 | AN(3) | AN(4) | Span Material |
| B.SP.05 | BSP05 | AN(1) | AN(3) | Span Continuity |
| B.SP.06 | BSP06 | AN(3) | AN(4) | Span Type |
| B.SP.09 | BSP09 | AN(3) | AN(4) | Deck Material and Type |
| B.SP.11 | BSP11 | AN(3) | AN(4) | Deck Protective System |
| B.RT.03 | BRT03 | AN(2) | AN(3) | Route Direction |
| B.H.01 | BH01 | AN(1) | AN(3) | Functional Classification |
| B.H.04 | BH04 | AN(1) | AN(3) | National Highway Freight Network |
| B.N.06 | BN06 | AN(1) | AN(3) | Substructure Navigation Protection |
| B.PS.01 | BPS01 | AN(2) | AN(4) | Load Posting Status |
| B.C.11 | BC11 | AN(1) | AN(4) | Scour Condition Rating |
| B.AP.02 | BAP02 | AN(1) | AN(5) | Overtopping Likelihood |
| B.AP.03 | BAP03 | AN(1) | AN(5) | Scour Vulnerability |
| B.AP.04 | BAP04 | AN(1) | AN(3) | Scour Plan of Action |

FHWA states these expanded lengths revert to the original SNBI formats beginning with the 2028 data submittal.

## Implementation consequences

1. Schema validation must be version-aware: 2026–27 transition formats differ from permanent SNBI formats.
2. Do not impose original SNBI field lengths on 2026–27 values.
3. Do not assume every field's accepted temporary codes are determined solely by string length or suffix.
4. Preserve raw source values, field tag, inventory year, schema revision, and validation-logic revision.
5. Keep schema validation and data validation separate. A value may fit the JSON schema but fail a field-specific business rule; conversely, a value accepted during transition may be disallowed from 2028.
6. Before parser release, compare the 2026 DC sample and a larger state file against the 2024 schema artifact and Errata No. 1/No. 2.

## Errata No. 2 status
FHWA's NBI Library lists “Errata Number 2 Specifications for the National Bridge Inventory” dated June 26, 2026:
https://www.fhwa.dot.gov/bridge/nbi/library.cfm

The document's direct PDF URL and text have not yet been retrieved in this work session. Do not infer its contents or assume it is merely editorial. Retrieval and comparison against the SNBI base specification and Errata No. 1 remain an explicit gate.

## Evidence status
- **Source-reported:** Schema purpose, schema/example dates, 2024 transition changes, exact field-length table, and planned 2028 schema revision.
- **Not established:** Direct validation of 2026 state files against the published schema, contents of Errata No. 2, or existence of any later schema artifact not listed on the page.
- **Next step:** Obtain the actual schema JSON, example file, Errata No. 2 PDF, and complete state JSON file; validate and report all mismatches.

Internal research record only; not approved for publication.
