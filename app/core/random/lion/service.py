from uuid import UUID

from app.core import Random

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name

from app.utils.dao.mysql.cqrs.subject.random.lion_word.query import query_random_lion_word

LionWord = Random.LionWord


def query_lion_word():
    return query_random_lion_word()


def add_lion_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id, name=LionWord.NAME, title=LionWord.TITLE, kind=Random.KIND)


def delete_my_lion_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, LionWord.NAME)
