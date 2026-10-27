
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


def analyze_interruptions_by_hour():
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

    interruption_types = {"Message", "Task_Update"}

    interruptions = [
        row for row in rows
        if row["event_type"].strip() in interruption_types
    ]

    print("=== CogniStream Potential Interruptions by Hour ===")
    print(f"Total activity events: {len(rows)}")
    print(f"Potential interruption events: {len(interruptions)}")

    if not interruptions:
        print("No potential interruption events found.")
        return

    hourly_counts = Counter()

    for row in interruptions:
        hour = row["timestamp"].strip()[11:13]
        hourly_counts[hour] += 1

    print("\nPotential interruption events by hour:")

    for hour in sorted(hourly_counts):
        print(f"- {hour}:00 - {hourly_counts[hour]} events")


if __name__ == "__main__":
    analyze_interruptions_by_hour()
