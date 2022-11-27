from fastapi import APIRouter, status

from app.core.subject.information.news.service import query_news

news_router = APIRouter(
    prefix='/information/news'
)


@news_router.get('/', status_code=status.HTTP_200_OK)
def get_news():
    return query_news()
