from uuid import UUID

from app.core import Suggestion

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.subject.suggest.menu.query import get_rand_menu

from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name

Menu = Suggestion.Menu


def get_random_cafe_menu():
    return get_rand_menu()


def add_menu_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id=user_id, name=Menu.NAME, title=Menu.TITLE, kind=Suggestion.KIND)


def delete_my_menu_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, Menu.NAME)
