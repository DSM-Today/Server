from fastapi import APIRouter, Depends, status

from app.core.information.service import query_information_list
from app.core.information.news.service import query_news, insert_news_bookmark, delete_my_news_bookmark

information_router = APIRouter(
    prefix='/information'
)


@information_router.get('/list', status_code=status.HTTP_200_OK)
def get_information_list():
    return query_information_list()


