from uuid import uuid4, UUID

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name


def add_menu_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id=user_id, name='MENU', title='오늘의 메뉴', kind='SUGGEST')


def delete_my_menu_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, 'MENU')
