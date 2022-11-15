from app.utils.dao.redis import Redis


def get_value_by_user_id(uid):
    return Redis.get(uid).decode("utf-8")
