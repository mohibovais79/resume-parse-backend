from fastapi import HTTPException, UploadFile
from PIL import Image

from utils.utils import allowed_file, ocr_extraction


class CropImage:
    def __init__(self) -> None:
        self.images = []

    async def manual_extraction(self, file: UploadFile):
        if not allowed_file(file.filename):
            raise HTTPException(
                status_code=400, detail="File type not allowed. Please upload a .docx, .png, .jpg, .jpeg, or .pdf file."
            )

        image = Image.open(file.file)
        text = ocr_extraction(image)
        self.images.append(image)
        return text
