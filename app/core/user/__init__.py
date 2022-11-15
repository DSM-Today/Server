from fastapi import Depends, APIRouter

from app.utils.security import oauth2_scheme

from app.core.user.service import query_my_bookmark_list, query_my_profile

from app.utils import show_reason

user_router = APIRouter(
    prefix='/user'
)


@user_router.get('/list')
@show_reason
def get_my_bookmark_list(token: str = Depends(oauth2_scheme)):
    return query_my_bookmark_list(token)


@user_router.get('/profile')
@show_reason
def show_my_profile(token: str = Depends(oauth2_scheme)):
    return query_my_profile(token)

