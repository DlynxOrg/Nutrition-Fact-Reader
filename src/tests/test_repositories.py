import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Metadata, OCR
from app.repositories.metadata_repository import MetadataRepository
from app.repositories.ocr_repository import OCRRepository

@pytest.mark.asyncio
async def test_metadata_repository(async_session_maker):
    async with async_session_maker() as async_session:
        repo = MetadataRepository(async_session)

        # Create
        metadata = Metadata(path="test/path", filename="test_file", is_valid=True)
        created_metadata = await repo.create_metadata(metadata)
        assert created_metadata.id is not None

        # Read
        fetched_metadata = await repo.get_metadata(created_metadata.id)
        assert fetched_metadata.filename == "test_file"

        # Update
        await repo.update_metadata(created_metadata.id, {"filename": "updated_file"})
        updated_metadata = await repo.get_metadata(created_metadata.id)
        assert updated_metadata.filename == "updated_file"

        # Delete
        await repo.delete_metadata(created_metadata.id)
        deleted_metadata = await repo.get_metadata(created_metadata.id)
        assert deleted_metadata is None
    repo = MetadataRepository(async_session)

    # Create
    metadata = Metadata(path="test/path", filename="test_file", is_valid=True)
    created_metadata = await repo.create_metadata(metadata)
    assert created_metadata.id is not None

    # Read
    fetched_metadata = await repo.get_metadata(created_metadata.id)
    assert fetched_metadata.filename == "test_file"

    # Update
    await repo.update_metadata(created_metadata.id, {"filename": "updated_file"})
    updated_metadata = await repo.get_metadata(created_metadata.id)
    assert updated_metadata.filename == "updated_file"

    # Delete
    await repo.delete_metadata(created_metadata.id)
    deleted_metadata = await repo.get_metadata(created_metadata.id)
    assert deleted_metadata is None

@pytest.mark.asyncio
async def test_ocr_repository(async_session_maker):
    async with async_session_maker() as async_session:
        repo = OCRRepository(async_session)

        # Create
        ocr = OCR(metadata_id="test_metadata_id", text_extracted="sample text")
        created_ocr = await repo.create_ocr(ocr)
        assert created_ocr.id is not None

        # Read
        fetched_ocr = await repo.get_ocr(created_ocr.id)
        assert fetched_ocr.text_extracted == "sample text"

        # Update
        await repo.update_ocr(created_ocr.id, {"text_extracted": "updated text"})
        updated_ocr = await repo.get_ocr(created_ocr.id)
        assert updated_ocr.text_extracted == "updated text"

        # Delete
        await repo.delete_ocr(created_ocr.id)
        deleted_ocr = await repo.get_ocr(created_ocr.id)
        assert deleted_ocr is None
    repo = OCRRepository(async_session)

    # Create
    ocr = OCR(metadata_id="test_metadata_id", text_extracted="sample text")
    created_ocr = await repo.create_ocr(ocr)
    assert created_ocr.id is not None

    # Read
    fetched_ocr = await repo.get_ocr(created_ocr.id)
    assert fetched_ocr.text_extracted == "sample text"

    # Update
    await repo.update_ocr(created_ocr.id, {"text_extracted": "updated text"})
    updated_ocr = await repo.get_ocr(created_ocr.id)
    assert updated_ocr.text_extracted == "updated text"

    # Delete
    await repo.delete_ocr(created_ocr.id)
    deleted_ocr = await repo.get_ocr(created_ocr.id)
    assert deleted_ocr is None