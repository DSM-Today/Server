from fastapi import APIRouter, Depends, status

from app.utils import show_reason
from app.utils.security import oauth2_scheme

from app.core.suggestion.book.service import query_book, add_book_to_bookmark, delete_my_book_bookmark

book_router = APIRouter(
    prefix='/suggest/book'
)


@book_router.get('/', status_code=status.HTTP_200_OK)
@show_reason
def get_book():
    return query_book()


@book_router.post('/', status_code=status.HTTP_201_CREATED)
@show_reason
def add_book_bookmark(token: str = Depends(oauth2_scheme)):
    add_book_to_bookmark(token)


@book_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
@show_reason
def delete_book_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_book_bookmark(token)