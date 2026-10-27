
import unittest
from unittest.mock import patch
from io import StringIO

from src.analyze_interruptions_by_hour import (
    analyze_interruptions_by_hour,
)


class TestAnalyzeInterruptionsByHour(unittest.TestCase):

    @patch("src.analyze_interruptions_by_hour.CLEAN_FILE")
    def test_analyze_interruptions_by_hour(self, mock_file):
        mock_file.exists.return_value = True

        mock_file.open.return_value.__enter__.return_value = StringIO(
            "event_id,timestamp,developer_id,source,event_type,duration_minutes\n"
            "EVT001,2026-10-01 09:00:00,DEV001,Slack,Message,5\n"
            "EVT002,2026-10-01 10:00:00,DEV002,Jira,Task_Update,10\n"
            "EVT003,2026-10-01 10:30:00,DEV001,Slack,Message,4\n"
            "EVT004,2026-10-01 11:00:00,DEV002,Jira,Task_Update,8\n"
            "EVT005,2026-10-01 11:15:00,DEV003,IDE,Coding,20\n"
        )

        output = StringIO()

        with patch("sys.stdout", output):
            analyze_interruptions_by_hour()

        result = output.getvalue()

        self.assertIn("Total activity events: 5", result)
        self.assertIn("Potential interruption events: 4", result)
        self.assertIn("09:00 - 1 events", result)
        self.assertIn("10:00 - 2 events", result)
        self.assertIn("11:00 - 1 events", result)


if __name__ == "__main__":
    unittest.main()
