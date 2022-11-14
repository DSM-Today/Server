from app.utils.security.token import get_user_id

from app.utils.dao.cqrs.bookmark.query import query_my_bookmark_list_by_id
from app.utils.dao.cqrs.user.query import query_user_by_id


def query_my_bookmark_list(token: str):
    user_id = get_user_id(token)

    return {
        'bookmark_list': query_my_bookmark_list_by_id(user_id)
    }


def query_my_profile(token: str):
    user = query_user_by_id(
        get_user_id(token)
    )

    return {
        'name': user.name,
        'birth_day': user.birth_day,
        'image_path': user.image_path,
        'introduction': user.introduce
    }
