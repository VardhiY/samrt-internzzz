from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from utils.pdf_parser import read_pdf
from utils.code_generator import generate_code_from_text
from utils.bug_fixer import fix_code_bugs
from utils.test_generator import generate_tests_from_code
from utils.code_summarizer import summarize_code

app = FastAPI()

# Enable CORS (for frontend-backend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root health check
@app.get("/")
def root():
    return {"message": "SmartSDLC backend running"}

# ------------------ Requirement Extractor ------------------
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    text = read_pdf(file.file)
    print("Extracted Text:", text)
    return {"extracted_text": text}

# ------------------ Code Generator ------------------
class CodeRequest(BaseModel):
    prompt: str

@app.post("/generate-code/")
def generate_code(data: CodeRequest):
    code = generate_code_from_text(data.prompt)
    return {"generated_code": code}

# ------------------ Bug Fixer ------------------
@app.post("/fix-bugs/")
def fix_bugs(data: CodeRequest):
    fixed_code = fix_code_bugs(data.prompt)
    return {"fixed_code": fixed_code}

# ------------------ Test Generator ------------------
@app.post("/generate-tests/")
def generate_tests(data: CodeRequest):
    tests = generate_tests_from_code(data.prompt)
    return {"test_cases": tests}

# ------------------ Code Summarizer ------------------
@app.post("/summarize-code/")
def summarize(data: CodeRequest):
    summary = summarize_code(data.prompt)
    return {"summary": summary}
