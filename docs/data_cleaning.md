# CogniStream — Data Cleaning

## Objective

Prepare a cleaned copy of the synthetic developer activity dataset for future analysis while preserving the original raw data.

## Input and Output

- **Input:** `data/raw/developer_activity.csv`
- **Output:** `data/processed/developer_activity_clean.csv`
- **Script:** `src/clean_activity.py`

## Cleaning Rule

The script uses `event_id` to identify duplicate records.

- The first occurrence of an event ID is retained.
- Later rows with the same event ID are skipped.
- The original raw CSV is not modified.

## Validation Results

- Original data rows: 10
- Cleaned data rows: 10
- Duplicate rows removed: 0

The row counts match because no duplicate event IDs were found in the current dataset.

## Limitations

This initial cleaning script focuses only on duplicate event IDs. It does not yet handle missing values, invalid timestamps, unexpected categories, or invalid duration values. Those checks require additional validation.

The dataset is synthetic and does not establish real developer productivity, cognitive load, or flow state.
