from fastapi import Depends, APIRouter

from app.utils.security import oauth2_scheme

from app.core.user.service import query_my_bookmark_list

user_router = APIRouter(
    prefix='/user'
)


@user_router.get('/list')
def get_my_bookmark_list(token: str = Depends(oauth2_scheme)):
    return query_my_bookmark_list(token)
