from ibm_watson_machine_learning import APIClient
from dotenv import load_dotenv
import pandas as pd
import json
import os

# Load credentials from .env file
load_dotenv()

# Watson Machine Learning credentials and configs
wml_credentials = {
    "url": os.getenv("WML_URL"),
    "apikey": os.getenv("WML_APIKEY")
}

space_id = os.getenv("WML_SPACE_ID")
deployment_id = os.getenv("WML_DEPLOYMENT_ID")

# Connect to IBM Watson Machine Learning
client = APIClient(wml_credentials)
client.set.default_space(space_id)

# === Load CSV and Prepare Payload ===
try:
    # Load your test dataset
    df = pd.read_csv("Admission_Predict.csv")  # <-- Change filename if needed

    # Drop columns not required by model
    columns_to_drop = ["Chance of Admit", "Serial No.", "Serial No"]
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    # Construct input payload
    payload = {
        "input_data": [
            {
                "fields": df.columns.tolist(),
                "values": df.values.tolist()
            }
        ]
    }

    # === Score the model ===
    response = client.deployments.score(deployment_id, payload)

    # Print formatted prediction results
    print("\n✅ Scoring successful. Results:\n")
    print(json.dumps(response, indent=2))

except Exception as e:
    print("❌ Scoring failed:", str(e))
