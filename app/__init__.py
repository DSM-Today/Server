from fastapi import FastAPI

from app.core.auth import auth_router
from app.core.auth.oauth import oauth_router

from app.core.user import include_user_router

from app.core.subject.random import include_random_routers
from app.core.subject.suggest import include_suggest_router

from app.core.subject.information.view import information_router
from app.core.subject.information.news.view import news_router
from app.core.subject.information.lotto.view import lotto_router

from app.core.bookmark.view import bookmark_router

from app.core.image import include_image_router


def _include_bookmark_router(app: FastAPI):
    app.include_router(bookmark_router)


def _include_auth_router(app: FastAPI):
    app.include_router(auth_router)
    app.include_router(oauth_router)


def _include_information_routers(app: FastAPI):
    app.include_router(news_router)
    app.include_router(lotto_router)
    app.include_router(information_router)


def create_app():
    app = FastAPI()

    include_user_router(app)

    include_image_router(app)

    _include_information_routers(app)
    include_random_routers(app)
    include_suggest_router(app)

    _include_auth_router(app)
    _include_bookmark_router(app)

    return app
