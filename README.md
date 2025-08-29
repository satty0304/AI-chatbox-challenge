AI Chatbox Challenge
This is a simple AI chatbot backend built with FastAPI.
It allows users to sign up / log in using email, and each user can have a maximum of 3 active conversations.
If a new one is started after the limit, the oldest conversation will be deleted automatically.
The chatbot uses an external AI API (I assumed HuggingFace).
Features
User sign-in and sign-up (basic email auth).
Each user can only keep 3 conversations at a time.
Auto-delete oldest conversation when a new one starts.
REST API built with FastAPI.
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
MIT
