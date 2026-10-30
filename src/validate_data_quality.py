import csv
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEAN_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "developer_activity_clean.csv"
)


def validate_data_quality():
    if not CLEAN_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found: {CLEAN_FILE}"
        )

    with CLEAN_FILE.open(
        "r", newline="", encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    required_columns = {
        "event_id",
        "timestamp",
        "developer_id",
        "source",
        "event_type",
        "duration_minutes",
    }

    if not required_columns.issubset(reader.fieldnames or []):
        print("Validation failed: Missing required columns.")
        return

    errors = []

    for index, row in enumerate(rows, start=2):
        try:
            datetime.fromisoformat(row["timestamp"].strip())
        except (ValueError, AttributeError):
            errors.append(f"Row {index}: Invalid timestamp.")

        try:
            duration = int(row["duration_minutes"])
            if duration < 0:
                errors.append(
                    f"Row {index}: Negative duration."
                )
        except (ValueError, TypeError):
            errors.append(
                f"Row {index}: Invalid duration."
            )

        for column in required_columns:
            if not row.get(column, "").strip():
                errors.append(
                    f"Row {index}: Missing value in {column}."
                )

    print("=== CogniStream Data Quality Report ===")
    print(f"Total records checked: {len(rows)}")
    print(f"Total quality issues: {len(errors)}")

    for error in errors:
        print(f"- {error}")

    if not errors:
        print("Data quality validation passed.")


if __name__ == "__main__":
    validate_data_quality()