import pandas as pd
from sklearn.datasets import fetch_openml

print("Downloading dataset...")
# Fetching a standard Telco customer churn dataset from OpenML
data = fetch_openml(name='telco-customer-churn', version=1, as_frame=True)
df = data.frame

# Clean up columns and target variable for simplicity
df = df[['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract', 'PaymentMethod', 'Churn']]
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

# Split the data into Reference (historical training data) and Current (production data)
# Let's take the first 5000 rows as reference, and the rest as current production data
reference_data = df.iloc[:5000].reset_index(drop=True)
current_data = df.iloc[5000:].reset_index(drop=True)

# Save them to CSV files so our monitoring script can read them easily
reference_data.to_csv("reference.csv", index=False)
current_data.to_csv("current.csv", index=False)

print("Data successfully prepared and saved!")
print(f"Reference data shape: {reference_data.shape}")
print(f"Current data shape: {current_data.shape}")
