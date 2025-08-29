from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ConversationCreate(BaseModel):
    message: str

class ConversationResponse(BaseModel):
    message: str
    response: str
