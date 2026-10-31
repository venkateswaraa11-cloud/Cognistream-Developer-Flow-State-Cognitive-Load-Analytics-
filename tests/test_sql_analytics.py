import sqlite3

from src.run_sql_analytics import (
    load_csv_to_database,
    run_analytics,
)


def test_sqlite_database_loads_records():
    connection = sqlite3.connect(":memory:")

    try:
        load_csv_to_database(connection)

        cursor = connection.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM developer_activity"
        )

        assert cursor.fetchone()[0] == 10

    finally:
        connection.close()


def test_sql_analytics_returns_developer_results():
    connection = sqlite3.connect(":memory:")

    try:
        load_csv_to_database(connection)

        cursor = connection.cursor()
        cursor.execute("""
            SELECT
                developer_id,
                SUM(
                    CASE
                        WHEN event_type = 'Coding'
                        THEN duration_minutes
                        ELSE 0
                    END
                ) AS coding_minutes
            FROM developer_activity
            GROUP BY developer_id
            ORDER BY coding_minutes DESC
        """)

        results = cursor.fetchall()

        assert results == [
            ("DEV001", 60),
            ("DEV003", 40),
            ("DEV002", 30),
        ]

    finally:
        connection.close()