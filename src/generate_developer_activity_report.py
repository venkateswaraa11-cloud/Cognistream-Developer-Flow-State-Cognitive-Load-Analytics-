
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
REPORT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "developer_activity_report.csv"
)
def export_developer_report(developer_stats):
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "developer_id",
        "coding_events",
        "coding_minutes",
        "average_coding_minutes",
        "potential_interruptions",
    ]

    with REPORT_FILE.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for developer in sorted(developer_stats):
            stats = developer_stats[developer]
            coding_events = stats["coding_events"]
            coding_minutes = stats["coding_minutes"]

            writer.writerow({
                "developer_id": developer,
                "coding_events": coding_events,
                "coding_minutes": coding_minutes,
                "average_coding_minutes": (
                    round(coding_minutes / coding_events, 2)
                    if coding_events else 0
                ),
                "potential_interruptions": (
                    stats["potential_interruptions"]
                ),
            })

    print(f"\nCSV report exported successfully: {REPORT_FILE}")


def generate_developer_activity_report():
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
        print("Report generation stopped: no records found.")
        return

    total_events = len(rows)
    developers = set()
    source_counts = defaultdict(int)
    event_counts = defaultdict(int)
    developer_stats = defaultdict(
        lambda: {
            "coding_events": 0,
            "coding_minutes": 0,
            "potential_interruptions": 0,
        }
    )
    hourly_coding = defaultdict(int)

    interruption_types = {"Message", "Task_Update"}

    for row in rows:
        developer = row["developer_id"].strip()
        source = row["source"].strip()
        event_type = row["event_type"].strip()
        duration = int(row["duration_minutes"])

        developers.add(developer)
        source_counts[source] += 1
        event_counts[event_type] += 1

        if event_type == "Coding":
            developer_stats[developer]["coding_events"] += 1
            developer_stats[developer]["coding_minutes"] += duration

            hour = row["timestamp"].strip()[11:13]
            hourly_coding[hour] += duration

        elif event_type in interruption_types:
            developer_stats[developer]["potential_interruptions"] += 1

    total_coding_events = event_counts["Coding"]
    total_coding_minutes = sum(
        stats["coding_minutes"]
        for stats in developer_stats.values()
    )
    total_interruptions = sum(
        stats["potential_interruptions"]
        for stats in developer_stats.values()
    )
    export_developer_report(developer_stats)
    print("=" * 55)
    print("       COGNISTREAM DEVELOPER ACTIVITY REPORT")
    print("=" * 55)

    print("\n1. OVERALL ACTIVITY")
    print(f"Total activity events: {total_events}")
    print(f"Unique developers: {len(developers)}")
    print(f"Total coding events: {total_coding_events}")
    print(f"Recorded coding minutes: {total_coding_minutes}")
    print(f"Potential interruption events: {total_interruptions}")

    print("\n2. EVENT DISTRIBUTION")
    for event_type, count in sorted(event_counts.items()):
        percentage = count / total_events * 100
        print(f"{event_type}: {count} ({percentage:.1f}%)")

    print("\n3. SOURCE DISTRIBUTION")
    for source, count in sorted(source_counts.items()):
        print(f"{source}: {count} events")

    print("\n4. DEVELOPER COMPARISON")
    for developer in sorted(developers):
        stats = developer_stats[developer]
        print(f"\nDeveloper: {developer}")
        print(f"Coding events: {stats['coding_events']}")
        print(f"Recorded coding minutes: {stats['coding_minutes']}")
        print(
            "Potential interruption events: "
            f"{stats['potential_interruptions']}"
        )

        if stats["coding_events"] > 0:
            average = (
                stats["coding_minutes"] / stats["coding_events"]
            )
            print(f"Average coding event duration: {average:.2f} minutes")

    print("\n5. HOURLY CODING DISTRIBUTION")
    for hour, minutes in sorted(hourly_coding.items()):
        print(f"{hour}:00 - {minutes} recorded coding minutes")

    print("\n6. ANALYTICAL NOTES")
    print(
        "Message and Task_Update events are treated as "
        "potential interruption indicators."
    )
    print(
        "These synthetic activity records do not directly "
        "measure cognitive load or prove productivity."
    )

    print("\n" + "=" * 55)
    print("             REPORT GENERATION COMPLETE")
    print("=" * 55)


if __name__ == "__main__":





    
    generate_developer_activity_report()
