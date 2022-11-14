from fastapi import APIRouter
from fastapi import status
from app.core.auth.service import query_client_id, register_or_login

auth_router = APIRouter(
    prefix='/auth'
)


@auth_router.get('/oauth/{service_type}')
def get_oauth_link(service_type: str):
    return query_client_id(service_type)


@auth_router.post('/oauth/{service_type}', status_code=status.HTTP_201_CREATED)
def get_code(service_type: str, id_token: str):
    return register_or_login(service_type, id_token)
