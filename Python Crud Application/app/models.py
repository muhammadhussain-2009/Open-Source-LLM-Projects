import uuid 
from datetime import datetime 
from sqlalchemy import Column, String, DateTime, func, text
from sqlalchemy.orm import Mapped, mapped_column
from uuid_utils.compat import uuid7
from app.database import Base 

#Models 
class Task(Base):
    id: Mapped[uuid.UUID]=mapped_column(
        primary_key=True,
        default=uuid7
    )
    title: Mapped[str]=mapped_column(String(200))
    description: Mapped[str | None]=mapped_column(String(200))
    completed: Mapped[bool]=mapped_column(
        default=False,
        server_default=text("false")
    )
    created: Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated: Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    def __repr__(self) -> str:
        return f"Task(id={self.id}, title={self.title})"