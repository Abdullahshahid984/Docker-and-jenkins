import argparse
import re
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

def clean_text(text):
    """Removes invalid characters for reportlab and escapes special symbols"""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    return text.strip()

def docx_to_pdf(docx_path, pdf_path):
    doc = Document(docx_path)
    pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
    
    styles = getSampleStyleSheet()
    story = []

    # Define Styles
    title_style = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        fontSize=18,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )
    
    normal_style = styles["Normal"]
    normal_style.fontSize = 12
    normal_style.leading = 14

    for para in doc.paragraphs:
        text = clean_text(para.text)  # Fix encoding issues
        
        if not text:  # Skip empty lines
            continue

        if para.style.name.startswith("Heading"):
            p = Paragraph(text, title_style)
        else:
            p = Paragraph(text, normal_style)

        story.append(p)
        story.append(Spacer(1, 0.2 * inch))

    pdf.build(story)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .docx to PDF with Formatting")
    parser.add_argument("docx_file", help="Path to the input .docx file")
    parser.add_argument("pdf_file", help="Path to the output PDF file")
    args = parser.parse_args()

    docx_to_pdf(args.docx_file, args.pdf_file)
