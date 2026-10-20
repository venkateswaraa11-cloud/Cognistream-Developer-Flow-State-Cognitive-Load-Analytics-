
import io
import unittest
from unittest.mock import patch

from src.analyze_interruptions import analyze_interruptions


class TestAnalyzeInterruptions(unittest.TestCase):

    @patch("src.analyze_interruptions.CLEAN_FILE")
    def test_analyze_interruptions(self, mock_file):
        mock_file.exists.return_value = True

        mock_file.open.return_value.__enter__.return_value = io.StringIO(
            "event_id,timestamp,developer_id,source,event_type,duration_minutes\n"
            "EVT001,2026-10-01 09:00:00,DEV001,Slack,Message,5\n"
            "EVT002,2026-10-01 09:10:00,DEV001,IDE,Coding,25\n"
            "EVT003,2026-10-01 09:20:00,DEV002,Jira,Task_Update,10\n"
        )

        with patch("builtins.print") as mock_print:
            analyze_interruptions()

        output = "\n".join(
            str(call.args[0]) for call in mock_print.call_args_list
        )

        self.assertIn("Total activity events: 3", output)
        self.assertIn("Potential interruption events: 2", output)
        self.assertIn("Slack: 1", output)
        self.assertIn("Jira: 1", output)


if __name__ == "__main__":
    unittest.main()
