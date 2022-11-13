from uuid import UUID, uuid4

from app.utils.type_changer import str_to_date

from app.utils.security.token import get_user_id

from app.utils.dataset.crawler.information.lotto import lotto_crawler

from app.utils.dao.cqrs.subject.comand import create_subject
from app.utils.dao.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id


def query_lotto():
    lotto = lotto_crawler.crawl()
    lotto['date'] = str_to_date(lotto['date'].replace('.', ''))

    create_subject(_id=uuid4().bytes, kind='INFORMATION', name='LOTTO', title='오늘의 로또')
    return lotto


def insert_lotto_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex
    create_bookmark(user_id=user_id, name='LOTTO', kind='INFORMATION', title='오늘의 로또')


def delete_my_lotto_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex
    delete_bookmark_by_user_id(user_id, 'LOTTO')
