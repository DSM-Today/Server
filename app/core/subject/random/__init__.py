from fastapi import FastAPI

from app.core.subject import Subject


class Random(Subject):
    KIND = 'RANDOM'


def include_random_routers(app: FastAPI):
    from app.core.subject.random.view import random_router
    from app.core.subject.random.quiz.view import quiz_router
    from app.core.subject.random.lion.view import lion_router
    from app.core.subject.random.luck.view import luck_router
    from app.core.subject.random.flower.view import flower_router
    from app.core.subject.random.person.view import person_router

    app.include_router(random_router)
    app.include_router(quiz_router)
    app.include_router(lion_router)
    app.include_router(luck_router)
    app.include_router(flower_router)
    app.include_router(person_router)
