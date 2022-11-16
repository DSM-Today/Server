from typing import Union

from fastapi import status, APIRouter, Header

from app.utils import show_reason

from app.core.auth.service import reissue_both_token

auth_router = APIRouter(
    prefix='/auth'
)


@auth_router.put('/token', status_code=status.HTTP_200_OK)
@show_reason
def reissue_tokens(refresh_token: Union[str, None] = Header(default=None)):
    return reissue_both_token(refresh_token)
