# CogniStream - Data Source Specification

## 1. Purpose

CogniStream explores developer workflow patterns, focus periods, interruptions, and task switching using developer activity events.

The initial version will use synthetic (mock) data to develop and validate the analytics workflow.

## 2. Planned Data Sources

| Source | Example Events | Analytical Purpose |
|---|---|---|
| GitHub | Commits, pull requests, code reviews | Explore coding activity patterns |
| Jira | Task started, task updated, task completed | Understand task progress and transitions |
| Slack | Message timestamps and channel activity | Explore potential communication interruptions |
| VS Code / ActivityWatch | Application activity and window changes | Estimate active periods and application switching |

## 3. Initial Data Strategy

- Begin with synthetic data that represents realistic developer activity.
- Use consistent timestamps and clearly defined event types.
- Avoid collecting personal messages, source-code contents, passwords, or other sensitive information.
- Keep mock data clearly distinguished from real-world observations.

## 4. Planned Event Fields

Each event may contain the following fields:

- `event_id`: Unique identifier for the event.
- `timestamp`: Date and time when the event occurred.
- `source`: System that produced the event.
- `event_type`: Type of activity recorded.
- `developer_id`: Pseudonymous identifier for the developer.
- `task_id`: Optional identifier for the related task.

Fields will be refined after the initial dataset is designed.

## 5. Initial Analytical Questions

1. How long do observed activity periods last?
2. How frequently do application or task switches occur?
3. How often do interruptions appear during an observed work period?
4. How do activity patterns vary throughout the day?

## 6. Measurement Limitations

Developer activity events are indirect indicators of workflow patterns. They do not independently measure actual cognitive load, prove a flow state, or establish that interruptions caused a productivity change.

Missing events and incomplete data may also affect the analysis.

## 7. Next Steps

1. Design a synthetic developer activity dataset.
2. Validate timestamps, event types, and required fields.
3. Clean and transform the data using Python and Polars.
4. Store analytical data in ClickHouse.
5. Explore patterns using SQL.
6. Develop an API and interactive dashboard.

---

**Status:** Data-source plan drafted; dataset creation and validation are pending.
