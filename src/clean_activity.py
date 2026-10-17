
import csv
from pathlib import Path

# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define the input and output files
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "developer_activity.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
CLEAN_FILE = PROCESSED_DIR / "developer_activity_clean.csv"


def clean_activity_data():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    with RAW_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        if not fieldnames:
            raise ValueError("The raw CSV has no header row.")

        rows = list(reader)

    seen_event_ids = set()
    cleaned_rows = []
    duplicate_count = 0

    for row in rows:
        event_id = row["event_id"].strip()

        if event_id in seen_event_ids:
            duplicate_count += 1
            continue

        seen_event_ids.add(event_id)
        cleaned_rows.append(row)

    with CLEAN_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    print(f"Original rows: {len(rows)}")
    print(f"Duplicate rows removed: {duplicate_count}")
    print(f"Cleaned rows: {len(cleaned_rows)}")
    print(f"Cleaned file saved to: {CLEAN_FILE}")


if __name__ == "__main__":
    clean_activity_data()
