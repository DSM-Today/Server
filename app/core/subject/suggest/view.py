from fastapi import APIRouter, Depends, status

from app.utils.security import oauth2_scheme

from app.core.subject.suggest.service import query_suggest_subject_list

suggest_router = APIRouter(
    prefix='/suggest'
)


@suggest_router.get('/list', status_code=status.HTTP_200_OK)
def get_information_list(token: str = Depends(oauth2_scheme)):
    return query_suggest_subject_list(token)
