# 🛡️ DriftGuard MLOps: Real-Time Data Drift Monitoring Dashboard

An end-to-end MLOps microservice built to monitor production data integrity, detect distribution drift using Evidently AI, and display real-time updates via a custom auto-refreshing FastAPI web dashboard—fully containerized with Docker.

---

## 🚀 Key Features
* **Automated Drift Detection:** Powered by Evidently AI's `DataDriftPreset` to compare baseline reference datasets against live production data.
* **Real-Time Web Dashboard:** A built-in, auto-polling UI that checks model health and updates metrics every 5 seconds.
* **FastAPI Backend:** High-performance asynchronous REST endpoints (`/evaluate-drift`) returning structured JSON metrics.
* **Dockerized Architecture:** Completely containerized environment ensuring seamless deployment across any machine or cloud platform.

---

## 🛠️ Tech Stack
* **Python / FastAPI:** REST API development and serving.
* **Evidently AI:** Statistical data drift analysis and HTML report generation.
* **Pandas / NumPy:** Data ingestion and manipulation.
* **Docker:** Containerization and deployment.
* **HTML5 / CSS / JavaScript:** Frontend polling interface.

---

## 📁 Project Structure
```text
drift-guard-mlops/
│
├── app.py                  # FastAPI application & dashboard server
├── reference.csv           # Baseline reference dataset
├── current.csv             # Production / incoming dataset
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker container configuration
└── README.md               # Project documentation
