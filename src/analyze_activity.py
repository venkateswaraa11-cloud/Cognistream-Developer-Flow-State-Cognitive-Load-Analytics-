
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


def analyze_activity():
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

    source_counts = Counter(
        row["source"].strip() for row in rows
    )

    event_type_counts = Counter(
        row["event_type"].strip() for row in rows
    )

    durations = [
        int(row["duration_minutes"])
        for row in rows
    ]

    total_duration = sum(durations)
    average_duration = total_duration / len(durations)

    print("=== CogniStream Activity Analysis ===")
    print(f"Total activity events: {len(rows)}")
    print(f"Total recorded duration: {total_duration} minutes")
    print(f"Average recorded duration: {average_duration:.2f} minutes")

    print("\nEvents by source:")
    for source, count in sorted(source_counts.items()):
        print(f"- {source}: {count}")

    print("\nEvents by type:")
    for event_type, count in sorted(event_type_counts.items()):
        print(f"- {event_type}: {count}")


if __name__ == "__main__":
    analyze_activity()
