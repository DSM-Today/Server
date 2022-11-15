from fastapi import APIRouter, Response, status

from app.core.auth.dto import DTO

from app.utils import show_reason

from app.core.auth.service import query_client_id, register_or_login

auth_router = APIRouter(
    prefix='/auth'
)


@auth_router.get('/oauth/{service_type}')
@show_reason
def get_oauth_link(service_type: str):
    return query_client_id(service_type)


@auth_router.post('/oauth/{service_type}', status_code=status.HTTP_201_CREATED)
@show_reason
def get_code(service_type, request: DTO.IdTokenRequest, response: Response):
    return register_or_login(service_type, request.id_token, response)
