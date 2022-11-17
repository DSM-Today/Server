from uuid import UUID

from sqlalchemy import text

from app.utils.dao.mysql.cqrs import dao


def query_subject_element_by_user_id_and_kind(user_id: UUID.hex, kind: str):
    query = f"select ts.name as name, ts.title as title," \
            f"(select count(tb.subject_name) as _count from tbl_bookmark tb where tb.subject_name like ts.name) as amount," \
            f"unhex('{user_id}') in (select user_id from tbl_bookmark tb2 where tb2.subject_name like ts.name) as is_marked " \
            f"from tbl_subject ts where ts.kind like '{kind}' " \
            f"group by ts.name, ts.title;"

    with dao.execute_query() as engine:
        return engine(text(query)).all()
