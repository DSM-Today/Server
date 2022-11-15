from fastapi import APIRouter, Depends, status

from app.utils import show_reason

from app.core.random.service import query_random_subject_list

random_router = APIRouter(
    prefix='/random'
)


@random_router.get('/list', status_code=status.HTTP_200_OK)
@show_reason
def get_information_list():
    return query_random_subject_list()
