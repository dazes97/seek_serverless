import json
from pydantic import ValidationError
from ..models.task_model import UpdateItem
from ..services.task_service import TaskService


def update(event, __):
    id = event['pathParameters']['id']
    try:
        body = json.loads(event['body'])
        update_status = UpdateItem(**body)
    except (json.JSONDecodeError, ValidationError) as e:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Invalid input',
                'errors': str(e),
                "status": "error"
            })
        }

    try:
        task_service = TaskService()
        task_service.update(id, update_status.status)
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': f'Item marked as {update_status.status} successfully',
                'data': [],
                'status': 'success'
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
                "message": "An error occurred while updating the task",
                "error": str(e),
                "status": "error"
            })
        }
