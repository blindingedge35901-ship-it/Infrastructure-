"""Conservative bridge identity and longitudinal-observation utilities.

These functions implement data-governance rules, not a calibrated deterioration
model. They intentionally avoid inferring physical identity or inspection links
from weak temporal or identifier evidence.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import date
from typing import Any, Iterable


class ValidationError(ValueError):
    """Raised when a source value violates a documented structural rule."""


def preserve_structure_number(value: Any) -> str | None:
    """Return an identifier as text; never strip leading zeroes or coerce to int."""
    if value is None:
        return None
    text = str(value)
    return text if text.strip() else None


def normalize_previous_bridge_number(value: Any, *, max_length: int = 15) -> str | None:
    """Normalize current SNBI BID03 semantics while preserving raw data elsewhere.

    A source value of '0' means no previous bridge number. Other identifiers
    remain strings. The caller must retain the original token in raw provenance.
    """
    text = preserve_structure_number(value)
    if text is None:
        raise ValidationError("BID03 must be present; use '0' when no previous number exists")
    if text == "0":
        return None
    if len(text) > max_length:
        raise ValidationError(f"previous bridge number exceeds {max_length} characters")
    return text


def component_rating_state(value: Any, *, transition_year: bool = False) -> tuple[str, Any]:
    """Classify a component rating without conflating zero, N, null, or temp codes."""
    if value is None or (isinstance(value, str) and value.strip() == ""):
        return ("MISSING", None)
    if isinstance(value, str):
        token = value.strip()
        if token.upper() == "N":
            return ("NOT_APPLICABLE", "N")
        if token.upper().endswith("-T"):
            if transition_year:
                return ("TEMPORARY_TRANSITION_CODE", token)
            return ("INVALID_TEMPORARY_CODE", token)
        if token.isdigit():
            number = int(token)
        else:
            return ("INVALID", token)
    elif isinstance(value, int) and not isinstance(value, bool):
        number = value
    else:
        return ("INVALID", value)
    if 0 <= number <= 9:
        return ("RATING", number)
    return ("INVALID", number)


def identity_link(
    predecessor_id: str,
    successor_id: str,
    *,
    relationship: str,
    evidence: Iterable[str],
    source: str,
    confidence: str = "UNASSESSED",
) -> dict[str, Any]:
    """Create an explicit identity-link record; never merge assets automatically."""
    allowed = {
        "RENUMBERED", "REPLACED", "PARTIALLY_RETAINED", "SPLIT", "MERGED",
        "JURISDICTION_TRANSFER", "CANDIDATE_ONLY", "UNRESOLVED",
    }
    if relationship not in allowed:
        raise ValidationError(f"unsupported identity relationship: {relationship}")
    if not predecessor_id or not successor_id:
        raise ValidationError("both source identifiers are required")
    if predecessor_id == successor_id and relationship in {"REPLACED", "RENUMBERED"}:
        raise ValidationError("replacement/renumbering requires distinct source identifiers")
    return {
        "predecessor_source_id": preserve_structure_number(predecessor_id),
        "successor_source_id": preserve_structure_number(successor_id),
        "relationship": relationship,
        "evidence": sorted(set(evidence)),
        "source": source,
        "confidence": confidence,
        "automatic_asset_merge": False,
    }


def deduplicate_legacy_inspection_events(
    records: Iterable[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Deduplicate reconstructed legacy events by asset, type, and MMYY.

    Repeated source appearances are retained in source_appearances. For a
    repeated event, the record with the lexically latest source_vintage is
    selected as the representative, matching the documented 'most recent data
    for a single date' transition rule. MMYY remains month precision; no day
    is invented here.
    """
    groups: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        asset = record.get("canonical_asset_id")
        event_type = record.get("inspection_type")
        month = record.get("inspection_month")
        if not all((asset, event_type, month)):
            raise ValidationError("asset, inspection_type, and inspection_month are required")
        if len(month) != 4 or not month.isdigit():
            raise ValidationError("inspection_month must be MMYY")
        mm = int(month[:2])
        if not 1 <= mm <= 12:
            raise ValidationError("inspection_month has invalid month")
        groups[(asset, event_type, month)].append(dict(record))

    output = []
    for key, group in sorted(groups.items()):
        chosen = max(group, key=lambda row: str(row.get("source_vintage", "")))
        chosen["source_appearances"] = [
            {
                "source_vintage": row.get("source_vintage"),
                "source_structure_number": preserve_structure_number(row.get("source_structure_number")),
            }
            for row in sorted(group, key=lambda row: str(row.get("source_vintage", "")))
        ]
        chosen["date_precision"] = "MONTH"
        chosen["day_01_is_proxy"] = True
        output.append(chosen)
    return output


def associate_condition_to_inspection(
    condition_observation_id: str,
    inspection_event_ids: Iterable[str],
    *,
    association_type: str = "AMBIGUOUS",
    evidence: Iterable[str] = (),
    confidence: str = "UNASSESSED",
) -> dict[str, Any]:
    """Represent zero, one, or many candidate event links without forcing one-to-one."""
    allowed = {"EXPLICIT", "SOURCE_MAPPED", "TEMPORAL_CANDIDATE", "AMBIGUOUS", "NO_LINK"}
    if association_type not in allowed:
        raise ValidationError(f"unsupported association type: {association_type}")
    event_ids = list(dict.fromkeys(inspection_event_ids))
    if association_type == "NO_LINK" and event_ids:
        raise ValidationError("NO_LINK association cannot contain inspection event IDs")
    if association_type in {"EXPLICIT", "SOURCE_MAPPED"} and len(event_ids) != 1:
        raise ValidationError("explicit/source-mapped association requires exactly one event")
    return {
        "condition_observation_id": condition_observation_id,
        "inspection_event_ids": event_ids,
        "association_type": association_type,
        "evidence": sorted(set(evidence)),
        "confidence": confidence,
    }


def reconcile_element_quantities(
    total_quantity: Any,
    condition_state_quantities: Iterable[Any],
) -> bool:
    """Check integer total equals the sum of CS1-CS4 quantities."""
    values = [total_quantity, *list(condition_state_quantities)]
    if len(values) != 5:
        raise ValidationError("exactly four condition-state quantities are required")
    if any(isinstance(v, bool) or not isinstance(v, int) for v in values):
        raise ValidationError("element quantities must be whole-number integers")
    if total_quantity <= 0 or any(v < 0 for v in values[1:]):
        raise ValidationError("total must be positive and state quantities nonnegative")
    return total_quantity == sum(values[1:])


def training_eligibility(
    *,
    identity_status: str,
    timing_basis: str,
    measurement_status: str,
    unresolved_identity_conflict: bool = False,
) -> tuple[str, list[str]]:
    """Return A/B/C cohort status and reproducible reasons."""
    reasons: list[str] = []
    if unresolved_identity_conflict or identity_status in {"UNRESOLVED", "COLLISION"}:
        return "C", ["unresolved_or_conflicting_identity"]
    if identity_status not in {"CONFIRMED", "BOUNDED_CANDIDATE"}:
        return "C", ["identity_status_not_admissible"]
    if measurement_status != "COMPATIBLE":
        return "C", ["measurement_semantics_unresolved_or_incompatible"]
    if timing_basis == "ACTUAL_INSPECTION_DATE":
        return "A", []
    if timing_basis in {"MONTH_PROXY", "VINTAGE_ONLY"}:
        reasons.append("timing_is_proxy_or_submission_vintage")
        return "B", reasons
    return "C", ["inspection_timing_unknown_or_invalid"]


def observation_key(
    canonical_asset_id: str,
    component_code: str,
    source_vintage: str,
    source_record_id: str,
) -> tuple[str, str, str, str]:
    """Build a source-observation key without pretending vintage is inspection time."""
    if not all((canonical_asset_id, component_code, source_vintage, source_record_id)):
        raise ValidationError("all observation-key fields are required")
    return canonical_asset_id, component_code, source_vintage, source_record_id
