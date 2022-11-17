from fastapi import APIRouter, status

from app.core.subject.random.flower.service import query_flower

flower_router = APIRouter(
    prefix='/random/flower'
)


@flower_router.get('/', status_code=status.HTTP_200_OK)
def get_flower():
    return query_flower()
