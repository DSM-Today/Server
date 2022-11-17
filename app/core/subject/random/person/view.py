from fastapi import APIRouter, status

from app.utils import show_reason

from app.core.subject.random.person.service import query_person

person_router = APIRouter(
    prefix='/random/person'
)


@person_router.get('/', status_code=status.HTTP_200_OK)
@show_reason
def get_person():
    return query_person()
