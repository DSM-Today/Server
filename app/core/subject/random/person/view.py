from fastapi import APIRouter, status

from app.core.subject.random.person.service import query_person

person_router = APIRouter(
    prefix='/random/person'
)


@person_router.get('/', status_code=status.HTTP_200_OK)
def get_person():
    return query_person()
