from sqlalchemy.orm import Session
from models import TaskDB
from models import TaskIn, TaskUpdate

def create_task_db(db: Session, task: TaskIn):
    db_task = TaskDB(**task.dict(), ID=str(len(db.query(TaskDB).all()) + 1))
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks_db(db: Session):
    return db.query(TaskDB).all()

def get_task_db(db: Session, task_id: str):
    return db.query(TaskDB).filter(TaskDB.ID == task_id).first()

def update_task_db(db: Session, task_id: str, task_update: TaskUpdate):
    task = db.query(TaskDB).filter(TaskDB.ID == task_id).first()
    if task:
        for key, value in task_update.dict(exclude_unset=True).items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
        return task
    return None

def delete_task_db(db: Session, task_id: str):
    task = db.query(TaskDB).filter(TaskDB.ID == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False