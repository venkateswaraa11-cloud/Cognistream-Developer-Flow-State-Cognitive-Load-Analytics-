import unittest
from unittest.mock import patch
from pathlib import Path
import tempfile
import csv
import io
from contextlib import redirect_stdout

from src.validate_data_quality import validate_data_quality


class TestDataQualityValidation(unittest.TestCase):

    def create_csv(self, rows):
        temp_file = tempfile.NamedTemporaryFile(
            mode="w",
            newline="",
            encoding="utf-8",
            suffix=".csv",
            delete=False
        )

        writer = csv.DictWriter(
            temp_file,
            fieldnames=[
                "event_id",
                "timestamp",
                "developer_id",
                "source",
                "event_type",
                "duration_minutes"
            ]
        )

        writer.writeheader()
        writer.writerows(rows)
        temp_file.close()

        return Path(temp_file.name)

    def test_valid_data(self):
        rows = [{
            "event_id": "EV001",
            "timestamp": "2026-10-30T09:00:00",
            "developer_id": "DEV001",
            "source": "IDE",
            "event_type": "Coding",
            "duration_minutes": "30"
        }]

        temp_file = self.create_csv(rows)

        try:
            with patch(
                "src.validate_data_quality.CLEAN_FILE",
                temp_file
            ):
                output = io.StringIO()

                with redirect_stdout(output):
                    validate_data_quality()

                self.assertIn(
                    "Data quality validation passed",
                    output.getvalue()
                )
        finally:
            temp_file.unlink()

    def test_invalid_timestamp(self):
        rows = [{
            "event_id": "EV001",
            "timestamp": "invalid-date",
            "developer_id": "DEV001",
            "source": "IDE",
            "event_type": "Coding",
            "duration_minutes": "30"
        }]

        temp_file = self.create_csv(rows)

        try:
            with patch(
                "src.validate_data_quality.CLEAN_FILE",
                temp_file
            ):
                output = io.StringIO()

                with redirect_stdout(output):
                    validate_data_quality()

                self.assertIn(
                    "Invalid timestamp",
                    output.getvalue()
                )
        finally:
            temp_file.unlink()

    def test_negative_duration(self):
        rows = [{
            "event_id": "EV001",
            "timestamp": "2026-10-30T09:00:00",
            "developer_id": "DEV001",
            "source": "IDE",
            "event_type": "Coding",
            "duration_minutes": "-10"
        }]

        temp_file = self.create_csv(rows)

        try:
            with patch(
                "src.validate_data_quality.CLEAN_FILE",
                temp_file
            ):
                output = io.StringIO()

                with redirect_stdout(output):
                    validate_data_quality()

                self.assertIn(
                    "Negative duration",
                    output.getvalue()
                )
        finally:
            temp_file.unlink()


if __name__ == "__main__":
    unittest.main()