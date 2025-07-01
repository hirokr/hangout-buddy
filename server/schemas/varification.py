# schemas/verification.py

from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Literal


# 🧾 For image-based ID (University/Workplace) verification
class IDVerificationRequest(BaseModel):
    image_url: HttpUrl
    type: Literal["university", "workplace"]


# 🧾 To request email verification (send code)
class EmailVerificationRequest(BaseModel):
    email: EmailStr


# 🧾 To submit code for email verification
class EmailCodeSubmit(BaseModel):
    email: EmailStr
    code: str
