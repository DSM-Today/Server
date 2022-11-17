from fastapi import APIRouter, Depends, status

from app.utils.security import oauth2_scheme

from app.core.bookmark.service import add_new_bookmark, delete_my_bookmark

bookmark_router = APIRouter(
    prefix='/bookmark'
)


@bookmark_router.post('/', status_code=status.HTTP_201_CREATED)
def create_bookmark(name: str, title: str, kind: str, token: str = Depends(oauth2_scheme)):
    add_new_bookmark(name, title, kind, token)


@bookmark_router.delete('/')
def delete_bookmark(name: str, token: str = Depends(oauth2_scheme)):
    delete_my_bookmark(name, token)
