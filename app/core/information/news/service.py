from uuid import uuid4, UUID

from app.core import Information

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.subject.comand import create_subject
from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name

from app.utils.dataset.crawler.information.news import news_crawler

News = Information.News


def query_news():
    subject_id = uuid4().bytes
    news = news_crawler.crawl()

    create_subject(subject_id, name=News.NAME, title=News.TITLE, kind=Information.KIND)

    return news


def insert_news_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id, name=News.NAME, title=News.TITLE, kind=Information.KIND)


def delete_my_news_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, 'NEWS')
