# CogniStream — Developer Activity Analysis

## Objective

Summarize the cleaned synthetic developer activity dataset to establish a basic analytical foundation for CogniStream.

## Input Dataset

`data/processed/developer_activity_clean.csv`

## Implementation

The analysis script is located at `src/analyze_activity.py`. It uses Python's built-in `csv`, `collections.Counter`, and `pathlib` modules.

## Metrics Generated

- Total number of recorded activity events
- Total recorded duration
- Average recorded duration per event
- Event counts by source
- Event counts by event type

## Results

- Total activity events: 10
- Total recorded duration: 184 minutes
- Average recorded duration: 18.40 minutes

### Events by Source

| Source | Events |
|---|---:|
| IDE | 4 |
| GitHub | 2 |
| Jira | 2 |
| Slack | 2 |

### Events by Type

| Event Type | Events |
|---|---:|
| Coding | 4 |
| Commit | 2 |
| Message | 2 |
| Task_Update | 2 |

## Limitations

The dataset contains synthetic records. These metrics describe the supplied activity records only; they do not directly measure productivity, cognitive load, or flow state. Recorded duration is treated as a numeric field and is not independently verified as elapsed time.

## Next Step

Expand the analysis with time-based activity patterns and source transitions, then build SQL-based analytical queries.
