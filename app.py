import streamlit as st
import requests
from dotenv import load_dotenv
import os
import json

# ✅ Load environment variables
load_dotenv()
API_KEY = os.getenv("WML_APIKEY")
DEPLOYMENT_URL = os.getenv("WML_DEPLOYMENT_URL")

# 🔍 Debug print
if not API_KEY or not DEPLOYMENT_URL:
    st.error("❌ Missing API credentials. Check your .env file.")
    st.stop()

# ✅ Get IBM ML token
def get_token():
    url = 'https://iam.cloud.ibm.com/identity/token'
    data = {"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
    try:
        res = requests.post(url, data=data)
        res.raise_for_status()
        return res.json()["access_token"]
    except Exception as e:
        st.error(f"❌ Failed to get token: {e}")
        return None

# ✅ Streamlit UI
st.set_page_config(page_title="🎓 Admission Predictor", layout="centered")
st.title("🎓 Graduate Admission Predictor")
st.markdown("Fill in your academic info to predict your chance of admission.")

with st.form("input_form"):
    gre = st.slider("GRE Score", 260, 340, 320)
    toefl = st.slider("TOEFL Score", 80, 120, 110)
    rating = st.selectbox("University Rating", [1, 2, 3, 4, 5])
    sop = st.slider("SOP (Statement of Purpose)", 1.0, 5.0, 3.5, 0.5)
    lor = st.slider("LOR (Letter of Recommendation)", 1.0, 5.0, 3.0, 0.5)
    cgpa = st.slider("CGPA", 6.0, 10.0, 8.5, 0.1)
    research = st.radio("Research Experience", [0, 1])
    submitted = st.form_submit_button("Predict")

if submitted:
    token = get_token()
    if token:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        # ✅ Match exact order of features used in training
        fields = [
            "Serial No.", "GRE Score", "TOEFL Score", "University Rating",
            "SOP", "LOR ", "CGPA", "Research"
        ]
        values = [[1, gre, toefl, rating, sop, lor, cgpa, research]]

        payload = {
            "input_data": [
                {
                    "fields": fields,
                    "values": values
                }
            ]
        }

        try:
            res = requests.post(DEPLOYMENT_URL, json=payload, headers=headers)
            res.raise_for_status()
            prediction = res.json()["predictions"][0]["values"][0][0]
            st.success(f"🎯 Your predicted chance of admission is **{prediction:.2%}**")
        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")
            st.text(res.text)
