import requests
import time

API_URL = "http://127.0.0.1:8000/evaluate-drift"

def check_model_health():
    try:
        # Trigger the FastAPI endpoint we just built
        response = requests.post(API_URL)
        if response.status_code == 200:
            data = response.json()
            print(f"Status Check: {data['message']}")
            
            # If drift is detected, you could trigger a Discord webhook here!
            # send_to_discord(data['message'])
        else:
            print("Error: Failed to reach the monitoring service.")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    # In a production environment, you would run this inside a background worker 
    # or an orchestrator like Airflow on a daily schedule.
    print("Starting DriftGuard automated background checker...")
    check_model_health()