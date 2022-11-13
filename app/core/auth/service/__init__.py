from uuid import uuid4, UUID
from fastapi import status, Response

from app.utils.security.oauth import provide_oauth
from app.utils.security.oauth.impl \
    import duc_query_oauth_link, duc_query_access_token, duc_query_userinfo, duc_query_birthday

from app.utils.type_changer import str_to_date

from app.utils.security.token import generate_access_token, generate_refresh_token

from app.utils.dao.cqrs.user.command import save_user
from app.utils.dao.cqrs.user.query import user_exist_by_email, query_id_by_email


def query_oauth_link(oauth_type: str):
    oauth = provide_oauth(oauth_type)

    return duc_query_oauth_link(oauth)


def register_or_login(oauth_type: str, code: str, response: Response):  # response를 가져오는 게 맞는 판단일까 TODO
    oauth = provide_oauth(oauth_type)

    access_token = duc_query_access_token(oauth, code)['access_token']
    user_info = duc_query_userinfo(oauth, access_token)

    user_id = uuid4()
    email = user_info['email']

    user_exist_by_email(email)
    birth_day = ''.join(map(str, duc_query_birthday(oauth, access_token).values()))

    if user_exist_by_email(email) is None:
        save_user(
            _id=uuid4().bytes,
            email=email,
            name=user_info['name'],
            image_path=user_info['picture'],
            birth_day=str_to_date(birth_day),
            can_person=False,
            introduce=None,
        )

        response.status_code = status.HTTP_201_CREATED
    else:
        response.status_code = status.HTTP_200_OK
        user_id = query_id_by_email(email)

    return {
        'access_token': generate_access_token(UUID(user_id).hex),
        'refresh_token': generate_refresh_token(UUID(user_id).hex)
    }
