from uuid import uuid4, UUID
from datetime import date

from app.utils.dao.cqrs import dao
from app.utils.dao.model.user import User


def save_user(email: str, name: str, image_path: str, birth_day: date, can_person: bool,
              introduce: str, _id: UUID.bytes):
    if _id is None:
        _id = uuid4().bytes

    if introduce is None:
        introduce = name + ' 지구를 부술 유일한 인간..크큭'

    with dao.session_scope() as session:
        session.add(
            User(
                id=_id,
                email=email,
                name=name,
                image_path=image_path,
                introduce=introduce,
                birth_day=birth_day,
                can_person=can_person
            )
        )
        session.commit()
