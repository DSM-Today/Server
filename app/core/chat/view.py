from fastapi import APIRouter

from app.config import SocketConfig
from app.core.chat import socket_manager

chat_router = APIRouter()


@chat_router.get('/chat/ports')
def get_socket_port():
    return {
        'port': SocketConfig.PORT
    }


@socket_manager().on('connect')
def enter_room():
    pass


@socket_manager().on('disconnect')
def left_room():
    pass


@socket_manager().on('message')
def catch_and_send():
    print('aa')
