# SNBI Detailed Code Mapping: Supplemental Structural and Material Mapping Findings

**Status:** Targeted supplemental review of FHWA's current Detailed Code Mapping page.  
**Research date:** 2026-11-26  
**Source:** https://www.fhwa.dot.gov/bridge/snbi/codemapping.cfm

## Purpose

This supplement records additional detailed mapping findings not fully covered in the semantic-loss audit. It is not a full transcription of codemapping.xlsx.

## 1. FHWA transition assumptions affect record structure

FHWA's Detailed Coding Map general notes state that the legacy Coding Guide does not identify every situation where multiple instances of a feature type (highway, railroad, etc.) are carried on or below a bridge. The transition therefore assumes:
- one instance of a given feature type;
- one route per highway;
- one main span set;
- one approach span set.

FHWA explicitly says these assumptions will be correct in many cases but should be adjusted after transition where they do not apply.

The notes also state:
- values not specified in the mapping result in null;
- temporary codes are marked by the suffix "-T", "TEMP" in the description, and an asterisk in the TEMP column;
- the description identifies possible permanent codes represented by a temporary code.

**Model implication:** The transition may simplify many-to-one and one-to-many relationships. Do not treat transitioned feature/route/span arrays as complete historical topology. Keep a transition-structure assumption flag and test actual post-transition records for additional features, routes, and span sets.

## 2. Span configuration and span type are separate items

FHWA maps legacy Items 43B/44B into several SNBI span concepts. Examples:
- B.SP.01 Span Configuration Designation: legacy Item 43B = 19 maps to culvert configuration C01; when Item 44B is nonzero, C02 may also be created. Other legacy values map to main span M01 and, where approach spans exist, A01.
- B.SP.04 Span Material: legacy 43A/44A values 1 or 2 map to temporary CR-T (reinforced concrete alternatives C01/C02/CX); 3 or 4 to S-T (steel alternatives); 5 or 6 to CP-T (prestressed concrete alternatives); 7 to T-T (timber alternatives); 8 to M-T (masonry alternatives); 9 to AI-T (aluminum or iron alternatives); 0 to X-T (other).
- B.SP.05 Span Continuity: legacy values can map to simple/single span, continuous, frame, buried, or temporary grouped categories, depending on Items 43A/44A and 43B/44B.
- B.SP.06 Span Type: legacy values map to specific permanent types only where the legacy code is sufficiently specific; otherwise temporary codes represent candidate permanent subtypes.

**Model implication:** Do not conflate span configuration, span material, span continuity, and span type. They describe different aspects of bridge structure. Store each at the span-set or span level where supported by SNBI structure.

## 3. Deck system fields depend on multiple legacy inputs

FHWA's detailed mapping shows:
- B.SP.09 Deck Material and Type uses legacy Item 107 and, for one steel case, Items 43B/44B. Item 107 = 5 maps to S04 only when 43B/44B = 08; otherwise it maps to temporary S-T (S03 or S04).
- B.SP.10 Wearing Surface uses Item 108A and, in combination with Item 107, may be blank when the deck material is not reported. Temporary codes are used for some concrete additive, polymer, and other categories.
- B.SP.11 Deck Protective System uses Items 108B and 108C; combinations distinguish membrane, admixture, coating, and other states. Some combinations yield temporary MX-T or no value.
- B.SP.12 Deck Reinforcing Protective System uses Item 108C; selected legacy values map to C01, C02, temporary C-T, S-T, or X-T.

**Model implication:** These deck attributes are not independent single-field conversions. Implement explicit multi-input mapping rules with tests for each combination and retain all source inputs. Avoid filling a missing deck system item from another deck field unless the official mapping rule explicitly instructs it.

## 4. Historic significance and ownership examples

Selected mappings:
- B.CL.04 Historic Significance: legacy Item 37 values 1 and 2 map to National Register / eligible; value 3 maps to temporary T representing several possible permanent codes; value 4 maps to code 7 (not determined).
- B.CL.01 Owner and B.CL.02 Maintenance Responsibility map legacy Items 22 and 21 respectively through code tables. The target SNBI values are alphanumeric responsibility categories, not simple numeric labels.
- B.CL.03 Federal or Tribal Land Access: legacy Item 105 maps to one or multiple land-agency designations; the SNBI item supports multiple values.

**Model implication:** Use typed code-list tables, not numeric coercion. Preserve multi-value membership and the exact mapping source.

## 5. Navigation and load-rating fields

Selected examples:
- B.N.06 Substructure Navigation Protection: legacy Item 111 = 1 maps to temporary 1-T ("not required" alternatives 0 or 1); values 2–5 map to distinct permanent states.
- B.LR.01 Design Load: legacy Item 31 values map to codes such as H10, H15, HS15, H20, HS20, HS20M, RR, HS20Plus, HL93, HL93Plus, or X; legacy value 7 produces no value.
- B.LR.04 Load Rating Method: legacy Item 63 maps multiple old codes to LFR, ASR, LRFR, assigned rating AR, load testing LT, engineering judgment EJ, or N (no analysis/evaluation).

**Model implication:** Missing or unmapped values are not automatically equivalent to "not applicable" or "safe." Keep unknown, not reported, and source-defined no-analysis states distinct.

## 6. Crosswalk mapping and validation must be implemented together

The Detailed Coding Map defines the transformation, while FHWA's Validation Logic defines acceptable values and conditional constraints for the resulting SNBI items. For example, temporary codes may be accepted for selected items in 2026–2027 and excluded beginning in 2028. Conditional rules may also depend on feature type or other linked objects.

Implementation requirements:
1. Version the crosswalk mapping tables independently from the parser.
2. Version the SNBI schema independently from the crosswalk.
3. Version validation logic independently from both.
4. Record the effective submission years for each rule set.
5. Validate transformed outputs under the validation rules applicable to the submission vintage.
6. Preserve warnings and flags separately from parse errors and critical validation errors.

A record can be valid under a transition-year rule while remaining unsuitable for a fully comparable long-term trend. Validation acceptance is not evidence of semantic equivalence.

## 7. Source limitations

The FHWA HTML page exposes many tables in indexed text, but its direct page view currently returns an internal error to the browser retrieval service. The downloadable Excel workbook is linked from the page but has not yet been acquired and parsed locally. Therefore this supplement is based on accessible published HTML/indexed table content, not a full workbook extraction or exhaustive item-by-item audit.

## Sources

1. FHWA, Detailed Code Mapping for Individual Data Items: https://www.fhwa.dot.gov/bridge/snbi/codemapping.cfm
2. FHWA, Data Crosswalk for "Over" Records and "Under" Records: https://www.fhwa.dot.gov/bridge/snbi/datacrosswalk.cfm
3. FHWA, Data Validation Logic: https://www.fhwa.dot.gov/bridge/snbi/data_validation_logic.cfm
4. FHWA, NBI Submittal File Schema: https://www.fhwa.dot.gov/bridge/snbi/schema.cfm

## Evidence classification

- **Source-reported:** Specific mappings and transition assumptions listed above.
- **Derived:** Transition assumptions can reduce historical topology detail and make some attributes dependent on multiple legacy fields.
- **Model recommendation:** Keep schema, mapping, and validation versions separate; preserve source inputs and ambiguity.
- **Outstanding:** Full Excel workbook acquisition and automated extraction/test coverage.
