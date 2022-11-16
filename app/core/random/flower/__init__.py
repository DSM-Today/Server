from fastapi import Depends, APIRouter, status

from app.utils.security import oauth2_scheme

from app.core.random.flower.service import add_flower_to_bookmark, delete_my_flower_bookmark, query_flower

flower_router = APIRouter(
    prefix='/random/flower'
)


@flower_router.get('/', status_code=status.HTTP_200_OK)
def get_flower():
    return query_flower()


@flower_router.post('/', status_code=status.HTTP_201_CREATED)
def add_flower_bookmark(token: str = Depends(oauth2_scheme)):
    add_flower_to_bookmark(token)


@flower_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def delete_flower_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_flower_bookmark(token)
