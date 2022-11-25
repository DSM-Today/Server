from fastapi import FastAPI


def include_bookmark_router(app: FastAPI):
    from app.core.bookmark.view import bookmark_router

    app.include_router(bookmark_router)
