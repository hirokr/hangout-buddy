# schemas/chat.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 🧾 Message input via WebSocket or HTTP
# schemas/chat.py

class ChatMessageCreate(BaseModel):
    receiver_id: str
    message: Optional[str]
    media_url: Optional[str]
    media_type: Optional[str] = "none"


# 🧾 Message output for frontend rendering
class ChatMessageOut(BaseModel):
    id: str
    sender_id: str
    receiver_id: str
    message: str
    timestamp: datetime

    class Config:
        orm_mode = True
