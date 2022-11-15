from uuid import UUID
from app.utils.dao.mysql.cqrs import dao
from app.utils.dao.mysql.model.bookmark import Bookmark

from sqlalchemy.sql import text


def create_bookmark(user_id: UUID.hex, name: str, kind: str, title: str):
    with dao.session_scope() as session:
        session.add(
            Bookmark(
                user_id=UUID(user_id).bytes,
                subject_name=name,
                subject_title=title,
                subject_kind=kind
            )
        )


def delete_bookmark_by_user_id_and_name(user_id: UUID.hex, subject_name: str):
    with dao.execute_query() as engine:
        engine.execute(text(
            f"DELETE FROM tbl_bookmark WHERE subject_name like '{subject_name}' and user_id like UNHEX('{user_id}')"
        ))
