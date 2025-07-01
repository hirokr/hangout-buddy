# models/post.py

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Enum
from datetime import datetime
from typing import Optional
from .base import BaseModel

class Post(BaseModel):
    __tablename__ = "posts"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    activity: Mapped[str]
    location: Mapped[str]
    datetime: Mapped[datetime]
    description: Mapped[Optional[str]]
    anonymous: Mapped[bool] = mapped_column(default=False)
    visibility: Mapped[str] = mapped_column(Enum("public", "university", "locality", name="visibility_types"))

    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
