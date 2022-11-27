from typing import Optional

from fastapi import HTTPException


# 이것도 이중 클래스로 나눌까? TODO


class InvalidTokenException(HTTPException):
    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'TOKEN IS NOT INVALID'

        self.detail = detail
        self.status_code = 401


class NotVerifiedIdToken(HTTPException):
    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'IT TOKEN IS NOT VERIFIED'

        self.detail = detail
        self.status_code = 400


class RoleNotCorrect(HTTPException):
    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'FORBIDDEN PLZ CHECK THE ROLE'

        self.detail = detail
        self.status_code = 403
