from uuid import uuid4
from collections import deque

from fastapi_socketio import SocketManager

from app.utils.security.token import get_user_name, get_image_path

_user_connect_list = {}
_user_room_list = {}
_user_pending_list = deque()


def _produce_room_id(user_sid, opponent_sid):
    room_id = uuid4()
    _user_room_list[user_sid] = room_id
    _user_room_list[opponent_sid] = room_id
    return room_id


def connect(sid, token):
    _user_connect_list[sid] = {
        'name': get_user_name(token),
        'image_path': get_image_path(token)
    }


def unconnect(sid):
    del _user_connect_list[sid]


async def join_room(sid, sio: SocketManager):
    if sid not in _user_connect_list:
        raise

    if _user_pending_list:
        opponent_sid = _user_pending_list.popleft()
        room_id = _produce_room_id(sid, opponent_sid)

        sio.enter_room(sid=sid, room=room_id, namespace='/chat')
        sio.enter_room(sid=opponent_sid, room=room_id, namespace='/chat')

        await sio.emit('room_response', room=room_id, data={'content': 'Connected'}, namespace='/chat')

    else:
        _user_pending_list.append(sid)

        await sio.emit('room_response', to=sid, data={'content': 'Wait'}, namespace='/chat')


def left_room(sid, sio: SocketManager):
    room_id = _user_room_list[sid]

    sio.leave_room(sid=sid, room=room_id)
    del _user_room_list[sid]


async def message(sid, data, sio: SocketManager):
    room_id = _user_room_list[sid]
    sender_info = _user_connect_list[sid]
    await sio.emit('message', data={
        'sender': sender_info['name'],
        'image_path': sender_info['image_path'],
        'content': data['data']
    }, room=room_id, namespace='/chat')
