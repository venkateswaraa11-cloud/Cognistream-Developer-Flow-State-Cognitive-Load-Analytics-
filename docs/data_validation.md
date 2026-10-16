
# CogniStream Dataset Validation

## Purpose
Validate the synthetic developer activity dataset before analysis.

## Dataset
- File: `data/raw/developer_activity.csv`
- Records: 10
- Developers: DEV001, DEV002, DEV003
- Data type: Synthetic activity data created for testing

## Validation Rules
1. Required columns must be present.
2. Required fields must not be empty.
3. Each event_id must be unique.
4. Source must be GitHub, Jira, Slack, or IDE.
5. Duration must be an integer greater than or equal to zero.
6. Timestamp must follow `YYYY-MM-DD HH:MM:SS`.

## Validation Results
- Records checked: 10
- Result: Passed, with no issues reported by the validation script.

## Limitations
- The dataset is small and synthetic.
- Passing these checks does not prove that the data represents real developer behavior.
- The script checks timestamp format, not whether events occur in a realistic chronological order.
