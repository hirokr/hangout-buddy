# models/user.py

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from typing import List, Optional
from .base import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[Optional[str]]
    
    avatar: Mapped[Optional[str]]
    bio: Mapped[Optional[str]]
    location: Mapped[Optional[str]]

    provider: Mapped[Optional[str]]  # "google", "facebook", etc.
    provider_id: Mapped[Optional[str]]
    is_verified: Mapped[bool] = mapped_column(default=False)
    verified_fields: Mapped[List[str]] = mapped_column(default=[])

    university: Mapped[Optional[str]]
    workplace: Mapped[Optional[str]]
    interests: Mapped[Optional[List[str]]] = mapped_column(default=[])

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    sent_messages = relationship("ChatMessage", back_populates="sender", foreign_keys="ChatMessage.sender_id")
    received_messages = relationship("ChatMessage", back_populates="receiver", foreign_keys="ChatMessage.receiver_id")
