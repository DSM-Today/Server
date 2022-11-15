from fastapi import APIRouter, Depends, status

from app.utils import show_reason
from app.utils.security import oauth2_scheme

from app.core.random.luck.service import query_user_luck, add_my_lucky_bookmark, delete_my_lucky_bookmark

luck_router = APIRouter(
    prefix='/random/lucky'
)


@luck_router.get('/', status_code=status.HTTP_200_OK)
@show_reason
def get_my_luck(token: str = Depends(oauth2_scheme)):
    return query_user_luck(token)


@luck_router.post('/', status_code=status.HTTP_201_CREATED)
@show_reason
def add_lucky_bookmark(token: str = Depends(oauth2_scheme)):
    add_my_lucky_bookmark(token)


@luck_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
@show_reason
def delete_lucky_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_lucky_bookmark(token)