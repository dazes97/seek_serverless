import json
from ..services.task_service import TaskService


def all(_, __):
    task_service = TaskService()
    try:
        task_list = task_service.all()
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                "data": [task.dict() for task in task_list],
                "message": "Task list retrieved successfully",
                "status": "success"
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                "message": "An error occurred while retrieving the task list",
                "error": str(e),
                "status": "error"
            })
        }
