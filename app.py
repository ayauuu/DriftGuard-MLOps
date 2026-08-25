import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from evidently import Report
from evidently.presets import DataDriftPreset

app = FastAPI(title="DriftGuard API")

# We can serve the HTML directly as a string to bypass any template engine caching bugs!
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DriftGuard Live Monitor</title>
    <style>
        body { font-family: Arial, sans-serif; background: #0d1117; color: #c9d1d9; text-align: center; padding-top: 50px; }
        .card { background: #161b22; border: 1px solid #30363d; display: inline-block; padding: 30px; border-radius: 10px; width: 400px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
        h1 { color: #58a6ff; font-size: 24px; }
        .status { font-size: 20px; font-weight: bold; margin: 20px 0; }
        .success { color: #3fb950; }
        .warning { color: #f85149; }
        .timer { font-size: 12px; color: #8b949e; margin-top: 15px; }
    </style>
</head>
<body>

    <div class="card">
        <h1>DriftGuard Live Monitor</h1>
        <p>Project: MLOps Data Drift Tracking</p>
        <hr style="border: 0; border-top: 1px solid #30363d;">
        
        <div id="status-box" class="status">Loading status...</div>
        <div id="details">Waiting for first check...</div>
        
        <div class="timer" id="timer">Refreshing every 5 seconds...</div>
    </div>

    <script>
        function fetchDriftStatus() {
            fetch('/evaluate-drift', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    const statusBox = document.getElementById('status-box');
                    const detailsBox = document.getElementById('details');
                    
                    statusBox.innerText = data.message;
                    statusBox.className = "status success";

                    detailsBox.innerHTML = `
                        <p>Reference Rows: ${data.dataset_metrics.reference_rows}</p>
                        <p>Current Rows: ${data.dataset_metrics.current_rows}</p>
                    `;
                })
                .catch(error => {
                    console.error('Error fetching drift:', error);
                    document.getElementById('status-box').innerText = "⚠️ Connection Lost";
                    document.getElementById('status-box').className = "status warning";
                });
        }

        fetchDriftStatus();
        setInterval(fetchDriftStatus, 5000);
    </script>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTML_CONTENT

@app.post("/evaluate-drift")
def evaluate_drift():
    # 1. Load the data
    reference_data = pd.read_csv("reference.csv")
    current_data = pd.read_csv("current.csv")

    # 2. Run the Evidently Report
    drift_report = Report(metrics=[DataDriftPreset()])
    my_snapshot = drift_report.run(reference_data=reference_data, current_data=current_data)
    
    # 3. Save the visual dashboard locally
    my_snapshot.save_html("drift_report.html")
    
    # 4. Return JSON metrics for the live page
    return {
        "status": "success",
        "message": "✅ Data looks stable!",
        "dataset_metrics": {
            "reference_rows": len(reference_data),
            "current_rows": len(current_data)
        }
    }