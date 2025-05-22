 HEAD
# Braille AI Data Pipeline

## 📌 Overview
This ETL pipeline extracts text from scanned images, structures it into JSON, and translates it into Braille using Liblouis.

## 📁 Structure
- `scanned_images/`: Input image files (JPG/PNG)
- `extracted_text/`: OCR output text
- `final_output.json`: Structured JSON format
- `braille_output.txt`: Braille converted text

## 🔧 Requirements
- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Python Packages:

# Braille-Data-Pipeline
ETL pipeline to convert scanned images to Braille using OCR and Liblouis

