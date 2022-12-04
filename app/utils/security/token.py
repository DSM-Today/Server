from uuid import UUID
from datetime import datetime, timedelta

import jwt

from app.config import JWTConfig
from app.utils.exception.custom import RoleNotCorrect


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


def get_user_name(token: str):
    return __decode_jwt(token)['unm']


def get_image_path(token: str):
    return __decode_jwt(token)['image_path']


def is_refresh_token(token: str):
    return __decode_jwt(token)['sub'] == JWTConfig.REFRESH_NAME


def check_role(token: str, role_list: list):
    def decorator_impl(func):
        def wrapper():
            if __decode_jwt(token)['role'] not in role_list:
                raise RoleNotCorrect

            return func

        return wrapper

    return decorator_impl
