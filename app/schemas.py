from pydantic import BaseModel, field_validator
from uuid import UUID
from .models import TaskStatus
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.CREATED


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None


class Task(TaskBase):
    id: str

    @field_validator("id")
    def validate_uuid(cls, v):
        try:
            UUID(v)
            return v
        except ValueError:
            raise ValueError("Неверный формат UUID ")

    class Config:
        from_attributes = True
