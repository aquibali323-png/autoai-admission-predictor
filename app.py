import streamlit as st
from ibm_watson_machine_learning import APIClient
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

wml_credentials = {
    "url": os.getenv("WML_URL"),
    "apikey": os.getenv("WML_APIKEY")
}
space_id = os.getenv("WML_SPACE_ID")
deployment_id = os.getenv("WML_DEPLOYMENT_ID")

client = APIClient(wml_credentials)
client.set.default_space(space_id)

st.title("🎓 Graduate Admission Predictor")

# Input form
cgpa = st.slider("CGPA", 6.0, 10.0, 8.0)
gre = st.slider("GRE Score", 260, 340, 310)
lor = st.slider("LOR (out of 5)", 1.0, 5.0, 3.0)
research = st.radio("Research Experience", [0, 1])
sop = st.slider("SOP (out of 5)", 1.0, 5.0, 3.0)
toefl = st.slider("TOEFL Score", 80, 120, 100)
serial = st.number_input("Serial No.", 1, 500, 123)
uni_rating = st.slider("University Rating", 1, 5, 3)
sop_text = st.slider("Statement of Purpose", 1.0, 5.0, 3.5)

if st.button("Predict"):
    input_fields = ["CGPA", "GRE Score", "LOR", "Research", "SOP", "TOEFL Score", "Serial No.", "University Rating", "Statement of Purpose"]
    input_values = [[cgpa, gre, lor, research, sop, toefl, serial, uni_rating, sop_text]]

    payload = {"input_data": [{"fields": input_fields, "values": input_values}]}

    try:
        response = client.deployments.score(deployment_id, payload)
        result = response['predictions'][0]['values'][0][0]
        st.success(f"🎯 Predicted Chance of Admission: **{round(result * 100, 2)}%**")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")