from uuid import uuid4, UUID

from app.core import Random

from app.utils.security.token import get_user_id

from app.utils.dataset.crawler.random.lucky import luck_crawler

from app.utils.dao.mysql.cqrs.subject.comand import create_subject
from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name
from app.utils.dao.mysql.cqrs.user.query import query_user_birth_by_id

Luck = Random.Luck


def query_user_luck(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_subject(uuid4().bytes, name=Luck.NAME, title=Luck.TITLE, kind=Random.KIND)

    birth = query_user_birth_by_id(user_id)

    return luck_crawler.crawl(
        int(str(birth)[5:].replace('-', ''))  # TODO
    )


def add_my_lucky_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id, name=Luck.NAME, title=Luck.TITLE, kind=Random.KIND)


def delete_my_lucky_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, Luck.NAME)
