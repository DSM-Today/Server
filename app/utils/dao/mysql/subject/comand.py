from uuid import UUID

from app.utils.dao.mysql.cqrs import dao
from app.utils.dao.mysql.subject import Subject


def create_subject(_id: UUID.bytes, name: str, title: str, kind: str): #TODO
    with dao.session_scope() as session:
        session.add(
            Subject(
                id=_id,
                kind=kind,
                name=name,
                title=title
            )
        )
