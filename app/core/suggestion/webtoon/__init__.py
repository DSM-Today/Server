from fastapi import APIRouter, Depends, status

from app.utils.security import oauth2_scheme

from app.core.suggestion.webtoon.service import query_webtoon, add_webtoon_to_bookmark, delete_my_webtoon_bookmark

webtoon_router = APIRouter(
    prefix='/suggest/webtoon'
)


@webtoon_router.get('/', status_code=status.HTTP_200_OK)
def get_webtoon():
    return query_webtoon()


@webtoon_router.post('/', status_code=status.HTTP_201_CREATED)
def add_webtoon_bookmark(token: str = Depends(oauth2_scheme)):
    add_webtoon_to_bookmark(token)


@webtoon_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def delete_webtoon_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_webtoon_bookmark(token)
