from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.subject.suggest.todo.query import query_todo_list
from app.utils.dao.mysql.cqrs.subject.suggest.todo.command import add_my_todo, delete_todo_from_my_list


def query_all_todo_list(token: str):
    user_id = get_user_id(token)

    return {
        "todo_list": query_todo_list(user_id)
    }


def insert_to_my_todo(token: str, todo_id: str):
    user_id = get_user_id(token)

    add_my_todo(
        user_id=user_id,
        todo_id=todo_id
    )


def delete_from_my_todo_list(token: str, todo_id: str):
    user_id = get_user_id(token)

    delete_todo_from_my_list(user_id, todo_id)