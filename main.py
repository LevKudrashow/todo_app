from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from models import Task, TaskIn, TaskUpdate
from .database import SessionLocal
from crud import create_task_db, get_tasks_db, get_task_db, update_task_db, delete_task_db
from auth import authenticate_user, create_access_token

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)  # You need to implement authentication
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})  # You need a User model for this
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/tasks", response_model=Task)
def create_task(task: TaskIn, db: Session = Depends(get_db)):
    return create_task_db(db, task)

@app.get("/tasks", response_model=List[Task])
def get_tasks(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return get_tasks_db(db)

@app.get("/tasks/{id}", response_model=Task)
def get_task(id: str, db: Session = Depends(get_db)):
    task = get_task_db(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{id}", response_model=Task)
def update_task(id: str, task_update: TaskUpdate, db: Session = Depends(get_db)):
    task = update_task_db(db, id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{id}", response_model=dict)
def delete_task(id: str, db: Session = Depends(get_db)):
    success = delete_task_db(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}