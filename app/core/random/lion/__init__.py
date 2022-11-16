from fastapi import Depends, APIRouter, status

from app.utils.security import oauth2_scheme

from app.core.random.lion.service import add_lion_to_bookmark, delete_my_lion_bookmark

lion_router = APIRouter(
    prefix='/random/lion'
)


@lion_router.post('/', status_code=status.HTTP_201_CREATED)
def add_lion_bookmark(token: str = Depends(oauth2_scheme)):
    add_lion_to_bookmark(token)


@lion_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def delete_lion_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_lion_bookmark(token)
