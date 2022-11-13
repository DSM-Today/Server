from fastapi import APIRouter, Depends, status

from app.utils.security import oauth2_scheme

from app.core.suggestion.food.service import query_food, add_food_to_bookmark, delete_my_food_bookmark

food_router = APIRouter(
    prefix='/suggest/food'
)


@food_router.get('/', status_code=status.HTTP_200_OK)
def get_food():
    return query_food()


@food_router.post('/', status_code=status.HTTP_201_CREATED)
def add_food_bookmark(token: str = Depends(oauth2_scheme)):
    add_food_to_bookmark(token)


@food_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def delete_food_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_food_bookmark(token)
