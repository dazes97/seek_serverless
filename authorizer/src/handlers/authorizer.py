from ..services.authorizer_service import AuthorizerService


def authorize(event, _):
    token = event['headers'].get('Authorization')
    if (token is None):
        token = event['headers'].get('authorization')
    authorizer_service = AuthorizerService()
    return authorizer_service.authorize(token)
