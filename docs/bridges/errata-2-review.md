# SNBI Errata No. 2 Review — 2026-11-26

## Source acquired
FHWA, *Specifications for the National Bridge Inventory with errata #2 - June 2026*, Publication No. FHWA-HIF-22-017:
https://www.fhwa.dot.gov/bridge/snbi/errata2_to_snbi_march_2022_publication.pdf

372-page PDF opened and text inspected through the web document reader.

## Critical legal/status distinction
The notice on page 1 states that Errata No. 2 contains redlined revisions to Errata No. 1. FHWA intends to address the Errata No. 2 revisions and Errata No. 1 revisions by a future rulemaking action. The redlined text is provided for information and **does not constitute official changes to the March 2022 SNBI currently**.

Therefore:
- Errata No. 2 is an official FHWA-published document, but its redlined proposed revisions are not currently official SNBI changes.
- Do not apply Errata No. 2 redlines as binding parser validation rules unless FHWA separately implements them through an authoritative mechanism.
- Maintain distinct rule versions: current operative SNBI specification, Errata No. 1 status, Errata No. 2 proposed redline, transition-year schema, and validation-logic release.
- Any model field definition or measurement rule derived from Errata No. 2 must be labeled proposed/pending, not current requirement.

## Confirmed example: NBIS Bridge Length (B.G.01)
The Errata No. 2 redline on PDF page 121 (printed page 103) states:
- Report NBIS bridge length to nearest tenth of a foot measured along roadway centerline.
- Measurements greater than 20.00 feet and less than 20.10 feet round up to 20.1 feet.

The same rounding language appears in the B.G.02 Total Bridge Length section (PDF page 124 / printed page 106).

Context:
- FHWA's earlier schema/validation update memorandum explains the issue: the 6.1 m legacy threshold converts to 20.01 ft, which rounds to 20.0 ft under ordinary nearest-tenth rounding. That creates ambiguity against the NBIS definition requiring more than 20 feet.
- The memorandum recommended transitional reporting of 20.1 feet for legacy 6.1 m records until field measurement.
- Errata No. 2 redline provides the explicit >20.00 and <20.10 ft rounding instruction, but its own notice says this redline is not currently an official change.

Source for the background memorandum:
https://www.fhwa.dot.gov/bridge/pubs/Memo-SNBI_Updates_Schema_ValidationLogic_NBISBridgeLength.pdf

## Confirmed identification rule: Previous Bridge Number (B.ID.03)
The consolidated Errata No. 2 PDF text states:
- Format AN(30015)
- Multiple previous bridge numbers may be reported, separated by pipe delimiters.
- Report 0 if no previous bridge number.
- Purpose is to retain links to previous bridge numbers associated with the bridge in the NBI.
- Example: when two separately numbered parallel bridges are reconstructed into one, report both previous numbers separated by a pipe.

Implementation implication:
- Do not normalize B.ID.03 as a single scalar predecessor ID.
- Preserve the raw string and parse it into a one-to-many predecessor link table only after validating the pipe-delimited semantics.
- Preserve 0 as the no-previous-bridge sentinel in raw data; derive a semantic state separately.
- Because this is read from the consolidated errata document, verify the current operative status of the specific wording before treating it as a new binding rule; the document's front notice applies to Errata No. 2 redlines.

## Other scope reviewed
The document's table of contents confirms the complete SNBI data organization: Bridge Identification; Bridge Material and Type; Bridge Geometry; Features; Loads, Load Rating, and Posting; Inspections; and Bridge Condition. It also contains comprehensive example data sets, item indexes, and component condition rating guidance. This supports the relational ingestion architecture already specified, but the actual JSON schema still needs to be acquired and tested against the public download.

## Parser and model safeguards
1. Maintain specification_version, schema_version, validation_logic_version, and errata_status as separate metadata.
2. Treat Errata No. 2 as a proposed redline in the current audit; do not silently merge it into operative rules.
3. Keep bridge length raw value, reported value, measurement method, source rule version, and any rounding transformation separately.
4. Treat B.ID.03 as a delimited history field capable of multiple prior IDs, not a simple one-to-one predecessor.
5. Separate NBIS inclusion threshold and physical measured length from reported rounded length; do not let a reporting-rounding convention create a false physical asset entry/exit.
6. Use the current official validation logic for acceptance tests, not proposed redline text.

## Evidence status
- **Directly inspected:** Errata No. 2 PDF, 372 pages; notice/status language; B.G.01 and B.G.02 rounding text; B.ID.03 format and multi-ID pipe-delimited description.
- **Source-reported:** FHWA says Errata No. 2 redlines are informational and not official changes currently.
- **Not yet completed:** Full page-by-page diff of Errata No. 2 against the 2022 base specification and Errata No. 1; exact status of every redlined item; acquisition of the JSON schema file and complete 2026 state data.
- **Next step:** Diff the entire Errata No. 2 against Errata No. 1/base SNBI and classify every changed item as operative unchanged text, Errata No. 1, or proposed Errata No. 2 redline.

Internal research record only; not approved for publication.
