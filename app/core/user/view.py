from fastapi import Depends, APIRouter, status

from app.utils.security import oauth2_scheme

from app.core.user.dto import Request

from app.core.user.service import query_my_bookmark_list, query_my_profile, user_initialize_information, \
    update_user_profile

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


@user_router.patch('/profile', status_code=status.HTTP_200_OK)
@show_reason
def update_my_profile(request: Request.UpdateProfile, token: str = Depends(oauth2_scheme)):
    update_user_profile(
        token,
        name=request.name,
        introduce=request.introduce,
        image_path=request.image_path,
        birth_day=request.birth_day
    )


@user_router.patch('/profile/init', status_code=status.HTTP_200_OK)
@show_reason
def initialize_user_information(request: Request.InitProfile, token: str = Depends(oauth2_scheme)):
    user_initialize_information(
        token,
        introduce=request.introduce,
        birth_day=request.birth_day,
        can_person=request.can_person
    )
