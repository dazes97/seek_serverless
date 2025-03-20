from uuid import uuid4
from datetime import datetime
from ..models.task_model import TodoItem
from ..repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()

    def all(self):
        return self.task_repository.all()

    def create(self, data):
        now = datetime.now().isoformat()
        todo_item = TodoItem(
            id=str(uuid4()),
            title=data.title,
            description=data.description,
            status='Por hacer',
            created_at=now
        )
        self.task_repository.create(todo_item)
        return todo_item

    def update(self, task_id: str, status: str):
        return self.task_repository.update(task_id, status)

    def delete(self, task_id: str):
        return self.task_repository.delete(task_id)
