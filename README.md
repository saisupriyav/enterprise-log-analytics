# Enterprise Log & Metrics Analytics Pipeline

## Problem Statement
Enterprise systems generate large volumes of system logs and background job metrics that are often unstructured and difficult to analyze.
This project builds a batch data pipeline that ingests raw system logs, parses and cleans them, stores structured data in a relational database, and generates operational KPIs to support system monitoring and reliability analysis.

## Why This Project
Operations teams need visibility into system health, job failures, and performance trends to minimize downtime and meet SLAs.
This pipeline demonstrates how raw logs can be transformed into actionable metrics for operational decision-making.

## Architecture Overview
1. Ingest raw system log files (CSV)
2. Parse and clean log records using Python
3. Store structured data in a relational database
4. Generate operational KPIs using SQL queries

This design mirrors real-world batch processing pipelines used in enterprise environments.

## Tech Stack
- Python
- Pandas
- SQL
- Relational Database (SQLite / PostgreSQL)

## Project Structure

```text
enterprise-log-analytics/
│
├── data/
│   └── raw/
│       └── system_logs.csv
│
├── src/
│   ├── ingest_logs.py
│   ├── clean_logs.py
│   └── load_to_db.py
│
├── sql/
│   ├── create_tables.sql
│   └── kpi_queries.sql
│
├── README.md
└── requirements.txt
```


## KPIs Generated
- Job failure rate
- System downtime
- Average job duration
- Error frequency trends

## How to Run
1. Install dependencies  
   `pip install -r requirements.txt`

2. Run ingestion  
   `python src/ingest_logs.py`

3. Clean logs  
   `python src/clean_logs.py`

4. Load data into DB  
   `python src/load_to_db.py`
