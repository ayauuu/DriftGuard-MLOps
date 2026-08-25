import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# 1. Load our reference and current datasets
reference_data = pd.read_csv("reference.csv")
current_data = pd.read_csv("current.csv")

print("Running Evidently AI Data Drift Report...")

# 2. Create an Evidently Report focused on Data Drift
drift_report = Report(metrics=[
    DataDriftPreset(),
])

# 3. Run the report and capture the result in a new variable
my_snapshot = drift_report.run(reference_data=reference_data, current_data=current_data)

# 4. Save that snapshot as an interactive HTML file
my_snapshot.save_html("drift_report.html")

print("Report generated successfully! Open 'drift_report.html' in your browser.")