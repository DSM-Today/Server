from fastapi import APIRouter

from app.core.subject.random.quiz.service import get_quiz

quiz_router = APIRouter(
    prefix='/random/quiz'
)


@quiz_router.get('/')
def get_random_quiz():
    return get_quiz()
