""" App entry point.
"""
import uvicorn
from fastapi import HTTPException, Request, FastAPI, status
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routes.user import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """ Lifespan function definition
    """
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Learnify",
    description="Learnify API, the backend API for the Learnify web application",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Home"])
async def get_root() -> dict:
    return {"message": "I am the Learnify API, the backend API for the Learnify web application."}

app.include_router(user_router, prefix="/api/v1")




if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)