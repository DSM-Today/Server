from uuid import UUID
from datetime import datetime, timedelta

import jwt

from app.config import JWTConfig


def generate_access_token(user_id: UUID.hex):
    exp = datetime.utcnow() + timedelta(hours=9 + int(JWTConfig.ACCESS_EXPIRE))
    return jwt.encode(payload={'exp': exp, 'sub': user_id, "type": JWTConfig.ACCESS_NAME}, key=JWTConfig.SECRET_KEY)


def generate_refresh_token(user_id: UUID.hex):
    exp = datetime.utcnow() + timedelta(hours=9 + int(JWTConfig.ACCESS_EXPIRE))
    return jwt.encode(payload={'exp': exp, 'sub': user_id, "type": JWTConfig.REFRESH_NAME}, key=JWTConfig.SECRET_KEY)
