from fastapi import APIRouter, status

from app.utils import show_reason

from app.core.suggestion.service import query_suggest_subject_list

suggest_router = APIRouter(
    prefix='/suggest'
)


@suggest_router.get('/list', status_code=status.HTTP_200_OK)
@show_reason
def get_information_list():
    return query_suggest_subject_list()
