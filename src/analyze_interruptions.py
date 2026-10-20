
import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEAN_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "developer_activity_clean.csv"
)


def analyze_interruptions():
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

    print("=== CogniStream Interruption Analysis ===")
    print(f"Total activity events: {len(rows)}")
    print(f"Potential interruption events: {len(interruptions)}")

    print("\nPotential interruptions by source:")
    source_counts = {}

    for row in interruptions:
        source = row["source"].strip()
        source_counts[source] = source_counts.get(source, 0) + 1

    for source, count in sorted(source_counts.items()):
        print(f"- {source}: {count}")


if __name__ == "__main__":
    analyze_interruptions()
