import unittest

from infrastructure_model.bridges.longitudinal import (
    ValidationError,
    associate_condition_to_inspection,
    component_rating_state,
    deduplicate_legacy_inspection_events,
    identity_link,
    normalize_previous_bridge_number,
    observation_key,
    preserve_structure_number,
    reconcile_element_quantities,
    training_eligibility,
)


class TestIdentifiers(unittest.TestCase):
    def test_leading_zeroes_are_preserved(self):
        self.assertEqual(preserve_structure_number("0007"), "0007")
        self.assertNotEqual(preserve_structure_number("0007"), preserve_structure_number("7"))

    def test_none_and_blank_identifier(self):
        self.assertIsNone(preserve_structure_number(None))
        self.assertIsNone(preserve_structure_number("  "))

    def test_bid03_zero_means_no_predecessor(self):
        self.assertIsNone(normalize_previous_bridge_number("0"))

    def test_bid03_retains_previous_number_as_text(self):
        self.assertEqual(normalize_previous_bridge_number("000123"), "000123")

    def test_bid03_length_is_validated(self):
        with self.assertRaises(ValidationError):
            normalize_previous_bridge_number("X" * 16)


class TestComponentRatings(unittest.TestCase):
    def test_numeric_zero_is_a_valid_rating(self):
        self.assertEqual(component_rating_state(0), ("RATING", 0))

    def test_n_is_not_applicable_not_zero(self):
        self.assertEqual(component_rating_state("N"), ("NOT_APPLICABLE", "N"))

    def test_null_and_blank_are_missing(self):
        self.assertEqual(component_rating_state(None), ("MISSING", None))
        self.assertEqual(component_rating_state(" "), ("MISSING", None))

    def test_temporary_code_only_allowed_in_transition(self):
        self.assertEqual(component_rating_state("MI-T", transition_year=True)[0],
                         "TEMPORARY_TRANSITION_CODE")
        self.assertEqual(component_rating_state("MI-T")[0], "INVALID_TEMPORARY_CODE")

    def test_out_of_range_and_non_numeric_rejected(self):
        self.assertEqual(component_rating_state(10)[0], "INVALID")
        self.assertEqual(component_rating_state("unknown")[0], "INVALID")


class TestIdentityAndObservationLinks(unittest.TestCase):
    def test_identity_link_never_auto_merges(self):
        link = identity_link("OLD001", "NEW001", relationship="RENUMBERED",
                             evidence=["same location", "agency history"], source="test")
        self.assertFalse(link["automatic_asset_merge"])
        self.assertEqual(link["predecessor_source_id"], "OLD001")

    def test_same_id_cannot_be_called_replacement(self):
        with self.assertRaises(ValidationError):
            identity_link("A", "A", relationship="REPLACED", evidence=[], source="test")

    def test_unknown_relationship_rejected(self):
        with self.assertRaises(ValidationError):
            identity_link("A", "B", relationship="SAME_AS", evidence=[], source="test")

    def test_condition_can_link_to_multiple_candidate_inspections(self):
        link = associate_condition_to_inspection(
            "obs-1", ["insp-1", "insp-2"], association_type="AMBIGUOUS")
        self.assertEqual(len(link["inspection_event_ids"]), 2)

    def test_no_link_cannot_contain_events(self):
        with self.assertRaises(ValidationError):
            associate_condition_to_inspection("obs-1", ["insp-1"],
                                              association_type="NO_LINK")

    def test_explicit_link_requires_exactly_one_event(self):
        with self.assertRaises(ValidationError):
            associate_condition_to_inspection("obs-1", ["i1", "i2"],
                                              association_type="EXPLICIT")


class TestLegacyEventDeduplication(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {"canonical_asset_id": "asset-1", "inspection_type": "ROUTINE",
             "inspection_month": "0620", "source_vintage": "2020",
             "source_structure_number": "0001", "interval": 24},
            {"canonical_asset_id": "asset-1", "inspection_type": "ROUTINE",
             "inspection_month": "0620", "source_vintage": "2021",
             "source_structure_number": "0002", "interval": 12},
            {"canonical_asset_id": "asset-1", "inspection_type": "UNDERWATER",
             "inspection_month": "0620", "source_vintage": "2021",
             "source_structure_number": "0002", "interval": 60},
        ]

    def test_repeated_month_is_deduplicated_but_source_appearances_retained(self):
        result = deduplicate_legacy_inspection_events(self.rows)
        self.assertEqual(len(result), 2)
        routine = next(row for row in result if row["inspection_type"] == "ROUTINE")
        self.assertEqual(routine["source_vintage"], "2021")
        self.assertEqual(len(routine["source_appearances"]), 2)
        self.assertEqual(routine["date_precision"], "MONTH")
        self.assertTrue(routine["day_01_is_proxy"])

    def test_different_inspection_types_same_month_remain_separate(self):
        result = deduplicate_legacy_inspection_events(self.rows)
        self.assertEqual({r["inspection_type"] for r in result},
                         {"ROUTINE", "UNDERWATER"})

    def test_invalid_month_rejected(self):
        row = dict(self.rows[0], inspection_month="1320")
        with self.assertRaises(ValidationError):
            deduplicate_legacy_inspection_events([row])

    def test_missing_key_rejected(self):
        with self.assertRaises(ValidationError):
            deduplicate_legacy_inspection_events([{"canonical_asset_id": "a"}])


class TestElementAndTrainingGates(unittest.TestCase):
    def test_element_quantity_reconciles(self):
        self.assertTrue(reconcile_element_quantities(10, [2, 3, 4, 1]))

    def test_element_quantity_mismatch(self):
        self.assertFalse(reconcile_element_quantities(10, [2, 3, 4, 0]))

    def test_element_quantities_require_integers(self):
        with self.assertRaises(ValidationError):
            reconcile_element_quantities(10, [2, 3, 4, 1.0])

    def test_training_a_requires_supported_identity_time_and_measurement(self):
        self.assertEqual(training_eligibility(
            identity_status="CONFIRMED",
            timing_basis="ACTUAL_INSPECTION_DATE",
            measurement_status="COMPATIBLE"), ("A", []))

    def test_month_proxy_is_conditional(self):
        status, reasons = training_eligibility(
            identity_status="BOUNDED_CANDIDATE",
            timing_basis="MONTH_PROXY",
            measurement_status="COMPATIBLE")
        self.assertEqual(status, "B")
        self.assertIn("timing_is_proxy_or_submission_vintage", reasons)

    def test_identity_collision_excluded(self):
        status, reasons = training_eligibility(
            identity_status="COLLISION",
            timing_basis="ACTUAL_INSPECTION_DATE",
            measurement_status="COMPATIBLE")
        self.assertEqual(status, "C")
        self.assertIn("unresolved_or_conflicting_identity", reasons)

    def test_unknown_timing_excluded(self):
        status, reasons = training_eligibility(
            identity_status="CONFIRMED",
            timing_basis="UNKNOWN",
            measurement_status="COMPATIBLE")
        self.assertEqual(status, "C")
        self.assertIn("inspection_timing_unknown_or_invalid", reasons)

    def test_observation_key_keeps_vintage_and_source_record(self):
        self.assertEqual(observation_key("asset-1", "DECK", "2026", "row-9"),
                         ("asset-1", "DECK", "2026", "row-9"))


if __name__ == "__main__":
    unittest.main()
