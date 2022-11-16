from uuid import UUID

from app.utils.dao.mysql.cqrs import dao

from app.utils.dao.mysql.model.subject.suggest.todo.my_todo import MyTodo


def add_my_todo(user_id, todo_id):
    with dao.session_scope() as session:
        session.add(
            MyTodo(
                user_id=UUID(user_id).bytes,
                todo_id=UUID(todo_id).bytes
            )
        )
