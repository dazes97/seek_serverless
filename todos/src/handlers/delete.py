import json
from ..services.task_service import TaskService


def delete(event, __):
    id = event['pathParameters']['id']
    task_service = TaskService()
    task_service.delete(id)
    return {
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Content-Type': 'application/json',
        },
        'body': json.dumps({
            'message': 'Item deleted successfully',
            'data': [],
            'status': 'success'
        })
    }
