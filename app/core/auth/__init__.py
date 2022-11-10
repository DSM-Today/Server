from fastapi import APIRouter
from fastapi import status
from app.core.auth.service import query_oauth_link, register_or_login

from fastapi import Response

auth_router = APIRouter(
    prefix='/auth'
)


@auth_router.get('/oauth/{service_type}')
def get_oauth_link(service_type: str):
    return query_oauth_link(service_type)


@auth_router.get('/oauth/{service_type}/code', status_code=status.HTTP_201_CREATED)
def get_code(service_type: str, code: str, response: Response):
    return register_or_login(service_type, code, response)
