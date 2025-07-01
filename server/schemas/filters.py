# schemas/filters.py

from pydantic import BaseModel
from typing import Optional, List


# 🧾 Used in feed filter/discovery endpoints
class DiscoveryFilters(BaseModel):
    area: Optional[str]
    university: Optional[str]
    workplace: Optional[str]
    interests: Optional[List[str]]
    country: Optional[str]
    past_activity: Optional[str]
