from uuid import uuid4, UUID
from datetime import date

from app.utils.dao.cqrs import dao
from app.utils.dao.model.user import User


def save_user(email: str, name: str, image_path: str, can_person: bool):
    with dao.session_scope() as session:
        user = User(
            id=uuid4().bytes,
            email=email,
            name=name,
            image_path=image_path,
            can_person=can_person
        )
        session.add(user)
        return user