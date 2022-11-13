from fastapi import APIRouter, Depends, status

from app.utils.security import oauth2_scheme
from app.core.information.news.service import query_news, insert_news_bookmark, delete_my_news_bookmark

news_router = APIRouter(
    prefix='/information/news'
)


@news_router.get('/', status_code=status.HTTP_200_OK)
def get_news():
    return query_news()


@news_router.post('/', status_code=status.HTTP_201_CREATED)
def add_news_bookmark(token: str = Depends(oauth2_scheme)):
    insert_news_bookmark(token)


@news_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def delete_news_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_news_bookmark(token)
