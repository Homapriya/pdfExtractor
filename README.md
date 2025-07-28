# PDF Outline Extractor (Adobe Hackathon Round 1)

This project extracts the section headings from input PDF files and scores them based on relevance to a given persona and job-to-be-done.

---

## 🚀 How It Works

1. Accepts one or more PDFs placed in the `input/` directory.
2. Extracts text and detects section headings using rules (not just font size).
3. Scores headings against a user persona and job-to-be-done.
4. Outputs a ranked list of relevant sections in `output/result.json`.

---

## 🧠 Approach

- Used **PyMuPDF** to parse PDFs and extract text blocks.
- Implemented basic heuristics for **heading detection**:
  - Font size and style
  - Line spacing
  - Capitalization
  - Position in the document
- Basic **keyword matching** to evaluate relevance (could be replaced by LLMs in full version).
- JSON output includes document name, headings, scores, and text snippets.

---

## 📂 Folder Structure

