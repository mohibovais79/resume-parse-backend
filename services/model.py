import io
import os

import fitz
import pymupdf
from docx import Document
from fastapi import HTTPException, UploadFile
from openai import OpenAI
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

from logs.logging import setup_logger

from .prompt import return_prompt
from .response_format import format


def return_response(resume_text: str):
    logger = setup_logger("resume_service")

    api_key = os.getenv("OPENAI_API_KEY")

    prompt = return_prompt(resume_text)
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You extract name, phone number, email, address, education details, work experience, skills, and certifications into JSON data.",
            },
            {"role": "user", "content": prompt},
        ],
        response_format=format,
    )
    logger.info("response by api", response.choices[0].message.content)
    return response.choices[0].message.content


async def process_resume(file_path: str) -> str:
    # Read the file content based on file type
    if file_path.endswith(".pdf"):
        # Open the PDF file from file path
        pdf_document = fitz.open(file_path)
        text = ""

        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            page_text = page.get_text("text")

            if page_text.strip():
                text += page_text
            else:
                image = page.get_pixmap().pil_image()
                engine = RapidOCR()
                result, elapse = engine(image)
                extracted_texts = [item[1] for item in result]
                text += " ".join(extracted_texts)

        return text

    elif file_path.endswith(".docx"):
        # Open the DOCX file from file path
        with open(file_path, "rb") as doc_file:
            doc = Document(doc_file)
            full_text = [para.text for para in doc.paragraphs]

        return "\n".join(full_text)

    elif file_path.endswith((".jpg", ".jpeg", ".png")):
        # Open image from file path
        image = Image.open(file_path)
        engine = RapidOCR()
        result, elapse = engine(image)
        extracted_texts = [item[1] for item in result]
        text = ""
        for extracted_text in extracted_texts:
            text = text + extracted_text
        return text

    else:
        return "Unsupported file type"
