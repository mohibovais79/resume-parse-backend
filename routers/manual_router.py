from fastapi import APIRouter, File, UploadFile

from controllers.manual_controller import ManualController

router = APIRouter()

manual_controller = ManualController()


@router.post("/manual_extraction")
async def manual_extraction(file: UploadFile = File(...)):
    return await manual_controller.manual_extraction(file)
