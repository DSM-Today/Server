from fastapi import APIRouter, Response, status

from app.core.auth.oauth.dto import Request

from app.core.auth.oauth.service import query_client_id, register_or_login

oauth_router = APIRouter(
    prefix='/auth/oauth'
)


@oauth_router.get('/{service_type}')
def get_oauth_link(service_type: str):
    return query_client_id(service_type)


@oauth_router.post('/{service_type}', status_code=status.HTTP_201_CREATED)
def get_code(service_type, request: Request.IdToken, response: Response):
    return register_or_login(service_type, request.id_token, response)
