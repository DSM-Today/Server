from datetime import timedelta

from app.config import JWTConfig

from fastapi import Response

from app.utils.dao.mysql.cqrs.user.query import user_exist_by_email, query_user_by_email

from app.utils.dao.mysql.cqrs.user.command import save_user

from app.utils.security.oauth import provide_oauth
from app.utils.security.oauth.impl import duc_query_client_id

from app.utils.security.token import generate_access_token, generate_refresh_token

from app.utils.dao.redis.command import set_ex


def query_client_id(oauth_type: str):
    oauth = provide_oauth(oauth_type)

    return {
        "client_id": duc_query_client_id(oauth)
    }


def register_or_login(oauth_type: str, id_token: str, response: Response):
    oauth = provide_oauth(oauth_type)

    user_info = oauth.check_id_token_verify(id_token)

    user = query_user_by_email(user_info['email'])

    if user is None:
        user = save_user(
            email=user_info['email'],
            name=user_info['name'],
            image_path=user_info['picture'],
            can_person=False
        )

        response.status_code = 201

    else:
        response.status_code = 200

    refresh_token = generate_refresh_token(user.id.hex())

    set_ex(
        ttl=timedelta(minutes= JWTConfig.REFRESH_EXPIRE * 1000),
        uid=user.id.hex(),
        refresh_token=refresh_token
    )

    return {
        "is_birthday_exist": False if user.birth_day is None else True,
        "is_can_person": False if user.can_person in [None, False] else True,
        "is_introduce_exist": False if user.introduce is None else True,
        "access_token": generate_access_token(user.id.hex()),
        "refresh_token": refresh_token
    }
