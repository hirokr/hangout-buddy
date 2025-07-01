# models/verification.py

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Enum
from .base import BaseModel
from datetime import datetime

class Verification(BaseModel):
    __tablename__ = "verifications"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    type: Mapped[str] = mapped_column(Enum("email", "university", "workplace", name="verification_types"))
    value: Mapped[str]  # email or image URL or code
    is_verified: Mapped[bool] = mapped_column(default=False)
    submitted_at: Mapped[datetime]
