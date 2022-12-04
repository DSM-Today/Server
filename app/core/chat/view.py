from collections import deque

from fastapi_socketio import SocketManager

from app.core.chat.service import connect, unconnect, \
    join_room, left_room, message


def register_user_connect(sio: SocketManager):
    @sio.on('connect', namespace='/chat')
    def user_connect(sid, environ):
        token = environ['HTTP_AUTHORIZATION'].split()[1]
        connect(sid, token)


def register_user_unconnect(sio: SocketManager):
    @sio.on('unconnect')
    def user_unconnect(sid):
        unconnect(sid)


def register_user_join_room(sio: SocketManager):
    @sio.on('join_room', namespace='/chat')
    async def user_join_room(sid):
        await join_room(sid, sio=sio)


def register_user_left_room(sio: SocketManager):
    @sio.on('left_room')
    async def user_left_room(sid):
        left_room(sid, sio)


def register_user_message(sio: SocketManager):
    @sio.on('message', namespace='/chat')
    async def user_message(sid, data):
        await message(sid, data, sio=sio)
