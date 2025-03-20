import json
from ..services.task_service import TaskService


def all(_, __):
    task_service = TaskService()
    task_list = task_service.all()
    return {
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Content-Type': 'application/json',
        },
        'body': json.dumps({
            "data": [task.dict() for task in task_list],
            "message": "Task list retrieved successfully"
        })
    }
