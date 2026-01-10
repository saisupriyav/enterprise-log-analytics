# Enterprise Log & Metrics Analytics Pipeline

## Problem Statement
Enterprise systems generate large volumes of unstructured logs and background job metrics.
This project builds a batch data pipeline to ingest, parse, clean, and analyze system logs to generate operational KPIs.

## Architecture
- Ingest raw system logs (CSV)
- Parse and clean log records
- Store structured data in a relational database
- Generate KPIs using SQL

## Tech Stack
- Python
- Pandas
- SQL
- Relational Database (SQLite / PostgreSQL)

## Project Structure
enterprise-log-analytics/
├── data/raw/system_logs.csv
├── src/
│   ├── ingest_logs.py
│   ├── clean_logs.py
│   └── load_to_db.py
├── sql/
│   ├── create_tables.sql
│   └── kpi_queries.sql
├── README.md
└── requirements.txt

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
