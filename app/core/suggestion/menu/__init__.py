from fastapi import APIRouter, Depends, status

from app.utils import show_reason
from app.utils.security import oauth2_scheme

from app.core.suggestion.menu.service import add_menu_to_bookmark, delete_my_menu_bookmark

menu_router = APIRouter(
    prefix='/suggest/menu'
)


@menu_router.post('/', status_code=status.HTTP_201_CREATED)
@show_reason
def add_menu_bookmark(token: str = Depends(oauth2_scheme)):
    add_menu_to_bookmark(token)


@menu_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
@show_reason
def delete_menu_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_menu_bookmark(token)
