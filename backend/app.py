from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import backend.models
from backend.database import create_db_and_tables
from backend.services.endpoint import router as sessions_router, register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sessions_router, prefix="/api/v1")
register_exception_handlers(app)


@app.get("/")
def hello() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/api/v1/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
