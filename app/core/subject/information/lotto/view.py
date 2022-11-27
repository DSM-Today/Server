from fastapi import APIRouter, status

from app.core.subject.information.lotto.service import query_lotto

lotto_router = APIRouter(
    prefix='/information/lotto'
)


@lotto_router.get('/', status_code=status.HTTP_200_OK)
def get_lotto():
    return query_lotto()

