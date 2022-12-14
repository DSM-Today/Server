from datetime import date

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.user.query import query_user_by_id
from app.utils.dao.mysql.user.command import initialize_user_info, update_user_profile_by_id

from app.utils.dao.mysql.bookmark.query import query_my_bookmark_list_by_id


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


def update_user_profile(token: str, image_path: str, name: str, introduce: str, birth_day: date):
    update_user_profile_by_id(
        get_user_id(token),
        name=name,
        introduce=introduce,
        image_path=image_path,
        birth_day=birth_day
    )


def user_initialize_information(token: str, introduce: str, can_person: bool, birth_day: date):
    initialize_user_info(
        get_user_id(token),
        introduce=introduce,
        can_person=can_person,
        birth_day=birth_day
    )