# 🩺 AI-Powered Medical Report Analyzer

This project uses **FastAPI**, **Streamlit**, and **transformers** to analyze and summarize medical reports in XML or PDF format, and predict the patient's medical condition using natural language processing (NLP).

---

## 🚀 Features

- 🔍 Extracts and reads medical reports (XML and PDF support)
- 🧠 Summarizes medical reports in plain English
- 🤖 Predicts likely patient condition using AI
- 🖼️ User-friendly Streamlit interface
- ⚙️ FastAPI backend for processing and inference

---

## 📁 Project Structure

medical_report_analyzer/
├── backend.py # FastAPI backend (exposes /analyze endpoint)
├── ui.py / app.py # Streamlit frontend (user interface)
├── summarizer.py # Contains summarization and prediction logic
├── reportfiles/ # Folder containing input medical reports (PDF/XML)
├── requirements.txt # List of required Python packages
└── README.md # Project overview (this file)


---

## ⚙️ How to Run the Project

### 1. 📦 Install Required Packages

```bash
pip install -r requirements.txt
If you don't have requirements.txt, you can create it using pip freeze > requirements.txt.

2. 🚀 Start the FastAPI Server
uvicorn backend:app --host 127.0.0.1 --port 8000 --reload
Then open your browser and visit:


http://127.0.0.1:8000/docs
You’ll see the Swagger UI where you can test the API.

3. 🖥️ Run the Streamlit Interface
bash
Copy
Edit
streamlit run ui.py
Enter or paste a medical report in the textbox and click "Analyze Report". You’ll see a summary and condition prediction based on the content.

🧠 Technologies Used
FastAPI – for the backend REST API

Streamlit – for the interactive web UI

Hugging Face Transformers – for summarization and classification

PyMuPDF / fitz – for reading PDFs

xml.etree.ElementTree – for parsing XML files

FAISS (optional) – for semantic search over reports

🔮 Future Enhancements
📂 Upload multiple reports at once

📈 Dashboard view for summarized reports

🧾 Save analysis results to a database

🔄 Fine-tune models on medical data for higher accuracy

🙋‍♀️ Author
Disha Shekar
🔗 GitHub