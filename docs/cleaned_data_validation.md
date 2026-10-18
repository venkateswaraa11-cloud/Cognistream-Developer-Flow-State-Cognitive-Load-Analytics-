# Cleaned Developer Activity Data Validation

## Purpose

This validation step checks whether the cleaned developer activity dataset meets the project's basic data-quality requirements before further analysis.

## Input

`data/processed/developer_activity_clean.csv`

## Validation Checks

The Python script checks:

- Required columns are present.
- Required fields are not empty.
- Event IDs are not duplicated.
- Data sources belong to the approved list: GitHub, Jira, Slack, and IDE.
- Duration values are integers and are not negative.

## Implementation

The validation script is located at:

`src/validate_cleaned_data.py`

It uses Python's built-in `csv` and `pathlib` modules.

## Test Results

- Rows checked: 10
- Data-quality issues reported: 0
- Result: Validation passed

## Limitations

This version does not validate timestamp formats or handle every possible malformed CSV row. A successful result confirms only that the records passed the checks currently implemented; it does not guarantee that the dataset is completely error-free.

## Next Step

Improve validation coverage before using the dataset for downstream analysis.