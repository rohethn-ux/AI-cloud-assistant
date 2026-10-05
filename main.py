import os
from fastapi import FastAPI
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()
model = genai.GenerativeModel("gemini-3.8-flash")

@app.get("/")
def home():
    return {"message": "AI Cloud Assistant is running"}

@app.get("/ask")
def ask(question: str):
    response = model.generate_content(question)
    return {"question": question, "answer": response.text}
