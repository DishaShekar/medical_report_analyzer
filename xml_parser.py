import xml.etree.ElementTree as ET
import os

def extract_text_from_xml(xml_file):
    """Extracts relevant medical report text from XML files."""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        abstract_elements = root.findall(".//AbstractText")  # Extract sections

        extracted_text = []
        for elem in abstract_elements:
            label = elem.attrib.get("Label", "General")  # Section Label
            text = elem.text.strip() if elem.text else ""
            extracted_text.append(f"{label}: {text}")

        return "\n".join(extracted_text) if extracted_text else None
    except Exception as e:
        print(f"❌ Error reading {xml_file}: {e}")
        return None

# Load all reports from folder
report_folder = r"C:\Users\91797\Downloads\reportfiles\Medical-Reports\reports"
medical_reports = []

for file in os.listdir(report_folder):
    if file.endswith(".xml"):
        text = extract_text_from_xml(os.path.join(report_folder, file))
        if text:
            medical_reports.append(text)

# Save extracted reports for processing
with open("medical_reports.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(medical_reports))

print(f" Extracted {len(medical_reports)} medical reports!")
