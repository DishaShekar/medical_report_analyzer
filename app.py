
import streamlit as st
import requests

st.title(" AI-Powered Medical Report Analyzer")

report_text = st.text_area("Paste the medical report here:")

if st.button("Analyze Report"):
    if(len(report_text)<=50):
        print("Please enter a valid report to analyze.")
    else:
        response = requests.post("http://127.0.0.1:8000/analyze/", json={"report_text": report_text})

    if response.status_code == 200:
        result = response.json()
        st.subheader(" Summary")
        st.write(result["summary"])
        
        st.subheader(" Predicted Condition")
        st.write(result["predicted_condition"])
    else:
        st.error("Failed to analyze report.")
