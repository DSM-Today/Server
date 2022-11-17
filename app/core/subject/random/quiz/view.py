from fastapi import APIRouter, status

from app.utils import show_reason

from app.core.subject.random.quiz.service import get_quiz

quiz_router = APIRouter(
    prefix='/random/quiz'
)


@show_reason
@quiz_router.get('/', status_code=status.HTTP_200_OK)
def get_random_quiz():
    return get_quiz()
