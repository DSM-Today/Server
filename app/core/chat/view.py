from app.core.chat import socket_manager


@socket_manager().on('connect')
def enter_room():
    pass


@socket_manager().on('disconnect')
def left_room():
    pass


@socket_manager().on('message')
def catch_and_send():
    print('aa')
