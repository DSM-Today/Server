from uuid import UUID

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name


def add_lion_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(
        user_id,
        name='LION_WORD',
        kind='RANDOM',
        title='오늘의 사자성어'
    )


def delete_my_lion_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, 'LION_WORD')
