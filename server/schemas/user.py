# schemas/user.py

from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, Literal, List
from datetime import datetime


# 🧾 User Registration
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: Optional[str]  # Optional for social login


# 🧾 Public User Info
class UserPublic(BaseModel):
    id: str
    name: str
    email: EmailStr
    avatar: Optional[HttpUrl]
    is_verified: bool
    verified_fields: List[str] = []
    created_at: datetime
    provider: Optional[str]

    class Config:
        orm_mode = True


# 🧾 Profile Update
class UserUpdate(BaseModel):
    name: Optional[str]
    avatar: Optional[HttpUrl]
    bio: Optional[str]
    location: Optional[str]
    interests: Optional[List[str]]
    university: Optional[str]
    workplace: Optional[str]


# 🧾 For linked OAuth providers
class LinkedOAuthAccount(BaseModel):
    provider: Literal["google", "facebook", "twitter"]
    provider_id: str
