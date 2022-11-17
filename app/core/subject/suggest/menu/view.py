from fastapi import APIRouter, status

from app.core.subject.suggest.menu.service import get_random_cafe_menu

menu_router = APIRouter(
    prefix='/suggest/menu'
)


@menu_router.get('/', status_code=status.HTTP_200_OK)
def get_random_menu():
    return get_random_cafe_menu()
