from datetime import timedelta
from app.utils.dao.redis import Redis


def set_ex(ttl: timedelta, uid, refresh_token):
    Redis.setex(
        name=uid,
        value=refresh_token,
        time=ttl
    )
