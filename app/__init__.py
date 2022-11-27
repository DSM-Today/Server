from fastapi import FastAPI

from app.utils.exception import initialize_exception_handler

from app.core.chat import initialize_socket, include_chat_router

from app.core.user import include_user_router

from app.core.auth import include_auth_routers

from app.core.image import include_image_router

from app.core.bookmark import include_bookmark_router

from app.core.subject.random import include_random_routers
from app.core.subject.suggest import include_suggest_routers
from app.core.subject.information import include_information_routers


def create_app():
    app = FastAPI()

    # exception
    initialize_exception_handler(app)

    # chat
    initialize_socket(app)
    include_chat_router(app)

    # user router
    include_user_router(app)

    # auth router
    include_auth_routers(app)

    # image router
    include_image_router(app)

    # bookmark router
    include_bookmark_router(app)

    # subject router
    include_random_routers(app)
    include_suggest_routers(app)
    include_information_routers(app)

    return app
