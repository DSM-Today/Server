from fastapi import FastAPI

from app.core.auth import auth_router

from app.core.information import information_router
from app.core.information.news import news_router
from app.core.information.lotto import lotto_router

from app.core.random import random_router
from app.core.random.luck import luck_router


def create_app():
    app = FastAPI(
        docs_url='/swagger',
        redoc_url='/redoc'
    )

    app.include_router(auth_router)

    # random
    app.include_router(random_router)
    app.include_router(luck_router)

    # information
    app.include_router(news_router)
    app.include_router(lotto_router)
    app.include_router(information_router)

    return app
