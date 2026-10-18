
import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEAN_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "developer_activity_clean.csv"
)

REQUIRED_COLUMNS = [
    "event_id",
    "timestamp",
    "developer_id",
    "source",
    "event_type",
    "duration_minutes",
]

ALLOWED_SOURCES = {"GitHub", "Jira", "Slack", "IDE"}


def validate_cleaned_data():
    if not CLEAN_FILE.exists():
        raise FileNotFoundError(f"Cleaned CSV not found: {CLEAN_FILE}")

    with CLEAN_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            print("Validation failed: CSV header is missing.")
            return

        missing_columns = [
            column for column in REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]

        if missing_columns:
            print(f"Validation failed: missing columns {missing_columns}")
            return

        rows = list(reader)

    issues = []
    seen_event_ids = set()

    for row_number, row in enumerate(rows, start=2):
        event_id = row["event_id"].strip()
        source = row["source"].strip()
        duration = row["duration_minutes"].strip()

        if not event_id:
            issues.append(f"Row {row_number}: event_id is empty.")
        elif event_id in seen_event_ids:
            issues.append(f"Row {row_number}: duplicate event_id '{event_id}'.")
        else:
            seen_event_ids.add(event_id)

        for column in REQUIRED_COLUMNS:
            if not row[column].strip():
                issues.append(f"Row {row_number}: {column} is empty.")

        if source not in ALLOWED_SOURCES:
            issues.append(f"Row {row_number}: invalid source '{source}'.")

        try:
            duration_value = int(duration)
            if duration_value < 0:
                issues.append(f"Row {row_number}: duration cannot be negative.")
        except ValueError:
            issues.append(f"Row {row_number}: duration must be an integer.")

    print(f"Rows checked: {len(rows)}")

    if issues:
        print(f"Validation failed: {len(issues)} issue(s) found.")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("Validation passed: no data-quality issues found.")


if __name__ == "__main__":
    validate_cleaned_data()
