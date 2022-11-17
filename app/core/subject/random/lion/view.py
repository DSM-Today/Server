from fastapi import APIRouter, status

from app.core.subject.random.lion.service import query_lion_word

lion_router = APIRouter(
    prefix='/random/lion'
)


@lion_router.get('/', status_code=status.HTTP_200_OK)
def get_lion_word():
    return query_lion_word()
