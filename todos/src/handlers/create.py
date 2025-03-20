import json

from pydantic import ValidationError

from ..models.task_model import CreateItem
from ..services.task_service import TaskService


def create(event, _):
    try:
        body = json.loads(event['body'])
        create_task = CreateItem(**body)
    except (json.JSONDecodeError, ValidationError) as e:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Invalid input',
                'errors': str(e)
            })
        }
    task_service = TaskService()
    task_item = task_service.create(create_task)
    return {
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Content-Type': 'application/json',
        },
        'body': json.dumps({
            "data": [task_item.dict()],
            "message": "Task list retrieved successfully",
            'status': 'success'
        })
    }
