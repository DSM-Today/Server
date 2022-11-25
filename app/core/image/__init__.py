from fastapi import FastAPI

from app.core.image.view import image_router


def include_image_router(app: FastAPI):
    app.include_router(image_router)