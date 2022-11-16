from fastapi import Depends, APIRouter, status

from app.utils.security import oauth2_scheme

from app.core.random.flower.service import add_flower_to_bookmark, delete_my_flower_bookmark

flower_router = APIRouter(
    prefix='/random/flower'
)


@flower_router.post('/')
def add_flower_bookmark(token: str = Depends(oauth2_scheme)):
    add_flower_to_bookmark(token)


@flower_router.delete('/')
def delete_flower_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_flower_bookmark(token)
