from uuid import UUID

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name


def add_flower_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(
        user_id,
        name='FLOWER',
        kind='RANDOM',
        title='오늘의 꽃'
    )


def delete_my_flower_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, 'FLOWER')
