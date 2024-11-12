from fastapi import APIRouter, File, UploadFile

from controllers.resume_controller import Resume, ResumeController
from models.schema import AutomaticExtractionModel

router = APIRouter()

# Create an instance of ResumeController
resume_controller = ResumeController()


@router.post("/upload_resume", response_model=AutomaticExtractionModel)
async def upload_resume(file: UploadFile = File(...)):
    return await resume_controller.upload_resume(file)
