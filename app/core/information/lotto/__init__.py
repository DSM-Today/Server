from fastapi import APIRouter, Depends, status\

from app.utils import show_reason

from app.utils.security import oauth2_scheme
from app.core.information.lotto.service import query_lotto, insert_lotto_bookmark, delete_my_lotto_bookmark

lotto_router = APIRouter(
    prefix='/information/lotto'
)


@lotto_router.get('/', status_code=status.HTTP_200_OK)
@show_reason
def get_lotto():
    return query_lotto()


@lotto_router.post('/', status_code=status.HTTP_201_CREATED)
@show_reason
def add_lotto_bookmark(token: str = Depends(oauth2_scheme)):
    insert_lotto_bookmark(token)


@lotto_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
@show_reason
def delete_lotto_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_lotto_bookmark(token)
