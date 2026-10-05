# AI Cloud Assistant

A small FastAPI service that integrates with Google's Gemini AI to answer questions through a REST API.

## What's actually working

- A FastAPI backend with two endpoints: a health check and an /ask endpoint.
- The /ask endpoint sends a question to Google's Gemini API and returns the AI-generated answer as JSON.
- API key is kept out of the codebase using a .env file (excluded from git via .gitignore).

## How to run it

1. Install dependencies:
   pip3 install fastapi uvicorn google-generativeai python-dotenv

2. Create a .env file with your own Gemini API key:
   GEMINI_API_KEY=your_key_here

3. Run the server:
   uvicorn main:app --reload

4. Test it:
   curl "http://localhost:8000/ask?question=What+is+Docker"

## What I learned

Google updates their Gemini model names fairly often, and older model names (like gemini-1.5-flash) can stop working for new accounts without warning. I had to debug through two outdated model names before landing on a currently supported one (gemini-3.8-flash), reading the actual error messages carefully to find the right fix each time.

## What's next

- Switch from the deprecated google.generativeai package to the newer google.genai package.
- Add a simple frontend or Postman collection to demo the API more easily.
- Containerize with Docker, consistent with my other projects.
