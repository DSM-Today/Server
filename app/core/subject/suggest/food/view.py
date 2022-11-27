from fastapi import APIRouter, status

from app.core.subject.suggest.food.service import query_food

food_router = APIRouter(
    prefix='/suggest/food'
)


@food_router.get('/', status_code=status.HTTP_200_OK)
def get_food():
    return query_food()
