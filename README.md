
# CogniStream
### Developer Flow-State & Cognitive Load Analytics

## Project Overview
CogniStream explores developer workflow patterns, activity events, interruptions, and context-switching using synthetic developer activity data.

## Objectives
- Analyze developer activity and workflow patterns.
- Explore potential focus periods and interruptions.
- Investigate context-switching patterns.
- Build data-driven visualizations and dashboards.
- Communicate findings through analytical reports.

## Technology Stack
- **Programming:** Python
- **Workflow Orchestration:** Apache Airflow
- **Data Processing:** Polars
- **Database:** ClickHouse
- **Query Language:** SQL
- **Backend API:** FastAPI
- **Frontend:** React
- **Dashboard Visualization:** Tremor.js
- **Version Control:** Git and GitHub

## Current Features
- Synthetic developer activity dataset.
- Raw dataset validation.
- Activity data cleaning.
- Cleaned dataset validation.
- Basic activity analysis.
- Potential interruption event analysis by source and developer.
- Coding event counts and recorded coding duration by developer.
- Unit tests for interruption and coding activity analysis.
- Coding activity analysis by hour, summarizing recorded coding duration according to each event's start hour.
- Coding activity analysis by developer and hour, summarizing recorded coding duration for each developer during each event's start hour.
## Interruption Analysis
The interruption analysis currently classifies `Message` and `Task_Update` event types as potential interruptions.

It reports the total number of activity events, the number of potential interruption events, and their distribution by source.

These classifications are analytical assumptions, not proof that every message or task update interrupted a developer's focus.

The analysis also groups potential interruption events by developer ID to show how these events are distributed across developers in the synthetic dataset.

## Coding Activity Analysis
The coding activity analysis identifies records with the `Coding` event type.

It reports the total number of activity events, the number of recorded coding events, the total recorded coding duration, and coding event counts and recorded duration by developer.

These results describe the synthetic dataset and should not be interpreted as verified measurements of real developer productivity or time spent coding.

## Project Structure
- `src/validate_activity.py` — validates the raw dataset.
- `src/clean_activity.py` — cleans activity data.
- `src/validate_cleaned_data.py` — validates cleaned data.
- `src/analyze_activity.py` — summarizes activity records.
- `src/analyze_interruptions.py` — summarizes potential interruption events.
- `src/analyze_coding_activity.py` — summarizes coding events and recorded coding duration by developer.
- `tests/test_analyze_interruptions.py` — tests interruption analysis.
- `tests/test_analyze_coding_activity.py` — tests coding activity analysis.
- `src/analyze_coding_by_developer_hour.py` — summarizes coding duration by developer and event start hour.
- `tests/test_analyze_coding_by_developer_hour.py` — tests coding activity analysis by developer and hour.

## Data Integrity and Limitations
The project currently uses synthetic activity data. Its results demonstrate the analysis workflow and must not be interpreted as verified measurements of real developer productivity, cognitive load, or flow state.

Activity events alone cannot establish causation or prove that a developer experienced an interruption.

## Planned Development
- Refine interruption and context-switching metrics.
- Develop reproducible analytics with SQL and Polars.
- Orchestrate data workflows with Apache Airflow.
- Store and query analytical data using ClickHouse.
- Build API endpoints and an interactive dashboard.
- Validate the integrated pipeline and document findings.

## Expected Outcome
A documented, tested analytics pipeline and interactive dashboard for exploring developer activity patterns and potential workflow friction.
