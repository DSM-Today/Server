from fastapi import APIRouter, status

from app.utils import show_reason

from app.core.subject.suggest.book.service import query_book

book_router = APIRouter(
    prefix='/suggest/book'
)


@book_router.get('/', status_code=status.HTTP_200_OK)
@show_reason
def get_book():
    return query_book()
