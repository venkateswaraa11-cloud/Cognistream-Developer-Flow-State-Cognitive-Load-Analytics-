import csv
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO


from src.generate_developer_activity_report import (
    generate_developer_activity_report,
    export_developer_report,
)



class TestDeveloperActivityReport(unittest.TestCase):

    @patch(
        "src.generate_developer_activity_report.CLEAN_FILE"
    )
    def test_report_metrics(self, mock_file):
        mock_file.exists.return_value = True

        rows = [
            {
                "event_id": "1",
                "timestamp": "2026-10-01 09:00:00",
                "developer_id": "DEV001",
                "source": "IDE",
                "event_type": "Coding",
                "duration_minutes": "25",
            },
            {
                "event_id": "2",
                "timestamp": "2026-10-01 09:30:00",
                "developer_id": "DEV001",
                "source": "Slack",
                "event_type": "Message",
                "duration_minutes": "5",
            },
            {
                "event_id": "3",
                "timestamp": "2026-10-01 10:00:00",
                "developer_id": "DEV002",
                "source": "IDE",
                "event_type": "Coding",
                "duration_minutes": "30",
            },
        ]

        mock_file.open.return_value.__enter__.return_value = (
            StringIO(
                "event_id,timestamp,developer_id,source,"
                "event_type,duration_minutes\n"
                "1,2026-10-01 09:00:00,DEV001,IDE,Coding,25\n"
                "2,2026-10-01 09:30:00,DEV001,Slack,Message,5\n"
                "3,2026-10-01 10:00:00,DEV002,IDE,Coding,30\n"
            )
        )

        output = StringIO()

        with redirect_stdout(output):
            generate_developer_activity_report()

        report = output.getvalue()

        self.assertIn("Total activity events: 3", report)
        self.assertIn("Unique developers: 2", report)
        self.assertIn("Recorded coding minutes: 55", report)
        self.assertIn("Potential interruption events: 1", report)
        self.assertIn("Developer: DEV001", report)
        self.assertIn("09:00 - 25 recorded coding minutes", report)

    @patch(
        "src.generate_developer_activity_report.CLEAN_FILE"
    )
    def test_empty_dataset(self, mock_file):
        mock_file.exists.return_value = True
        mock_file.open.return_value.__enter__.return_value = (
            StringIO(
                "event_id,timestamp,developer_id,source,"
                "event_type,duration_minutes\n"
            )
        )

        output = StringIO()

        with redirect_stdout(output):
            generate_developer_activity_report()

        self.assertIn(
            "Report generation stopped: no records found.",
            output.getvalue(),
        )


    def test_csv_export(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = Path(temp_dir) / "developer_activity_report.csv"

            stats = {
                "DEV001": {
                    "coding_events": 2,
                    "coding_minutes": 60,
                    "potential_interruptions": 2,
                },
                "DEV002": {
                    "coding_events": 1,
                    "coding_minutes": 30,
                    "potential_interruptions": 0,
                },
            }

            with patch(
                "src.generate_developer_activity_report.REPORT_FILE",
                report_path,
            ):
                with redirect_stdout(StringIO()):
                    export_developer_report(stats)

            with report_path.open(
                "r", newline="", encoding="utf-8"
            ) as file:
                rows = list(csv.DictReader(file))

            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["developer_id"], "DEV001")
            self.assertEqual(rows[0]["coding_minutes"], "60")
            self.assertEqual(
                rows[0]["average_coding_minutes"], "30.0"
            )
            self.assertEqual(
                rows[0]["potential_interruptions"], "2"
            )
if __name__ == "__main__":
    unittest.main()