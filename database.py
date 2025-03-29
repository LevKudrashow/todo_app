from datetime import datetime, timezone
from typing import Dict
from typing import Optional
from uuid import uuid4
from models import Task, TaskCreate, TaskUpdate

# In-memory database
db: Dict[str, Task] = {}

def get_tasks():
    """Get all active tasks (not deleted)"""
    return [task for task in db.values() if task.DeletedAt is None]

def get_task(task_id: str) -> Optional[Task]:
    """Get a specific task by ID if it exists and isn't deleted"""
    task = db.get(task_id)
    return task if task and task.DeletedAt is None else None

def create_task(task_data: TaskCreate) -> Task:
    """Create a new task with generated ID and timestamps"""
    task_id = str(uuid4())
    now = datetime.now(timezone.utc)
    task = Task(
        ID=task_id,
        Title=task_data.Title,
        Description=task_data.Description,
        Done=False,
        ToDo=task_data.ToDo,
        CreatedAt=now,
        UpdatedAt=now,
        DeletedAt=None
    )
    db[task_id] = task
    return task

def update_task(task_id: str, task_data: TaskUpdate) -> Optional[Task]:
    """Update an existing task"""
    if task_id not in db:
        return None
    
    task = db[task_id]
    if task.DeletedAt is not None:
        return None
    
    update_data = task_data.dict(exclude_unset=True)
    
    if 'Title' in update_data:
        task.Title = update_data['Title']
    if 'Description' in update_data:
        task.Description = update_data['Description']
    if 'Done' in update_data:
        task.Done = update_data['Done']
    if 'ToDo' in update_data:
        task.ToDo = update_data['ToDo']
    
    task.UpdatedAt = datetime.now(timezone.utc)
    db[task_id] = task
    return task

def delete_task(task_id: str) -> Optional[Task]:
    """Soft delete a task by setting DeletedAt timestamp"""
    if task_id not in db:
        return None
    
    task = db[task_id]
    if task.DeletedAt is not None:
        return None
    
    task.DeletedAt = datetime.now(timezone.utc)
    db[task_id] = task
    return task