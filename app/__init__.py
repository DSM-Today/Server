from fastapi import FastAPI

from app.core.auth import auth_router
from app.core.auth.oauth import oauth_router

from app.core.user import include_user_router

from app.core.subject.random import include_random_routers
from app.core.subject.suggest import include_suggest_routers
from app.core.subject.information import include_information_routers

from app.core.bookmark.view import bookmark_router

from app.core.image import include_image_router


def _include_bookmark_router(app: FastAPI):
    app.include_router(bookmark_router)


def _include_auth_router(app: FastAPI):
    app.include_router(auth_router)
    app.include_router(oauth_router)


def create_app():
    app = FastAPI()

    include_user_router(app)

    include_image_router(app)

    include_random_routers(app)
    include_suggest_routers(app)
    include_information_routers(app)

    _include_auth_router(app)
    _include_bookmark_router(app)

    return app
