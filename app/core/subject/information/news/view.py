from fastapi import APIRouter, status

from app.utils import show_reason

from app.core.subject.information.news.service import query_news

news_router = APIRouter(
    prefix='/information/news'
)


@news_router.get('/', status_code=status.HTTP_200_OK)
@show_reason
def get_news():
    return query_news()
