from ..services.authorizer_service import AuthorizerService


def authorize(event, _):
    token = event['headers'].get('Authorization')
    print(f'Token del header: {token}')
    authorizer_service = AuthorizerService()
    return authorizer_service.authorize(token)
