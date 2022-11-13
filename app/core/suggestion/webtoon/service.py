from uuid import uuid4, UUID

from app.utils.security.token import get_user_id

from app.utils.dataset.crawler.operation.webtoon import webtoon_crawler

from app.utils.dao.cqrs.subject.comand import create_subject
from app.utils.dao.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name


def query_webtoon():

    create_subject(uuid4().bytes, name='WEBTOON', title='오늘의 웹툰', kind='SUGGEST')

    return webtoon_crawler.crawl()


def add_webtoon_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id=user_id, name='WEBTOON', kind='SUGGEST', title='오늘의 웹툰')


def delete_my_webtoon_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, 'WEBTOON')
