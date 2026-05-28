from fastapi import FastAPI
from main import run_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI App Compiler is running"}

@app.get("/generate")
def generate(prompt: str):
    return run_pipeline(prompt)