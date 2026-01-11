import csv
import random
from datetime import datetime, timedelta

NUM_RECORDS = 1000
OUTPUT_FILE = "data/raw/system_logs.csv"

systems = ["ERP", "Billing", "CRM", "HRMS"]
job_types = ["ETL", "REPORT", "BACKUP"]
statuses = ["SUCCESS", "FAILED", "RUNNING"]
hosts = ["host01", "host02", "host03"]

start_time = datetime.now() - timedelta(days=7)

with open(OUTPUT_FILE, mode="w", newline="") as f:
    writer = csv.writer(f)

    # header
    writer.writerow([
        "timestamp",
        "system_name",
        "job_name",
        "job_type",
        "status",
        "duration_sec",
        "error_code",
        "host"
    ])

    for i in range(NUM_RECORDS):
        timestamp = start_time + timedelta(minutes=random.randint(1, 10080))
        system = random.choice(systems)
        job_type = random.choice(job_types)
        status = random.choices(
            statuses, weights=[0.8, 0.15, 0.05]
        )[0]

        duration = random.randint(30, 3600)
        error_code = "" if status == "SUCCESS" else random.choice(["E101", "E205", "E330"])
        job_name = f"{system}_{job_type}_JOB_{random.randint(1,20)}"
        host = random.choice(hosts)

        writer.writerow([
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            system,
            job_name,
            job_type,
            status,
            duration,
            error_code,
            host
        ])

print(f"Generated {NUM_RECORDS} log records in {OUTPUT_FILE}")
