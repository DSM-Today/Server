from fastapi import APIRouter, Depends, status

from app.utils import show_reason
from app.utils.security import oauth2_scheme

from app.core.subject.random.luck.service import query_user_luck

luck_router = APIRouter(
    prefix='/random'
)


@luck_router.get('/lucky', status_code=status.HTTP_200_OK)
@show_reason
def get_my_luck(token: str = Depends(oauth2_scheme)):
    return query_user_luck(token)
