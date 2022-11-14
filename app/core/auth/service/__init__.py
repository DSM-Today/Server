from uuid import UUID
from app.utils.dao.cqrs.user.query import user_exist_by_email, query_id_by_email, query_user_by_id

from app.utils.dao.cqrs.user.command import save_user

from app.utils.security.oauth import provide_oauth
from app.utils.security.oauth.impl import duc_query_client_id

from app.utils.security.token import generate_access_token, generate_refresh_token


def query_client_id(oauth_type: str):
    oauth = provide_oauth(oauth_type)

    return {
        "client_id": duc_query_client_id(oauth)
    }


def register_or_login(oauth_type: str, id_token: str):
    oauth = provide_oauth(oauth_type)

    user_info = oauth.check_id_token_verify(id_token)

    if user_exist_by_email(user_info['email']) is None:
        user = save_user(
            email=user_info['email'],
            name=user_info['name'],
            image_path=user_info['picture'],
            can_person=False
        )


    else:
        user_id = query_id_by_email(user_info['email'])

        user = query_user_by_id(user_id)

    return {
        "is_birthday_exist": False if user.birth_day is None else True,
        "is_can_person": False if user.can_person in [None, False] else True,
        "is_introduce_exist": False if user.introduce is None else True,
        "access_token": generate_access_token(user.id.hex()),
        "refresh_token": generate_refresh_token(user.id.hex())
    }
