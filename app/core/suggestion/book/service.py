from uuid import uuid4, UUID

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.subject.comand import create_subject
from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name

from app.utils.dataset.crawler.operation.book import book_crawler


def query_book():
    create_subject(uuid4().bytes, name='BOOK', title='오늘의 책', kind='SUGGEST')

    return book_crawler.crawl()


def add_book_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id=user_id, name='BOOK', title='오늘의 책', kind='SUGGEST')


def delete_my_book_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, 'BOOK')