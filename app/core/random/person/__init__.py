from fastapi import APIRouter, Depends, status

from app.utils import show_reason
from app.utils.security import oauth2_scheme

from app.core.random.person.service import query_person, delete_my_person_bookmark, add_person_to_bookmark

person_router = APIRouter(
    prefix='/random/person'
)


@person_router.get('/', status_code=status.HTTP_200_OK)
@show_reason
def get_person():
    return query_person()


@person_router.post('/', status_code=status.HTTP_201_CREATED)
@show_reason
def add_person_bookmark(token: str = Depends(oauth2_scheme)):
    add_person_to_bookmark(token)


@person_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
@show_reason
def delete_person_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_person_bookmark(token)
