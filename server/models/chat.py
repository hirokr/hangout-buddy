# models/chat.py

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum
from typing import Optional
from datetime import datetime
from .base import BaseModel

class ChatMessage(BaseModel):
    __tablename__ = "chat_messages"

    sender_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    receiver_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    
    # Message content or media URL
    message: Mapped[Optional[str]]
    media_url: Mapped[Optional[str]]
    media_type: Mapped[Optional[str]] = mapped_column(
        Enum("image", "video", "file", "none", name="media_types"),
        default="none"
    )

    timestamp: Mapped[datetime]

    sender = relationship("User", back_populates="sent_messages", foreign_keys=[sender_id])
    receiver = relationship("User", back_populates="received_messages", foreign_keys=[receiver_id])
