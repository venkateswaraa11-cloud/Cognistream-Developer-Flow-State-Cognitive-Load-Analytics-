
import csv
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEAN_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "developer_activity_clean.csv"
)


def analyze_coding_by_hour():
    if not CLEAN_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found: {CLEAN_FILE}"
        )

    with CLEAN_FILE.open(
        "r", newline="", encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("Analysis stopped: dataset contains no records.")
        return

    coding_events = [
        row for row in rows
        if row["event_type"].strip() == "Coding"
    ]

    print("=== CogniStream Coding Activity by Hour ===")
    print(f"Total activity events: {len(rows)}")
    print(f"Recorded coding events: {len(coding_events)}")

    if not coding_events:
        print("No coding events found.")
        return

    hourly_minutes = Counter()

    for row in coding_events:
        hour = row["timestamp"].strip()[11:13]
        duration = int(row["duration_minutes"])
        hourly_minutes[hour] += duration

    print("\nRecorded coding duration by hour:")

    for hour in sorted(hourly_minutes):
        print(
            f"- {hour}:00 - "
            f"{hourly_minutes[hour]} recorded minutes"
        )


if __name__ == "__main__":
    analyze_coding_by_hour()
