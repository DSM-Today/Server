from app.utils.security.token import get_user_id

from app.utils.dao.mysql.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name


def add_new_bookmark(name: str, title: str, kind: str, token: str):
    create_bookmark(
        user_id=get_user_id(token),
        name=name,
        title=title,
        kind=kind
    )


def delete_my_bookmark(name: str, token: str):
    delete_bookmark_by_user_id_and_name(
        user_id=get_user_id(token),
        subject_name=name
    )
