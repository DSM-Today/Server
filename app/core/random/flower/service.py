from uuid import UUID

from app.core import Random

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.subject.random.flower.query import query_random_flower

from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name

Flower = Random.Flower


def query_flower():
    return query_random_flower()


def add_flower_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id, name=Flower.NAME, title=Flower.TITLE, kind=Random.KIND)


def delete_my_flower_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, Flower.NAME)
