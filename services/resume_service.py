import json
import os

from fastapi import HTTPException, UploadFile
from pydantic import BaseModel

from logs.logging import setup_logger
from services.model import process_resume, return_response
from utils.utils import allowed_file


class ResumeUpload(BaseModel):
    resume: str


class Resume(ResumeUpload):
    id: int


class ResumeService:
    def __init__(self) -> None:
        self.resumes = []

    async def upload_resume(self, file: UploadFile):
        logger = setup_logger("resume_service")
        if not allowed_file(file.filename):
            raise HTTPException(
                status_code=400, detail="File type not allowed. Please upload a .docx, .png, .jpg, .jpeg, or .pdf file."
            )

        resume_file_path = f"uploads/{file.filename}"
        os.makedirs(os.path.dirname(resume_file_path), exist_ok=True)

        with open(resume_file_path, "wb") as out_file:
            content = await file.read()
            out_file.write(content)

        new_resume = Resume(id=len(self.resumes) + 1, resume=file.filename)
        extracted_text = await process_resume(resume_file_path)
        logger.info("text extracted by ocr ", extracted_text)

        response_string = return_response(extracted_text)
        response = json.loads(response_string)
        logger.info("response by api after normalizing", response)

        self.resumes.append(new_resume)

        return response
