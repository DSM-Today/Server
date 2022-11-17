from sqlalchemy.sql import text

from app.utils.dao.mysql.cqrs import dao


def query_todo_list(user_id: str):
    with dao.execute_query() as execute:
        query = "select HEX(td.id) as id, td.content as content, " \
                f"td.id in (select tmt2.todo_id from tbl_my_todo tmt2 where tmt2.user_id like UNHEX('{(user_id)}')) as is_my_todo" \
                " from tbl_todo td left join tbl_my_todo tmt on td.id = tmt.todo_id;"

        return execute(text(query)).all()


