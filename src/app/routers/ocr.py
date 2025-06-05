from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from services.image_service import ImageService
from database.connection import DatabaseConnection
from schemas.metadata_schema import MetadataValidationSchema
from tasks.example_task import extract_text_task

router = APIRouter()
db = DatabaseConnection()

@router.post("/extract-text/")
async def extract_text(metadata: MetadataValidationSchema):
    task_result = await extract_text_task.aio_run(metadata)
    return {"content": task_result}