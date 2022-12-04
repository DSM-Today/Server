from fastapi import FastAPI
from fastapi_socketio import SocketManager

from app.core.chat.view import register_user_connect, register_user_unconnect,\
    register_user_message, register_user_join_room, register_user_left_room


def initialize_socket(app: FastAPI):
    sio = SocketManager(app=app, mount_location='/', async_mode="asgi")

    register_user_connect(sio)
    register_user_unconnect(sio)
    register_user_join_room(sio)
    register_user_left_room(sio)
    register_user_message(sio)
