# 2026 SNBI Data Acquisition Test — 2026-11-26

## Purpose
Test whether the first SNBI-era public National Bridge Inventory release can be acquired as real JSON records for parser development.

## Official release facts
FHWA's 2026 download page lists state-level Excel, JSON, and GeoJSON downloads and reports 624,939 public highway bridges nationally. It lists Colorado at 9,018 bridges and states Guam did not submit 2026 data.

Sources:
- https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm
- https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm

FHWA's general download page states that 2026 and 2027 are transition years to SNBI; the data may contain temporary codes and null values. The 2025 ASCII release is the final Coding Guide-format year. Historical 1992–2025 files remain in ASCII format.

## Schema facts
FHWA's NBI Submittal File Schema page states that the JSON schema applies to the March 15, 2026 submittal and future submittals. It describes attribute-value pairs and arrays for one-to-many SNBI relationships, and says the format supports combining inventory and element data in a single submittal.

Schema page:
- https://www.fhwa.dot.gov/bridge/snbi/schema.cfm

The page identifies a schema updated 2024-07-18 and an example submittal data file updated 2025-02-26. The 2024 schema revision accommodates SNBI Errata #1 and transition temporary codes. This does not establish that the public 2026 download exactly matches a particular schema revision; that must be checked against the actual file and current errata.

## Acquisition test
The 2026 state JSON download URL pattern is exposed by FHWA's download page. A direct request was tested for Colorado:

- https://www.fhwa.dot.gov/bridge/nbi/2026/JSON/CO26.json

The web retrieval service rejected the Colorado file because its response was 27,760,308 bytes, exceeding its content-length limit. A direct runtime download attempt could not resolve the FHWA host due to a DNS/network restriction in that execution environment. A smaller District of Columbia endpoint test did not return usable content through the web retrieval service. Therefore no JSON records were actually acquired, parsed, or validated in this work session.

The Colorado URL is an acquisition endpoint tested for existence/size behavior, not a claim that its contents have been inspected.

## Consequences for implementation
Do not yet write or claim a tested production parser. The actual public JSON data structure, compact field names, nested collection shapes, null conventions, temporary-code values, and consistency with the current schema/errata remain to be inspected.

Recommended next acquisition route:
1. Download one small jurisdiction file (e.g. District of Columbia) or a single-state file through a normal browser or a runtime with working FHWA network access.
2. Preserve the original bytes and register URL, retrieval timestamp, file size, checksum, and inventory year.
3. Parse the JSON without flattening nested arrays.
4. Compare keys, types, required fields, nulls, and nested arrays with the current FHWA schema and Errata No. 1/2.
5. Only then implement and test the SNBI ingestion adapter; keep it separate from the legacy fixed-width ASCII adapter.

## Evidence status
- **Source-reported:** 2026 state counts, national total, download formats, transition-year warnings, schema description and publication dates.
- **Directly tested:** Colorado JSON endpoint responds with a 27,760,308-byte payload that exceeds the web retrieval service's limit.
- **Not inspected:** Actual 2026 JSON record content, DC file, schema file contents, current Errata No. 2 document.
- **Not established:** Parser correctness, nationwide file integrity, or exact schema-to-public-download conformity.

Internal research record only; not approved for publication.
