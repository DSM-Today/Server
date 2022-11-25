from fastapi import FastAPI

from app.core.user import include_user_router

from app.core.auth import include_auth_routers

from app.core.image import include_image_router

from app.core.bookmark import include_bookmark_router

from app.core.subject.random import include_random_routers
from app.core.subject.suggest import include_suggest_routers
from app.core.subject.information import include_information_routers


def create_app():
    app = FastAPI()

    include_user_router(app)

    include_auth_routers(app)

    include_image_router(app)

    include_bookmark_router(app)

    include_random_routers(app)
    include_suggest_routers(app)
    include_information_routers(app)

    return app
