import os
import fitz  # PyMuPDF
from pathlib import Path
from config import PDF_DIR

def convert_pdf_to_markdown(pdf_path: str, output_dir: str) -> str:
    """Convert a single PDF to Markdown and save it."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    filename = Path(pdf_path).stem + ".md"
    output_path = Path(output_dir) / filename

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return str(output_path)

def convert_all_pdfs_to_markdown(output_dir: str):
    """Convert all PDFs in the PDF_DIR to Markdown and save them to output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    pdf_files = list(Path(PDF_DIR).glob("*.pdf"))

    markdown_files = []
    for pdf_file in pdf_files:
        md_file = convert_pdf_to_markdown(str(pdf_file), output_dir)
        markdown_files.append(md_file)

    return markdown_files
