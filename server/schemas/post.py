# schemas/post.py

from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime as date


# 🧾 Create a hangout post
class PostCreate(BaseModel):
    activity: str
    location: str
    datetime: date
    description: Optional[str]
    anonymous: bool = False
    visibility: Literal["public", "university", "locality"] = "public"


# 🧾 For post edits
class PostUpdate(BaseModel):
    activity: Optional[str]
    location: Optional[str]
    datetime: Optional[date]
    description: Optional[str]
    visibility: Optional[Literal["public", "university", "locality"]]


# 🧾 Output schema for feed
class PostOut(BaseModel):
    id: str
    user_id: str
    activity: str
    location: str
    datetime: date
    description: Optional[str]
    anonymous: bool
    visibility: str
    created_at: date

    class Config:
        orm_mode = True
