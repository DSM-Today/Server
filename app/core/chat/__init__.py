from fastapi import FastAPI
from fastapi_socketio import SocketManager

from app.utils.exception.custom import SocketUnDefinedException

__socket_manager = None


def initialize_socket(app: FastAPI):
    global __socket_manager
    __socket_manager = SocketManager(app=app)


def socket_manager():
    if __socket_manager is None:
        raise SocketUnDefinedException

    return __socket_manager


def include_chat_router(app: FastAPI):
    from app.core.chat.view import chat_router

    app.include_router(chat_router)
