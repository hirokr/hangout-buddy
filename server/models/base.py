# models/base.py

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
import uuid

class Base(DeclarativeBase):
    pass

# 🧾 UUID-enabled abstract base model with timestamps
class BaseModel(Base):
    __abstract__ = True

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())
