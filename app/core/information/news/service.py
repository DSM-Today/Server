from uuid import uuid4, UUID

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.subject.comand import create_subject
from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name

from app.utils.dataset.crawler.information.news import news_crawler


def query_news():
    _id = uuid4().bytes
    news = news_crawler.crawl()

    create_subject(_id, 'NEWS', '오늘의 뉴스', 'INFORMATION')

    return news


def insert_news_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(
        user_id=user_id,
        name='NEWS',
        kind='INFORMATION',
        title='오늘의 뉴스',
    )


def delete_my_news_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, 'NEWS')



