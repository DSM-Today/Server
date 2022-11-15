from uuid import uuid4, UUID

from app.utils.security.token import get_user_id

from app.utils.dataset.crawler.operation.movie import movie_crawler
from app.utils.dao.mysql.cqrs.subject.comand import create_subject
from app.utils.dao.mysql.cqrs.bookmark import create_bookmark, delete_bookmark_by_user_id_and_name


def query_movie():
    create_subject(uuid4().bytes, name='MOVIE', title='오늘의 영화', kind='SUGGEST')

    return movie_crawler.crawl()


def add_movie_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id=user_id, name='MOVIE', title='오늘의 영화', kind='SUGGEST')


def delete_my_movie_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, 'MOVIE')
