from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Task, TaskCreate, TaskUpdate
from database import get_tasks, get_task, create_task, update_task, delete_task
import uvicorn

app = FastAPI(
    title="ToDo API",
    description="A simple ToDo application with FastAPI",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url=None
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tasks", response_model=list[Task], tags=["tasks"])
async def read_tasks():
    """Get all active tasks"""
    return get_tasks()

@app.get("/tasks/{task_id}", response_model=Task, tags=["tasks"])
async def read_task(task_id: str):
    """Get a specific task by ID"""
    task = get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", response_model=Task, tags=["tasks"])
async def add_task(task: TaskCreate):
    """Create a new task"""
    return create_task(task)

@app.put("/tasks/{task_id}", response_model=Task, tags=["tasks"])
async def modify_task(task_id: str, task: TaskUpdate):
    """Update an existing task"""
    updated_task = update_task(task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}", response_model=Task, tags=["tasks"])
async def remove_task(task_id: str):
    """Delete a task (soft delete)"""
    deleted_task = delete_task(task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)