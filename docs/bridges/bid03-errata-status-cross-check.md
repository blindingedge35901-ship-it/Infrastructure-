# SNBI Errata Status Cross-Check: BID03 and Identifier Continuity

Date: 2026-11-26

## Purpose
Cross-check the Errata No. 2 redline for B.ID.03 against the March 2022 SNBI, Errata No. 1, current FHWA validation logic, and the published Data Crosswalk.

## Current operative validation logic
FHWA SNBI Data Validation Logic, Version 1.2 (updated 2026-09-16), currently specifies:
- BID03 Previous Bridge Number must not be null; report 0 if there is no previous bridge number.
- Maximum length: 15 characters.
- Character restrictions: letters, digits, spaces, periods, and specified symbols.
- A flag is raised if BID03 equals BID01.

Source: https://www.fhwa.dot.gov/bridge/snbi/data_validation_logic.cfm

## March 2022 SNBI and Errata No. 1
The base SNBI specifies B.ID.03 Previous Bridge Number as AN(15). It instructs agencies to report the previous bridge number when a bridge number changes. Errata No. 1's displayed B.ID.01 text continues to direct agencies to report the previous bridge number under B.ID.03; it does not establish the multi-predecessor, pipe-delimited expansion in the redline text reviewed here.

Sources:
- https://www.fhwa.dot.gov/bridge/snbi/snbi_march_2022_publication.pdf
- https://www.fhwa.dot.gov/bridge/snbi/errata1_to_snbi_march_2022_publication.pdf

## Errata No. 2 redline
The June 2026 Errata No. 2 redline describes B.ID.03 as a much longer alphanumeric field (format shown as AN(30015)) and permits multiple previous bridge numbers separated by pipe delimiters. It describes using this to preserve multiple predecessor identities, such as two separately numbered parallel bridges reconstructed into one.

Source:
- https://www.fhwa.dot.gov/bridge/snbi/errata2_to_snbi_march_2022_publication.pdf

The Errata No. 2 document's front notice says its redlined revisions are informational and do not constitute official changes to the March 2022 SNBI currently. FHWA says it intends to address these revisions through future rulemaking.

## Crosswalk treatment of historical identifiers
FHWA's Data Crosswalk maps legacy Item 8 Structure Number to B.ID.01 Bridge Number. Its transition note instructs developers to trim leading/trailing spaces and provide an option for handling leading zeros (trim, or trim all but one leading zero), but **not to provide a default selection**. It also says all legacy data must be preserved in original form. The crosswalk maps B.ID.03 as populated from NBI Structure Number Change history.

Source:
- https://www.fhwa.dot.gov/bridge/snbi/datacrosswalk.cfm

## Implementation decision
For the current 2026 production parser and validator:
1. Implement BID03 according to the current validation logic: preserve raw value, maximum 15 characters, item-specific character validation, and explicit 0 sentinel handling.
2. Do not split BID03 on pipe or accept 300-character values as current-valid unless a later authoritative FHWA release changes the operative validation rules.
3. Add a forward-compatible parser design so a future version can support multiple predecessor IDs if/when the proposed Errata No. 2 change becomes operative.
4. Keep `bridge_identity_link` capable of multiple predecessor/successor links as an internal model capability, but do not infer that current BID03 values encode multiple predecessors.
5. Preserve raw legacy identifiers exactly. Any leading-zero normalization must be an explicit state/agency-level migration decision, not a default transformation.
6. Version the specification, schema, validation logic, and proposed errata separately.

## Evidence classification
- **Current validation rule:** BID03 maximum 15 characters; 0 if no previous number.
- **Base specification:** B.ID.03 AN(15).
- **Crosswalk instruction:** legacy leading-zero treatment is a user-selected migration option with no default; preserve original values.
- **Proposed Errata No. 2 redline:** multi-number pipe-delimited previous bridge numbers and longer field format; not currently an official change according to the document's notice.
- **Model design inference:** internal identity graph should support one-to-many lineage, because physical replacement/merger histories can be more complex than one-to-one. This is a model capability, not a claim that current BID03 supports it.

Internal research only; not approved for publication.
