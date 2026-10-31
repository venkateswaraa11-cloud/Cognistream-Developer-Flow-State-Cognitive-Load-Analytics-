import csv
import sqlite3
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEAN_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "developer_activity_clean.csv"
)

DATABASE_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "cognistream.db"
)

SQL_FILE = PROJECT_ROOT / "sql" / "developer_analytics.sql"
def create_database():
    connection = sqlite3.connect(DATABASE_FILE)

    return connection
def load_csv_to_database(connection):
    with CLEAN_FILE.open(
        "r", newline="", encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS developer_activity (
            event_id TEXT,
            timestamp TEXT,
            developer_id TEXT,
            source TEXT,
            event_type TEXT,
            duration_minutes INTEGER
        )
    """)

    cursor.execute("DELETE FROM developer_activity")

    cursor.executemany("""
        INSERT INTO developer_activity (
            event_id,
            timestamp,
            developer_id,
            source,
            event_type,
            duration_minutes
        )
        VALUES (
            :event_id,
            :timestamp,
            :developer_id,
            :source,
            :event_type,
            :duration_minutes
        )
    """, rows)

    connection.commit()

    print(f"Loaded {len(rows)} records into SQLite.")


def run_analytics(connection):
    with SQL_FILE.open("r", encoding="utf-8") as file:
        query = file.read()

    cursor = connection.cursor()
    cursor.execute(query)

    results = cursor.fetchall()

    columns = [
        description[0]
        for description in cursor.description
    ]

    print("\nDEVELOPER ANALYTICS SUMMARY")
    print("=" * 60)
    print(" | ".join(columns))
    print("-" * 60)

    for row in results:
        print(" | ".join(str(value) for value in row))
        def main():
            connection = create_database()

            try:
                load_csv_to_database(connection)
                run_analytics(connection)
            finally:
                connection.close()


            if __name__ == "__main__":
                 main()


def main():
    connection = create_database()

    try:
        load_csv_to_database(connection)
        run_analytics(connection)
    finally:
        connection.close()


if __name__ == "__main__":
    main()