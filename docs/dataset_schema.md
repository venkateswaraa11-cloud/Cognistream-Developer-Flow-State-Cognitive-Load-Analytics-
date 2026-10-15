# CogniStream — Synthetic Developer Activity Dataset Schema

## 1. Purpose

This dataset contains synthetic developer activity events created for analyzing workflow patterns, application switching, and potential interruptions.

The records are simulated for learning and demonstration. They do not represent real developers or prove actual cognitive load or flow state.

## 2. Data Sources

- GitHub — simulated code and commit activity
- Jira — simulated task activity
- Slack — simulated messaging activity
- IDE — simulated coding and development activity

## 3. Dataset Columns

| Column | Data Type | Description | Example |
|---|---|---|---|
| event_id | String | Unique identifier for each event | EVT001 |
| timestamp | Datetime | Date and time of the event | 2026-10-01 09:30:00 |
| developer_id | String | Anonymous developer identifier | DEV001 |
| source | String | Application that generated the event | GitHub |
| event_type | String | Type of activity performed | Commit |
| duration_minutes | Integer | Duration of the activity in minutes | 15 |

## 4. Privacy

Developer identifiers are fictional. No real personal information is included.


## 5. Data Quality Rules

1. Every event must have a unique event_id.
2. Every event must have a valid timestamp.
3. developer_id must not contain real personal information.
4. source must be GitHub, Jira, Slack, or IDE.
5. duration_minutes must be a non-negative integer.
6. Required fields must not be empty.
7. Synthetic records must be clearly identified as simulated data.
## 6. Dataset File

- File name: `developer_activity.csv`
- Location: `data/raw/developer_activity.csv`
- Format: CSV (Comma-Separated Values)
- Initial sample size: 5 synthetic activity records
- Column count: 6, excluding the header row from the record count
- Status: Initial sample created; validation and expansion are pending