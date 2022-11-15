from app.utils.dao.mysql.cqrs import dao

from sqlalchemy import text


def query_subject_title_list_by_kind(kind: str):
    query = f"select ts.name as subject, ts.title as title, (" \
            f"select count(tb.subject_name) as bookmark_amount from tbl_bookmark tb where subject_name like ts.name) as bookmark_amount " \
            f"from tbl_subject ts" \
            f" where ts.kind like  '{kind}'" \
            f"group by ts.name, ts.title;"

    with dao.execute_query() as engine:
        return engine(text(query)).all()

