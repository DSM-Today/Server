from fastapi import FastAPI

from app.core.user.view import user_router


def include_user_router(app: FastAPI):
    app.include_router(user_router)