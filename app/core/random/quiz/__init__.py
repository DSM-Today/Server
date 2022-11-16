from fastapi import APIRouter, Depends

from app.utils.security import oauth2_scheme

from app.core.random.quiz.service import get_quiz, add_quiz_to_bookmark, delete_my_quiz_bookmark

quiz_router = APIRouter(
    prefix='/random/quiz'
)


@quiz_router.get('/')
def get_random_quiz():
    return get_quiz()


@quiz_router.post('/')
def add_quiz_bookmark(token: str = Depends(oauth2_scheme)):
    add_quiz_to_bookmark(token)


@quiz_router.delete('/')
def delete_quiz_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_quiz_bookmark(token)
