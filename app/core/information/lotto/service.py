from uuid import UUID, uuid4

from app.core import Information

from app.utils.type_changer import str_to_date

from app.utils.security.token import get_user_id

from app.utils.dataset.crawler.information.lotto import lotto_crawler

from app.utils.dao.mysql.cqrs.subject.comand import create_subject
from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name

Lotto = Information.Lotto


def query_lotto():
    lotto = lotto_crawler.crawl()
    lotto['date'] = str_to_date(lotto['date'].replace('.', ''))

    create_subject(_id=uuid4().bytes, name=Lotto.NAME, title=Lotto.TITLE, kind=Information.KIND)
    return lotto


def insert_lotto_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex
    create_bookmark(user_id=user_id, name=Lotto.NAME, title=Lotto.TITLE, kind=Information.KIND)


def delete_my_lotto_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex
    delete_bookmark_by_user_id_and_name(user_id, Lotto.NAME)
