# schemas/comment.py

from pydantic import BaseModel
from datetime import datetime


# 🧾 To create a comment on a post
class CommentCreate(BaseModel):
    post_id: str
    message: str


# 🧾 Output comment object
class CommentOut(BaseModel):
    id: str
    user_id: str
    post_id: str
    message: str
    created_at: datetime

    class Config:
        orm_mode = True
