from uuid import UUID

from app.utils.dao.mysql.cqrs import dao
from sqlalchemy.sql import text


def query_my_bookmark_list_by_id(user_id: UUID.hex):
    sql = f"select subject_name, subject_title, (" \
          f"select count(subject_name) as count from tbl_bookmark tb2 where tb2.subject_name like tb1.subject_name) as amount " \
          f"from tbl_bookmark tb1" \
          f" where user_id like UNHEX('{user_id}')"

    with dao.execute_query() as engine:
        return engine.execute(text(
            sql
        )).all()
