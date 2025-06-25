from fastapi import FastAPI
from pydantic import BaseModel
from pyautomate_ai.ai_models.document_classifier import classify_document

app = FastAPI()

class DocumentRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.post("/classify")
def classify(request: DocumentRequest):
    label = classify_document(request.text)
    return {"label": label} 