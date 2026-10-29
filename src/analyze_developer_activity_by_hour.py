import csv
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEAN_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "developer_activity_clean.csv"
)


def analyze_developer_activity_by_hour():
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
    hourly_stats = defaultdict(
        lambda: {
            "coding_events": 0,
            "coding_minutes": 0,
            "potential_interruptions": 0,
        }
    )

    for row in rows:
        developer = row["developer_id"].strip()
        hour = row["timestamp"].strip()[11:13]
        key = (developer, hour)
        event_type = row["event_type"].strip()

        if event_type == "Coding":
            hourly_stats[key]["coding_events"] += 1
            hourly_stats[key]["coding_minutes"] += int(
                row["duration_minutes"]
            )
        elif event_type in interruption_types:
            hourly_stats[key]["potential_interruptions"] += 1

    print("=== CogniStream Developer Activity by Hour ===")
    print(f"Total activity events: {len(rows)}")

    for developer, hour in sorted(hourly_stats):
        stats = hourly_stats[(developer, hour)]

        print(f"\nDeveloper: {developer} | Hour: {hour}:00")
        print(f"- Coding events: {stats['coding_events']}")
        print(f"- Recorded coding minutes: {stats['coding_minutes']}")
        print(
            "- Potential interruption events: "
            f"{stats['potential_interruptions']}"
        )


if __name__ == "__main__":
    analyze_developer_activity_by_hour()