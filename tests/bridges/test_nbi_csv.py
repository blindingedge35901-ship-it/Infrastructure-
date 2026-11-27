import csv
import tempfile
import unittest
from pathlib import Path

from infrastructure_model.bridges.nbi_csv import (
    NbiCsvError,
    profile_nbi_rows,
    read_nbi_csv,
)


class TestLosslessNbiCsvIngestion(unittest.TestCase):
    def write_csv(self, directory, headers, rows):
        path = Path(directory) / "sample.csv"
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(headers)
            writer.writerows(rows)
        return path

    def test_preserves_leading_zeroes_and_numeric_looking_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_csv(
                directory,
                ["YEAR", "STATE_CODE_001", "STRUCTURE_NUMBER_008", "COUNTY_CODE_003"],
                [["2025", "08", "00001234", "001"]],
            )
            manifest, rows = read_nbi_csv(path)
            record = next(rows)
            self.assertEqual(record["STRUCTURE_NUMBER_008"], "00001234")
            self.assertEqual(record["STATE_CODE_001"], "08")
            self.assertEqual(record["COUNTY_CODE_003"], "001")
            self.assertIsNone(manifest.row_count)
            self.assertEqual(len(manifest.sha256), 64)

    def test_profiles_year_state_and_duplicate_keys_without_dropping(self):
        rows = iter([
            {"YEAR": "2024", "STATE_CODE_001": "08", "STRUCTURE_NUMBER_008": "0001"},
            {"YEAR": "2024", "STATE_CODE_001": "08", "STRUCTURE_NUMBER_008": "0001"},
            {"YEAR": "2025", "STATE_CODE_001": "08", "STRUCTURE_NUMBER_008": "0001"},
        ])
        result = profile_nbi_rows(rows)
        self.assertEqual(result["row_count"], 3)
        self.assertEqual(result["rows_by_year"], {"2024": 2, "2025": 1})
        self.assertEqual(result["rows_by_year_state"]["2024|08"], 2)
        self.assertEqual(result["duplicate_source_key_count"], 1)
        self.assertEqual(result["duplicate_source_keys"]["2024|08|0001"], 2)

    def test_detects_source_change_between_manifest_and_consumption(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_csv(
                directory,
                ["YEAR", "STATE_CODE_001", "STRUCTURE_NUMBER_008"],
                [["2025", "08", "0001"]],
            )
            manifest, rows = read_nbi_csv(path)
            path.write_text(
                "YEAR,STATE_CODE_001,STRUCTURE_NUMBER_008\n2025,08,0002\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(NbiCsvError, "changed"):
                list(rows)
            self.assertEqual(len(manifest.sha256), 64)

    def test_rejects_missing_required_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_csv(directory, ["YEAR", "STATE_CODE_001"], [["2025", "08"]])
            with self.assertRaises(NbiCsvError):
                read_nbi_csv(path)

    def test_rejects_duplicate_headers(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_csv(
                directory,
                ["YEAR", "STATE_CODE_001", "STRUCTURE_NUMBER_008", "YEAR"],
                [["2025", "08", "0001", "2025"]],
            )
            with self.assertRaises(NbiCsvError):
                read_nbi_csv(path)

    def test_rejects_row_width_mismatch(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_text(
                "YEAR,STATE_CODE_001,STRUCTURE_NUMBER_008\n2025,08\n",
                encoding="utf-8",
            )
            manifest, rows = read_nbi_csv(path)
            with self.assertRaises(NbiCsvError):
                list(rows)


if __name__ == "__main__":
    unittest.main()
