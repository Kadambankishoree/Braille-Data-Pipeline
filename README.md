# 🧠 Braille Data Pipeline - Accessibility AI Project

This project is a prototype data pipeline for converting unstructured scanned content into structured Braille text, designed to support AI models for accessibility tools.

---

## 📌 Overview

The goal is to create a small ETL pipeline to simulate how Flickdone converts scanned books or digital pages into structured data that can help train Braille translation models. It works in 4 main stages:

1. **Collect**: OCR-ready scanned pages (images)  
2. **Extract & Clean**: Extract text using Tesseract OCR and optionally Gemini/Qwen VLM  
3. **Structure**: Organize extracted text into a clean, paragraph-aligned JSON format  
4. **Translate**: Convert structured text into Braille using Liblouis  

---

## 📁 Project Structure

```
Braille-Data-Pipeline/
│
├── scanned_images/          # Input images (JPEG pages from books)
├── extracted_text/          # Extracted plain text files (from OCR)
├── convert_to_json.py       # Script to create structured JSON
├── convert_to_braille.py    # Script to convert to Braille using Liblouis
├── braille_output.json      # Braille version of structured text
├── final_output.json        # Final JSON after structure
├── README.md                # This file
└── extract_text.py          # OCR extraction logic (using pytesseract)
```

---

## ⚙️ How It Works

### 1️⃣ OCR Text Extraction

Uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) via Python’s `pytesseract` to extract text from scanned images in `/scanned_images`.

```bash
python extract_text.py
```

Text is saved into `/extracted_text`.

---

### 2️⃣ Structure to JSON

Cleans and converts plain text files into structured paragraph-level JSON format.

```bash
python convert_to_json.py
```

Generates: `final_output.json`

---

### 3️⃣ Translate to Braille

Uses Liblouis to convert clean text into Braille.

```bash
python convert_to_braille.py
```

Generates: `braille_output.json`

---

## 📦 Dependencies

Install all dependencies with:

```bash
pip install pytesseract pillow liblouis
```

Make sure **Tesseract OCR** is installed and added to your system PATH.  
Download from: 👉 https://github.com/tesseract-ocr/tesseract/wiki

---

## 🌐 Target Languages

This prototype currently supports **English**, but can be adapted for **Hindi** using different Liblouis tables.

---

## 🎯 Future Enhancements

- Add multilingual support  
- Use VLMs like Gemini or Qwen-VL for enhanced visual extraction  
- Include annotations for tables/images in pages  

---

## 🧑‍💻 Author

**Kadamban Kishore**  
GitHub: [@Kadambankishoree](https://github.com/Kadambankishoree)
