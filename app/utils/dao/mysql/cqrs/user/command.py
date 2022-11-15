from uuid import uuid4, UUID
from datetime import date

from app.utils.dao.mysql.cqrs import dao
from app.utils.dao.mysql.model.user import User


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


def initialize_user_info(user_id: UUID.hex, introduce: str, birth_day: date, can_person: bool):
    with dao.session_scope() as session:
        session.query(User).filter(User.id == UUID(user_id).bytes).update(
            {
                'can_person': can_person,
                'birth_day': birth_day,
                'introduce': introduce
            }
        )


def update_user_profile_by_id(user_id: UUID.hex, name: str, image_path: str, birth_day: date, introduce: str):
    with dao.session_scope() as session:
        session.query(User).filter(User.id == UUID(user_id).bytes).update(
            {
                'name': name if name not in [None, '', ' '] else User.name,
                'introduce': introduce,
                'birth_day': birth_day if birth_day is not None else User.birth_day,
                'image_path': image_path if image_path is not None else User.image_path
            }
        )
