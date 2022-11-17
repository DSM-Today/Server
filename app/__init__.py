from fastapi import FastAPI

from app.core.auth import auth_router
from app.core.auth.oauth import oauth_router

from app.core.user import user_router

from app.core.subject.suggest.view import suggest_router
from app.core.suggestion.book import book_router
from app.core.suggestion.food import food_router
from app.core.subject.suggest.webtoon.view import webtoon_router
from app.core.subject.suggest.music.view import music_router
from app.core.subject.suggest.movie.view import movie_router
from app.core.suggestion.menu import menu_router
from app.core.subject.suggest.todo.view import todo_router

from app.core.subject.information.view import information_router
from app.core.subject.information.news.view import news_router
from app.core.subject.information.lotto.view import lotto_router

from app.core.subject.random.view import random_router
from app.core.subject.random.quiz.view import quiz_router
from app.core.subject.random.lion.view import lion_router
from app.core.subject.random.luck.view import luck_router
from app.core.subject.random.flower.view import flower_router
from app.core.subject.random.person.view import person_router


def _include_auth_router(app: FastAPI):
    app.include_router(auth_router)
    app.include_router(oauth_router)


def _include_user_router(app: FastAPI):
    app.include_router(user_router)


def _include_suggest_router(app: FastAPI):
    app.include_router(suggest_router)
    app.include_router(book_router)
    app.include_router(food_router)
    app.include_router(webtoon_router)
    app.include_router(music_router)
    app.include_router(movie_router)
    app.include_router(menu_router)
    app.include_router(todo_router)


def _include_random_routers(app: FastAPI):
    app.include_router(random_router)
    app.include_router(luck_router)
    app.include_router(quiz_router)
    app.include_router(flower_router)
    app.include_router(lion_router)
    app.include_router(person_router)


def _include_information_routers(app: FastAPI):
    app.include_router(news_router)
    app.include_router(lotto_router)
    app.include_router(information_router)


def create_app():
    app = FastAPI()

    _include_information_routers(app)
    _include_random_routers(app)
    _include_suggest_router(app)
    _include_user_router(app)
    _include_auth_router(app)

    return app
