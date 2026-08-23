from fastapi import FastAPI, UploadFile, File, Form
from sqlmodel import Session, select
from pathlib import Path
import shutil
import json

from .database import create_db, engine
from .models import Candidate
from .parser import extract_text_from_pdf, extract_text_from_txt
from .llm import analyze_resume, match_resume

app = FastAPI(
    title="Smart Resume Screener",
    description="AI-powered resume screening and job matching system"
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.on_event("startup")
def startup():
    create_db()


@app.get("/")
def home():
    return {
        "message": "Smart Resume Screener API is running"
    }
