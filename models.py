from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

class TaskDB(Base):
    __tablename__ = "tasks"
    ID = Column(String, primary_key=True, index=True)
    Title = Column(String, index=True)
    Description = Column(String)
    Done = Column(Boolean, default=False)
    ToDo = Column(DateTime)
    CreatedAt = Column(DateTime, default=datetime.utcnow)
    UpdatedAt = Column(DateTime, default=datetime.utcnow)
    DeletedAt = Column(DateTime, nullable=True)

class Task(BaseModel):
    ID: str
    Title: str
    Description: str
    Done: bool
    ToDo: datetime
    CreatedAt: datetime
    UpdatedAt: datetime
    DeletedAt: Optional[datetime] = None

class TaskIn(BaseModel):
    Title: str
    Description: str
    Done: bool
    ToDo: datetime

class TaskUpdate(BaseModel):
    Title: Optional[str] = None
    Description: Optional[str] = None
    Done: Optional[bool] = None
    ToDo: Optional[datetime] = None