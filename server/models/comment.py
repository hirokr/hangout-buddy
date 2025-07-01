# models/comment.py

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from .base import BaseModel

class Comment(BaseModel):
    __tablename__ = "comments"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[str] = mapped_column(ForeignKey("posts.id"))
    message: Mapped[str]

    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
