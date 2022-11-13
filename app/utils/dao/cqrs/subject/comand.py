from uuid import UUID

from app.utils.dao.cqrs import dao
from app.utils.dao.model.subject import Subject


def create_subject(_id: UUID.bytes, name: str, title: str, kind: str):
    with dao.session_scope() as session:
        session.add(
            Subject(
                id=_id,
                kind=kind,
                name=name,
                title=title
            )
        )
