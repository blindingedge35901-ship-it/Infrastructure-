# Independent NBI Republish Candidate — Bridge Report Card (2025)

**Audit date:** 2026-11-27  
**Purpose:** Identify a free, independently accessible secondary copy of selected FHWA NBI data for cross-checking and potential parser smoke tests.  
**Status:** Candidate only. Not an authoritative replacement for FHWA source files; no CSV bytes have yet been retrieved or parsed.

## Source and stated lineage

Bridge Report Card's data-download page describes its material as the 2025 National Bridge Inventory, compiled August 20, 2026. It states that its per-state CSVs contain the complete 2025 inventory for each state, with a selected set of fields, and that its source is FHWA's 2025 per-state NBI files. Its methodology page says the Good/Fair/Poor class is FHWA's computed field, not a classification independently created by the site. The site explicitly says it is not affiliated with a government agency.

- Landing page: https://bridgereportcard.com/data/
- Methodology: https://bridgereportcard.com/about/
- Colorado state page: https://bridgereportcard.com/state/colorado/
- Published state-file naming convention: `bridges-<state>.csv`; the page lists CO among the state links.
- Data page describes free CSVs and no sign-up; the site requests attribution.

## Potentially useful files

The page lists:
- `bridge-conditions-by-state.csv` and `bridge-conditions-by-county.csv`: aggregate condition counts.
- `poor-bridges.csv`: all poor-rated bridges, selected fields.
- `closed-and-posted-bridges.csv`: closed, load-posted, or temporary-measure records.
- `condition-changes-2024-2025.csv`: records whose class, component ratings, or status changed, matched by state plus structure number.
- `bridges-<state>.csv`: selected fields for every bridge in the 2025 state inventory.

The per-state field list includes state, county, structure number, facility, feature, location, year built/reconstructed, ADT and ADT year, FHWA condition class, deck/superstructure/substructure/culvert ratings, structure kind/type, length, owner code, coordinates, load status, last inspection month, inspection interval, scour code, fracture-critical flag, and prior condition.

## What this could support

If the files can be retrieved and their contents inspected, they may support:
1. A secondary-source parser smoke test on a state-level bridge table.
2. A record-level cross-check of selected 2025 Colorado observations and selected aggregate counts.
3. A preliminary test of the site's stated 2024–2025 matching rule (state + structure number), with explicit warning that this is not an FHWA-certified identity crosswalk.
4. A way to test downstream data-quality and reporting logic while the complete FHWA source archive remains inaccessible from this runtime.

The republished table is a selected-field derivative, not a complete raw NBI record. It cannot validate the 445-character FHWA record parser, reconstruct all NBI items, establish historical identity continuity, or substitute for the full official annual source files.

## Reconciliation flags — do not silently harmonize

The Bridge Report Card homepage reports 624,169 total bridges for 2025 and 41,677 poor bridges. Its methodology says figures are derived from FHWA's 2025 per-state files. The FHWA 2025 condition baseline already recorded in this repository is 624,193 total bridges and 41,685 poor bridges. This yields differences of 24 total records and 8 poor records.

These discrepancies may reflect different source extracts, filtering, revisions, or compilation logic. Their cause is not established by the pages reviewed. Retain both source-reported totals and investigate against the actual FHWA files; do not replace the official baseline or treat the third-party count as corrected.

The Colorado state page reports 8,990 bridges and 417 poor. The FHWA 2025 published state table also reports 8,990 Colorado bridges. The matching total is a useful consistency check, not proof that every record or field matches.

## Retrieval test and limitations

On 2026-11-27, the web page was inspected and its CSV link structure was confirmed. The web retrieval service rejected CSV responses as an unsupported content type. A direct runtime download attempt of the Colorado CSV also failed. Therefore:
- No CSV bytes were acquired.
- No file hash, row count, header inspection, or record-level comparison was performed.
- No real-data parser test was run.
- The candidate remains a research lead, not a completed acquisition.

## Decision

Keep the official FHWA files as the primary source of record. Retain Bridge Report Card as a potentially useful, free secondary validation source if a supported retrieval path becomes available. Any use in tests must label the source as a third-party FHWA-derived republish, preserve its compilation date and URL, and keep discrepancies visible.
