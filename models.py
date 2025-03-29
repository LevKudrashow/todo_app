from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    ID: str
    Title: str
    Description: str
    Done: bool
    ToDo: datetime
    CreatedAt: datetime
    UpdatedAt: datetime
    DeletedAt: Optional[datetime] = None

class TaskCreate(BaseModel):
    Title: str
    Description: str
    ToDo: datetime

class TaskUpdate(BaseModel):
    Title: Optional[str] = None
    Description: Optional[str] = None
    Done: Optional[bool] = None
    ToDo: Optional[datetime] = None