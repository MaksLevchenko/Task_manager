from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, db
from .db import get_db

app = FastAPI(
    title="Task Manager API",
    description="Простой API для управления задачами",
    version="1.0.0",
)

models.Base.metadata.create_all(bind=db.engine)


@app.post(
    "/tasks/", response_model=schemas.Task, summary="Создание задачи", tags=["Tasks"]
)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)


@app.get(
    "/tasks/",
    response_model=list[schemas.Task],
    summary="Получение всех задач",
    tags=["Tasks"],
)
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks


@app.get(
    "/tasks/{task_id}",
    response_model=schemas.Task,
    summary="Получение задачи по ID",
    tags=["Tasks"],
)
def read_task(task_id: str, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return db_task


@app.put(
    "/tasks/{task_id}",
    response_model=schemas.Task,
    summary="Обновление задачи по ID",
    tags=["Tasks"],
)
def update_task(
    task_id: str, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)
):
    db_task = crud.update_task(db, task_id=task_id, task_update=task_update)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return db_task


@app.delete(
    "/tasks/{task_id}",
    response_model=schemas.Task,
    summary="Удаление задачи по ID",
    tags=["Tasks"],
)
def delete_task(task_id: str, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return db_task


@app.get("/")
def read_root():
    return {"message": "Task Manager API"}
