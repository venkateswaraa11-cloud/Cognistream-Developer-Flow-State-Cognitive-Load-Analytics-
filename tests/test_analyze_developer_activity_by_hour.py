import unittest
from unittest.mock import patch
from io import StringIO

from src.analyze_developer_activity_by_hour import (
    analyze_developer_activity_by_hour,
)


class TestDeveloperActivityByHour(unittest.TestCase):

    @patch(
        "src.analyze_developer_activity_by_hour.CLEAN_FILE"
    )
    def test_developer_activity_by_hour(self, mock_file):
        mock_file.exists.return_value = True

        mock_file.open.return_value.__enter__.return_value = StringIO(
            "event_id,timestamp,developer_id,source,event_type,duration_minutes\n"
            "EVT001,2026-10-01 09:00:00,DEV001,IDE,Coding,25\n"
            "EVT002,2026-10-01 09:30:00,DEV001,Slack,Message,5\n"
            "EVT003,2026-10-01 10:00:00,DEV002,IDE,Coding,30\n"
            "EVT004,2026-10-01 10:30:00,DEV002,Jira,Task_Update,10\n"
        )

        output = StringIO()

        with patch("sys.stdout", output):
            analyze_developer_activity_by_hour()

        result = output.getvalue()

        self.assertIn("Total activity events: 4", result)
        self.assertIn("Developer: DEV001 | Hour: 09:00", result)
        self.assertIn("Recorded coding minutes: 25", result)
        self.assertIn("Potential interruption events: 1", result)
        self.assertIn("Developer: DEV002 | Hour: 10:00", result)
        self.assertIn("Recorded coding minutes: 30", result)


if __name__ == "__main__":
    unittest.main()