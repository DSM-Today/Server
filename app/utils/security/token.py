from uuid import UUID
from datetime import datetime, timedelta

import jwt

from app.config import JWTConfig


def generate_access_token(user_id: UUID.hex):
    exp = datetime.utcnow() + timedelta(hours=9 + int(JWTConfig.ACCESS_EXPIRE))
    return jwt.encode(
        payload={
            'sub': JWTConfig.ACCESS_NAME,
            'uid': user_id,
            'exp': exp
        },
        key=JWTConfig.SECRET_KEY,
        algorithm=JWTConfig.ALGORITHM
    )


def generate_refresh_token(user_id: UUID.hex):
    exp = datetime.utcnow() + timedelta(hours=9 + int(JWTConfig.ACCESS_EXPIRE))
    return jwt.encode(
        payload={
            'sub': JWTConfig.REFRESH_NAME,
            'uid': user_id,
            'exp': exp
        },
        key=JWTConfig.SECRET_KEY,
        algorithm=JWTConfig.ALGORITHM
    )


def __decode_jwt(token: str):
    return jwt.decode(jwt=token, key=JWTConfig.SECRET_KEY, algorithms=JWTConfig.ALGORITHM)


def get_user_id(token: str):
    return __decode_jwt(token)['uid']


def check_role(token: str, role_list: list):
    def decorator_impl(func):
        def wrapper():
            if __decode_jwt(token)['role'] not in role_list:
                from fastapi import HTTPException
                raise HTTPException(403, detail='역할이 올바르지 않습니다')

            return func

        return wrapper

    return decorator_impl
