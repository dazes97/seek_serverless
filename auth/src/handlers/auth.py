import json
from pydantic import ValidationError
from ..services.auth_service import AuthService
from ..models.user_model import User


def authenticate(event, _):
    try:
        body = json.loads(event['body'])
        user = User(**body)
    except (json.JSONDecodeError, ValidationError) as e:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
                'Content-Type': 'application/json',
            },
            'body': json.dumps({
                'message': 'Invalid input',
                'errors': str(e),
                'status': 'error'
            })
        }

    auth_service = AuthService()
    token = auth_service.authenticate(user.email, user.password)

    if token:
        return {
            'statusCode': 201,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
                'Content-Type': 'application/json',
            },
            'body': json.dumps({
                "data": [{'token': token}],
                "message": "Authentication successful",
                'status': 'success'
            })
        }
    else:
        return {
            'statusCode': 404,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
                'Content-Type': 'application/json',
            },
            'body': json.dumps({
                'message': 'Authentication failed',
                'errors': 'Invalid email or password',
                'status': 'error'
            })
        }
