import json
import pandas as pd
import os


def generate_reports():

    path = "reports/report.json"

    if not os.path.exists(path):
        print("JSON report not found")
        return

    with open(path) as f:

        data = json.load(f)

    rows = []

    for test in data["tests"]:

        rows.append({

            "Test": test["nodeid"],
            "Outcome": test["outcome"],
            "Duration": test["call"]["duration"]

        })

    df = pd.DataFrame(rows)

    os.makedirs("reports", exist_ok=True)

    # CSV
    df.to_csv(
        "reports/report.csv",
        index=False
    )

    # Excel
    df.to_excel(
        "reports/report.xlsx",
        index=False
    )

    print("CSV Generated")
    print("Excel Generated")