# score_model.py

from ibm_watson_machine_learning import APIClient
from dotenv import load_dotenv
import json
import os

load_dotenv()
wml_credentials = {
    "url": os.getenv("WML_URL"),
    "apikey": os.getenv("WML_APIKEY")
}

space_id = os.getenv("WML_SPACE_ID")

deployment_id = os.getenv("WML_DEPLOYMENT_ID")
client = APIClient(wml_credentials)

# Optional: confirm connection
client.set.default_space(space_id)  # only if you're using deployment spaces

# Example payload
payload = {
    "input_data": [
        {
            "fields": ["CGPA", "GRE Score", "LOR", "Research", "SOP", "TOEFL Score", "Serial No.", "University Rating", "Statement of Purpose"],
            "values": [
                [8.5, 320, 3, 1, 4, 110, 123, 4, 3.5]
            ]
        }
    ]
}

try:
    response = client.deployments.score(deployment_id, payload)
    print(json.dumps(response, indent=2))
except Exception as e:
    print("Scoring failed:", str(e))
