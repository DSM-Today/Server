from fastapi import FastAPI

from app.core.auth import auth_router


def create_app():
    app = FastAPI(
        docs_url='/swagger',
        redoc_url='/redoc'
    )

    app.include_router(auth_router)

    return app
