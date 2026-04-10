import os

from sqlalchemy import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://esbot_user:esbot_password@localhost:5432/esbot",
)

engine = create_engine(DATABASE_URL)
