import fitz  # PyMuPDF
import os
import json

def extract_outline(file_path):
    doc = fitz.open(file_path)
    outline = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    text = " ".join([span["text"] for span in line["spans"]]).strip()
                    if text and len(text) < 70:
                        outline.append({
                            "level": "H1",
                            "text": text,
                            "page": page_num + 1
                        })

    return {
        "title": os.path.basename(file_path),
        "outline": outline
    }

input_dir = "/app/input"
output_dir = "/app/output"

for file in os.listdir(input_dir):
    if file.endswith(".pdf"):
        result = extract_outline(os.path.join(input_dir, file))
        with open(os.path.join(output_dir, file.replace(".pdf", ".json")), "w") as f:
            json.dump(result, f, indent=2)
