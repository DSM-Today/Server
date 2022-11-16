from uuid import uuid4, UUID

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.user.query import query_random_user

from app.utils.dao.mysql.cqrs.subject.comand import create_subject
from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name


def query_person():
    create_subject(uuid4().bytes, kind='RANDOM', name='PERSON', title='오늘의 인물')

    return query_random_user()


def add_person_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(
        user_id,
        name='LUCKY',
        kind='PERSON',
        title='오늘의 인물'
    )


def delete_my_person_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, 'PERSON')
