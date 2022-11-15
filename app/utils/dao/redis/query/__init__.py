from app.utils.dao.redis import Redis


def get_value_by_user_id(uid):
    token = Redis.get(uid)

    if token is not None:
        token = token.decode('utf-8')

    return token
