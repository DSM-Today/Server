from fastapi import FastAPI

from app.core.auth import auth_router
from app.core.auth.oauth import oauth_router

from app.core.user import user_router

from app.core.suggestion import suggest_router
from app.core.suggestion.book import book_router
from app.core.suggestion.food import food_router
from app.core.suggestion.webtoon import webtoon_router
from app.core.suggestion.music import music_router
from app.core.suggestion.movie import movie_router
from app.core.suggestion.menu import menu_router
from app.core.suggestion.todo import todo_router

from app.core.information import information_router
from app.core.information.news import news_router
from app.core.information.lotto import lotto_router

from app.core.random import random_router
from app.core.random.luck import luck_router
from app.core.random.quiz import quiz_router
from app.core.random.flower import flower_router
from app.core.random.lion import lion_router


def create_app():
    app = FastAPI(
        docs_url='/swagger',
        redoc_url='/redoc'
    )

    # auth
    app.include_router(auth_router)
    app.include_router(oauth_router)

    # user
    app.include_router(user_router)

    # suggest
    app.include_router(suggest_router)
    app.include_router(book_router)
    app.include_router(food_router)
    app.include_router(webtoon_router)
    app.include_router(music_router)
    app.include_router(movie_router)
    app.include_router(menu_router)
    app.include_router(todo_router)

    # random
    app.include_router(random_router)
    app.include_router(luck_router)
    app.include_router(quiz_router)
    app.include_router(flower_router)
    app.include_router(lion_router)

    # information
    app.include_router(news_router)
    app.include_router(lotto_router)
    app.include_router(information_router)

    return app
