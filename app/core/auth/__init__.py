from fastapi import APIRouter
from fastapi import status
from app.core.auth.service import query_client_id, register_or_login

from app.utils import show_reason

auth_router = APIRouter(
    prefix='/auth'
)


@auth_router.get('/oauth/{service_type}')
@show_reason
def get_oauth_link(service_type: str):
    return query_client_id(service_type)


@auth_router.post('/oauth/{service_type}', status_code=status.HTTP_201_CREATED)
@show_reason
def get_code(service_type: str, id_token: str):
    return register_or_login(service_type, id_token)
