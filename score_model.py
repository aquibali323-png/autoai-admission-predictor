# from ibm_watson_machine_learning import APIClient
# from dotenv import load_dotenv
# import pandas as pd
# import json
# import os

# # Load environment variables from .env
# load_dotenv()

# # WML Credentials
# wml_credentials = {
#     "url": os.getenv("WML_URL"),
#     "apikey": os.getenv("WML_APIKEY")
# }
# space_id = os.getenv("WML_SPACE_ID")
# deployment_id = os.getenv("WML_DEPLOYMENT_ID")

# # Initialize IBM WML client
# client = APIClient(wml_credentials)
# client.set.default_space(space_id)

# try:
#     # Load your dataset
#     df = pd.read_csv("Admission_Predict.csv")  # Ensure this matches your actual CSV file

#     # Drop the target and identifier columns
#     df = df.drop(columns=["Serial No.", "Chance of Admit"])

#     # Reorder columns if needed (based on training order)
#     expected_fields = [
#         "GRE Score", "TOEFL Score", "University Rating", "SOP",
#         "LOR", "CGPA", "Research"
#     ]
#     df = df[expected_fields]

#     # Create payload for scoring
#     payload = {
#         "input_data": [
#             {
#                 "fields": df.columns.tolist(),
#                 "values": df.values.tolist()
#             }
#         ]
#     }

#     # Perform scoring
#     response = client.deployments.score(deployment_id, payload)

#     # Print response
#     print("\n✅ Scoring successful. Model predictions:\n")
#     print(json.dumps(response, indent=2))

# except Exception as e:
#     print("❌ Error during scoring:", str(e))
