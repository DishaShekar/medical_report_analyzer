from transformers import pipeline

# ✅ Load Summarization Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ✅ Load Medical Diagnosis Model (Replace with a trained one)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def summarize_report(report_text):
    """Summarizes a medical report."""
    summary = summarizer(report_text, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

def predict_condition(report_text):
    condition_labels = [
        "Flu", "Pneumonia", "Chronic Kidney Disease", "Heart Disease",
        "Lung Infection", "Fracture", "Arthritis", "Diabetes", "Hypertension",
        "Jaundice", "Malaria", "Dengue", "Typhoid", "Chickenpox", "Measles",
        "Hepatitis", "Tuberculosis", "Asthma", "Bronchitis", "Cancer", "Stroke",
        "Ulcer", "Appendicitis", "Diarrhea", "Constipation", "Food Poisoning",
        "Migraine", "Sinusitis", "Tonsillitis"
    ]

    result = classifier(report_text, candidate_labels=condition_labels)

    top_label = result["labels"][0]
    top_score = result["scores"][0]

    # 👇 Threshold logic: if model is not confident enough, return "None"
    if top_score < 0.5:
        return "None"
    else:
        return top_label


if __name__ == "__main__":
    # Test with sample report
    with open("medical_reports.txt", "r", encoding="utf-8") as f:
        sample_report = f.readlines()[0]

    print(" Original Report:\n", sample_report)
    print("\n Summary:\n", summarize_report(sample_report))
    print("\n Predicted Condition:", predict_condition(sample_report))
