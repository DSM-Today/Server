from datetime import date

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.user.query import query_user_by_id
from app.utils.dao.mysql.cqrs import initialize_user_info

from app.utils.dao.mysql.cqrs.bookmark import query_my_bookmark_list_by_id


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


def user_initialize_information(token: str, introduce: str, can_person: bool, birth_day: date):
    initialize_user_info(
        get_user_id(token),
        introduce=introduce,
        can_person=can_person,
        birth_day=birth_day
    )