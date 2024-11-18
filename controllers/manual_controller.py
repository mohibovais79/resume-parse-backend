from fastapi import UploadFile
from PIL import Image

from services.manual_service import CropImage


class ManualController:
    def __init__(self) -> None:
        self.crop_image = CropImage()

    async def manual_extraction(self, file: UploadFile):
        return await self.crop_image.manual_extraction(file)
