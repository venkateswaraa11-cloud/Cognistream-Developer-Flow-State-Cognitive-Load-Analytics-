
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
- Potential interruption event analysis by source.
- Unit test for interruption analysis.
- Developer-level hourly analysis combining recorded coding activity and potential interruption events.

## Interruption Analysis
The interruption analysis currently classifies `Message` and `Task_Update` event types as potential interruptions.

It reports the total number of activity events, the number of potential interruption events, and their distribution by source.

These classifications are analytical assumptions, not proof that every message or task update interrupted a developer's focus.

## Project Structure
- `src/validate_activity.py` — validates the raw dataset.
- `src/clean_activity.py` — cleans activity data.
- `src/validate_cleaned_data.py` — validates cleaned data.
- `src/analyze_activity.py` — summarizes activity records.
- `src/analyze_interruptions.py` — summarizes potential interruption events.
- `tests/test_analyze_interruptions.py` — tests interruption analysis.

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
