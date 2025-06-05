
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from services.image_service import ImageService
from services.file_service import FileService
from database.connection import DatabaseConnection
from schemas.metadata_schema import MetadataValidationSchema
from tasks.example_task import upload_image_task, validate_image_task

router = APIRouter()
db = DatabaseConnection()

@router.post("/upload-image/")
async def upload_image(file: UploadFile):
    file_service = FileService()
    metadata_schema = await file_service.save_image(file)
    task_result = await upload_image_task.aio_run(metadata_schema)
    return {"metadata": task_result}

@router.post("/validate-image/")
async def validate_image(metadata: MetadataValidationSchema):
    task_result = await validate_image_task.aio_run(metadata)
    return {"is_valid": task_result}