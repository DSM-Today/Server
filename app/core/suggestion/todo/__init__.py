from fastapi import APIRouter, Depends

from app.utils.security import oauth2_scheme

from app.core.suggestion.todo.service import query_all_todo_list, insert_to_my_todo

todo_router = APIRouter(
    prefix='/suggest/todo'
)


@todo_router.get('/list')
def get_todo_list(token: str = Depends(oauth2_scheme)):
    return query_all_todo_list(token)


@todo_router.get('/my-list')
def get_my_todo_list(token: str = Depends(oauth2_scheme)):
    pass


@todo_router.post('/{todo_id}')
def add_to_my_todo(todo_id: str, token: str = Depends(oauth2_scheme)):
    insert_to_my_todo(token, todo_id)


@todo_router.delete('/{todo_id}')
def delete_from_my_todo(todo_id: str, token: str = Depends(oauth2_scheme)):
    pass
