from fastapi import APIRouter, status

from app.utils import show_reason

from app.core.subject.information.lotto.service import query_lotto

lotto_router = APIRouter(
    prefix='/information/lotto'
)


@lotto_router.get('/', status_code=status.HTTP_200_OK)
@show_reason
def get_lotto():
    return query_lotto()

