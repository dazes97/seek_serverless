from typing import Literal, Optional
from pydantic import BaseModel, Field


class TodoItem(BaseModel):
    id: str
    title: str
    description: str
    status: str
    created_at: str
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class CreateItem(BaseModel):
    title: str = Field(..., min_length=1, max_length=50)
    description: str = Field(..., min_length=1, max_length=255)


class UpdateItem(BaseModel):
    status: Literal['Por hacer', 'En progreso', 'Terminado']
