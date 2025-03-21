import json
from ..services.task_service import TaskService


def delete(event, __):
    id = event['pathParameters']['id']
    try:
        task_service = TaskService()
        task_service.delete(id)
        return {
            'statusCode': 201,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Item deleted successfully',
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
                "message": "An error occurred while deleting the task",
                "error": str(e),
                "status": "error"
            })
        }
