from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import summarize_report, predict_condition

app = FastAPI()

class MedicalReportRequest(BaseModel):
    report_text: str

@app.post("/analyze/")
def analyze_report(request: MedicalReportRequest):
    summary = summarize_report(request.report_text)
    condition = predict_condition(request.report_text)
    return {"summary": summary, "predicted_condition": condition}
