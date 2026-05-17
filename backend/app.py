from contextlib import asynccontextmanager
from fastapi import FastAPI
import backend.models
from backend.database import create_db_and_tables
from backend.services.endpoint import router as sessions_router, register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(sessions_router)
register_exception_handlers(app)


@app.get("/")
def hello() -> dict[str, str]:
    return {"message": "Hello World"}
