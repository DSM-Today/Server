from fastapi import APIRouter, status

from app.core.subject.suggest.webtoon.service import query_webtoon

webtoon_router = APIRouter(
    prefix='/suggest/webtoon'
)


@webtoon_router.get('/', status_code=status.HTTP_200_OK)
def get_webtoon():
    return query_webtoon()
