from fastapi import HTTPException, UploadFile
from pydantic import BaseModel

from services.resume_service import Resume, ResumeService, ResumeUpload


class ResumeController:
    def __init__(self) -> None:
        self.resume_service = ResumeService()

    async def upload_resume(self, file: UploadFile):
        try:
            return await self.resume_service.upload_resume(file)
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
    
