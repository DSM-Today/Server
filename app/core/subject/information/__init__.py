from fastapi import FastAPI

from app.core.subject import Subject


class Information(Subject):
    KIND = 'INFORMATION'


def include_information_routers(app: FastAPI):
    from app.core.subject.information.view import information_router
    from app.core.subject.information.news.view import news_router
    from app.core.subject.information.lotto.view import lotto_router

    app.include_router(information_router)
    app.include_router(news_router)
    app.include_router(lotto_router)
