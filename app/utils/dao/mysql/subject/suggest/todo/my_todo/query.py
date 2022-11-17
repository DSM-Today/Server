from sqlalchemy.sql import text

from app.utils.dao.mysql import dao


def query_my_todo_list(user_id: str):
    with dao.execute_query() as execute:
        query = "select HEX(tt.id) as todo_id, tt.content " \
                "from tbl_my_todo mtd " \
                "join tbl_todo tt on tt.id = mtd.todo_id " \
                f"where user_id like UNHEX('{user_id}')"

        return execute(text(query)).all()
