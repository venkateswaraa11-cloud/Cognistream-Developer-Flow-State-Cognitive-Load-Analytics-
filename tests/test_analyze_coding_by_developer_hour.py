import unittest
from unittest.mock import patch
from io import StringIO

from src.analyze_coding_by_developer_hour import (
    analyze_coding_by_developer_hour,
)


class TestAnalyzeCodingByDeveloperHour(unittest.TestCase):

    @patch("src.analyze_coding_by_developer_hour.CLEAN_FILE")
    def test_analyze_coding_by_developer_hour(self, mock_file):
        mock_file.exists.return_value = True

        mock_file.open.return_value.__enter__.return_value = StringIO(
            "event_id,timestamp,developer_id,source,event_type,duration_minutes\n"
            "EVT001,2026-10-01 09:00:00,DEV001,IDE,Coding,25\n"
            "EVT002,2026-10-01 09:30:00,DEV001,IDE,Coding,35\n"
            "EVT003,2026-10-01 10:00:00,DEV002,IDE,Coding,30\n"
            "EVT004,2026-10-01 10:30:00,DEV003,IDE,Coding,40\n"
            "EVT005,2026-10-01 11:00:00,DEV002,Slack,Message,5\n"
        )

        output = StringIO()

        with patch("sys.stdout", output):
            analyze_coding_by_developer_hour()

        result = output.getvalue()

        self.assertIn("Total activity events: 5", result)
        self.assertIn("Recorded coding events: 4", result)
        self.assertIn("DEV001 at 09:00 - 60 recorded minutes", result)
        self.assertIn("DEV002 at 10:00 - 30 recorded minutes", result)
        self.assertIn("DEV003 at 10:00 - 40 recorded minutes", result)
        self.assertNotIn("DEV002 at 11:00", result)


if __name__ == "__main__":
    unittest.main()