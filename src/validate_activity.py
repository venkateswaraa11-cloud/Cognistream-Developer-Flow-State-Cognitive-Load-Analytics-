
import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "raw" / "developer_activity.csv"

REQUIRED_COLUMNS = {
    "event_id",
    "timestamp",
    "developer_id",
    "source",
    "event_type",
    "duration_minutes",
}

ALLOWED_SOURCES = {"GitHub", "Jira", "Slack", "IDE"}


def validate_activity_data():
    errors = []
    seen_event_ids = set()
    row_count = 0

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            print("ERROR: CSV file is empty or has no header.")
            return

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)

        if missing_columns:
            print(f"ERROR: Missing columns: {sorted(missing_columns)}")
            return

        for line_number, row in enumerate(reader, start=2):
            row_count += 1

            for column in REQUIRED_COLUMNS:
                if not (row.get(column) or "").strip():
                    errors.append(
                        f"Row {line_number}: {column} is missing."
                    )

            event_id = (row.get("event_id") or "").strip()

            if event_id:
                if event_id in seen_event_ids:
                    errors.append(
                        f"Row {line_number}: duplicate event_id '{event_id}'."
                    )
                seen_event_ids.add(event_id)

            source = (row.get("source") or "").strip()

            if source and source not in ALLOWED_SOURCES:
                errors.append(
                    f"Row {line_number}: invalid source '{source}'."
                )

            duration = (row.get("duration_minutes") or "").strip()

            if duration:
                try:
                    duration_value = int(duration)

                    if duration_value < 0:
                        errors.append(
                            f"Row {line_number}: duration cannot be negative."
                        )
                except ValueError:
                    errors.append(
                        f"Row {line_number}: duration must be an integer."
                    )

            timestamp = (row.get("timestamp") or "").strip()

            if timestamp:
                from datetime import datetime

                try:
                    datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    errors.append(
                        f"Row {line_number}: invalid timestamp '{timestamp}'."
                    )

    print(f"Rows checked: {row_count}")

    if errors:
        print(f"Validation failed: {len(errors)} issue(s) found.")
        for error in errors:
            print(f"- {error}")
    else:
        print("Validation passed: no data-quality issues found.")


if __name__ == "__main__":
    validate_activity_data()
