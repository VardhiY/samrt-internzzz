# This will be your final main.py for FastAPI backend in SmartSDLC project

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.pdf_parser import read_pdf
from utils.code_generator import generate_code_from_text
from utils.bug_fixer import fix_code_bugs
from utils.test_generator import generate_tests_from_code
from utils.code_summarizer import summarize_code

app = FastAPI()

# CORS setup for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "SmartSDLC backend running"}

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    text = read_pdf(file.file)
    return {"extracted_text": text}

class CodeRequest(BaseModel):
    prompt: str

@app.post("/generate-code/")
def generate_code(data: CodeRequest):
    code = generate_code_from_text(data.prompt)
    return {"generated_code": code}

class BugFixRequest(BaseModel):
    code: str

@app.post("/fix-bugs/")
def fix_bugs(data: BugFixRequest):
    fixed = fix_code_bugs(data.code)
    return {"fixed_code": fixed}

class TestGenRequest(BaseModel):
    code: str

@app.post("/generate-tests/")
def generate_tests(data: TestGenRequest):
    tests = generate_tests_from_code(data.code)
    return {"test_cases": tests}

class SummarizerRequest(BaseModel):
    code: str

@app.post("/summarize-code/")
def summarize(data: SummarizerRequest):
    summary = summarize_code(data.code)
    return {"summary": summary}

