from fastapi import FastAPI

from app.core.subject import Subject


class Suggest(Subject):
    KIND = 'SUGGEST'


def include_suggest_routers(app: FastAPI):
    from app.core.subject.suggest.view import suggest_router
    from app.core.subject.suggest.book.view import book_router
    from app.core.subject.suggest.food.view import food_router
    from app.core.subject.suggest.todo.view import todo_router
    from app.core.subject.suggest.menu.view import menu_router
    from app.core.subject.suggest.music.view import music_router
    from app.core.subject.suggest.movie.view import movie_router
    from app.core.subject.suggest.webtoon.view import webtoon_router

    app.include_router(suggest_router)
    app.include_router(book_router)
    app.include_router(food_router)
    app.include_router(webtoon_router)
    app.include_router(music_router)
    app.include_router(movie_router)
    app.include_router(menu_router)
    app.include_router(todo_router)
