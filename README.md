AI Chatbox Challenge

This is a simple AI chatbot backend built with FastAPI.
It allows users to sign up / log in using email, and each user can have a maximum of 3 active conversations.
If a new one is started after the limit, the oldest conversation will be deleted automatically.

The chatbot uses an external AI API (I assumed OpenAI, but it can be swapped with any other LLM like HuggingFace).

Features

User sign-in and sign-up (basic email auth).

Each user can only keep 3 conversations at a time.

Auto-delete oldest conversation when a new one starts.

REST API built with FastAPI.

Easily extendable to plug in your own AI provider.

Assumptions

Since the requirement didn’t mention which AI agent to use,
I used a placeholder for OpenAI (can be replaced with HuggingFace or other providers).
The goal was to focus more on the backend logic and conversation management.

Installation & Run (Local)

Clone the repo

git clone https://github.com/satty0304/AI-chatbox-challenge.git
cd AI-chatbox-challenge


Create virtual environment & install dependencies

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt


Run server

uvicorn main:app --reload


Open in browser:

http://127.0.0.1:8000/docs


You’ll see the interactive Swagger API docs.

API Endpoints

POST /signup → Register new user

POST /login → Login with email

POST /chat → Start conversation with AI (auto-manages limit 3)

GET /conversations → List user’s active conversations

Bonus (not included yet, but possible)

Deployment (e.g., on Render/Heroku)

Postman collection

Front-end (React/Next.js)

Letting users bring their own AI key

License

MIT# AI-chatbox-challenge
AI Chatbot backend built with FastAPI. Supports user login and max 3 conversations.
