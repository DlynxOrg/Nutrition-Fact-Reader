import os
from sqlmodel import create_engine, Session
from models.models import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


from threading import Lock

class DatabaseConnection:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(DatabaseConnection, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.connection_string = os.getenv("OCR_PSQL_DB_URL")
        if not self.connection_string:
            raise ValueError("DATABASE_URL environment variable is not set.")
        self.engine = create_engine(self.connection_string, echo=True)
        self._initialized = True

    def create_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        with Session(self.engine) as session:
            yield session