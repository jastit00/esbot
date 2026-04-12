from contextlib import asynccontextmanager
from fastapi import FastAPI
import backend.models
from backend.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def hello() -> dict[str, str]:
    return {"message": "Hello World"}
