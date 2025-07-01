# schemas/auth.py

from pydantic import BaseModel, EmailStr
from typing import Literal, Optional


# 🧾 Email/Password Login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# 🧾 Social Login Input
class OAuthLoginRequest(BaseModel):
    provider: Literal["google", "facebook", "twitter"]
    access_token: str


# 🧾 Common Token Response (JWT)
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
