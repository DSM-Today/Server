from fastapi import APIRouter, status

from app.utils import show_reason

from app.core.subject.suggest.webtoon.service import query_webtoon

webtoon_router = APIRouter(
    prefix='/suggest/webtoon'
)


@show_reason
@webtoon_router.get('/', status_code=status.HTTP_200_OK)
def get_webtoon():
    return query_webtoon()
