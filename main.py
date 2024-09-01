""" App entry point.
"""
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi import HTTPException, Request, FastAPI, status
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routes.user import user_router
from api.utils.error_handlers import (integrity_error_handler, general_exception_handler, http_exception_handler, validation_exception_handler)
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
from api.v1.routes import api_version_one

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

# Set up email templates and css static files
email_templates = Jinja2Templates(directory='api/templates/email_templates')


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

# Register routers
app.include_router(api_version_one)


# Register exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(IntegrityError, integrity_error_handler)
app.add_exception_handler(Exception, general_exception_handler)



if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)