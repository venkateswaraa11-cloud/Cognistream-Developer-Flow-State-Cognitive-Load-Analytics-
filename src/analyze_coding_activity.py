
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


def analyze_coding_activity():
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

    print("=== CogniStream Coding Activity Analysis ===")
    print(f"Total activity events: {len(rows)}")
    print(f"Recorded coding events: {len(coding_events)}")

    if not coding_events:
        print("No coding events found.")
        return

    total_coding_minutes = sum(
        int(row["duration_minutes"])
        for row in coding_events
    )

    developer_counts = Counter(
        row["developer_id"].strip()
        for row in coding_events
    )

    developer_minutes = Counter()

    for row in coding_events:
        developer = row["developer_id"].strip()
        duration = int(row["duration_minutes"])
        developer_minutes[developer] += duration

    print(f"Total recorded coding duration: {total_coding_minutes} minutes")

    print("\nCoding activity by developer:")

    for developer in sorted(developer_counts):
        print(
            f"- {developer}: "
            f"{developer_counts[developer]} coding events, "
            f"{developer_minutes[developer]} recorded minutes"
        )


if __name__ == "__main__":
    analyze_coding_activity()
