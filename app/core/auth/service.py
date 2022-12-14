from datetime import timedelta

from app.config import JWTConfig

from app.utils.exception.custom import InvalidTokenException

from app.utils.dao.redis.command import set_ex
from app.utils.dao.redis.query import get_value_by_user_id

from app.utils.dao.mysql.user.query import query_user_by_id

from app.utils.security.token import is_refresh_token, get_user_id, generate_access_token, generate_refresh_token


def reissue_both_token(token: str):
    user_id = get_user_id(token)

    user = query_user_by_id(user_id)
    refresh_token = get_value_by_user_id(user_id)

    if (refresh_token is None) or (user is None) or not is_refresh_token(token):
        raise InvalidTokenException

    issued_refresh_token = generate_refresh_token(user_id)

    set_ex(
        uid=user_id,
        refresh_token=issued_refresh_token,
        ttl=timedelta(minutes=JWTConfig.REFRESH_EXPIRE * 1000)
    )

    return {
        'access_token': generate_access_token(user_id),
        'refresh_token': issued_refresh_token
    }
