from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum as PyEnum  # Use Python's Enum

class CallStatus(PyEnum):
    ringing = "ringing"
    active = "active"
    ended = "ended"
    rejected = "rejected"

class Call(BaseModel):
    id: str
    caller_id: str
    receiver_id: str
    status: CallStatus
    started_at: datetime
    ended_at: Optional[datetime]
