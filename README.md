# 🎓 IBM AutoAI Admission Prediction Model

This project uses IBM Watsonx's AutoAI to automatically build and deploy a machine learning model that predicts the probability of a student's admission to graduate school.

---

## 💡 Project Features

- ✅ AutoAI-based pipeline generation (no manual ML tuning needed)
- ✅ Ridge Regression model deployed via Watson Machine Learning (WML)
- ✅ REST API endpoint for real-time prediction
- ✅ Python scoring script using the `ibm-watson-machine-learning` SDK
- ✅ `.env`-based config management for API security

---

## 🔍 Model Usage Modes

You can run the model in two modes:

1. **🌐 Deployed API Mode**  
   - Set `USE_API = True` in `score_model.py`
   - Provide your `API key`, `deployment ID`, and `space ID` in a `.env` file

2. **🖥️ Local (Offline) Mode** *(optional)*  
   - Export the model pipeline (`autoai_model.pkl`) from the notebook
   - Use it to predict locally without calling WML

---

## 🚀 How to Use

## ⚙️ Setup Instructions

To avoid Windows path-length errors:

1. Clone this repo to a **short directory**, e.g. `C:\ai_project`
2. Open terminal and run:

```bash
python -m venv venv
venv\Scripts\activate   # on Windows
pip install -r requirements.txt
python score_model.py
git clone https://github.com/your-username/watsonx-autoai-admission.git
cd watsonx-autoai-admission