from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel, create_engine
import backend.models 
import backend.database

backend.database.engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
SQLModel.metadata.create_all(backend.database.engine)
