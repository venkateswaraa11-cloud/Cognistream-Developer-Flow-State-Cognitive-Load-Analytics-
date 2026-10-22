
import unittest
from unittest.mock import patch
from io import StringIO

from src.analyze_coding_activity import analyze_coding_activity


class TestAnalyzeCodingActivity(unittest.TestCase):

    @patch("src.analyze_coding_activity.CLEAN_FILE")
    def test_analyze_coding_activity(self, mock_file):
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
            analyze_coding_activity()

        result = output.getvalue()

        self.assertIn("Total activity events: 5", result)
        self.assertIn("Recorded coding events: 4", result)
        self.assertIn("Total recorded coding duration: 130 minutes", result)
        self.assertIn("DEV001: 2 coding events, 60 recorded minutes", result)
        self.assertIn("DEV002: 1 coding events, 30 recorded minutes", result)
        self.assertIn("DEV003: 1 coding events, 40 recorded minutes", result)


if __name__ == "__main__":
    unittest.main()
