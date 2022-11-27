from fastapi import APIRouter, Depends, status

from app.utils.security import oauth2_scheme

from app.core.subject.random.service import query_random_subject_list

random_router = APIRouter(
    prefix='/random'
)


@random_router.get('/list', status_code=status.HTTP_200_OK)
def get_information_list(token: str = Depends(oauth2_scheme)):
    return query_random_subject_list(token)
