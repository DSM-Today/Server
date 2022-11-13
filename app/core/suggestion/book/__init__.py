from fastapi import APIRouter, Depends, status

from app.utils.security import oauth2_scheme

from app.core.suggestion.book.service import query_book

book_router = APIRouter(
    prefix='/suggest/book'
)


@book_router.get('/', status_code=status.HTTP_200_OK)
def get_book():
    return query_book()


@book_router.post('/', status_code=status.HTTP_201_CREATED)
def add_book_bookmark(token: str = Depends(oauth2_scheme)):
    pass


@book_router.post('/', status_code=status.HTTP_204_NO_CONTENT)
def delete_book_bookmark(token: str = Depends(oauth2_scheme)):
    pass
