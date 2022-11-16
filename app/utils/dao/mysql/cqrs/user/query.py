from uuid import UUID
from datetime import date

from sqlalchemy.sql import func

from app.utils.dao.mysql.cqrs import dao

from app.utils.dao.mysql.model.user import User


def user_exist_by_email(email: str):
    with dao.session_scope() as session:
        return session.query(User.email).filter(User.email == email).scalar()


def query_id_by_email(email: str):
    with dao.session_scope() as session:
        return session.query(User.id).filter(User.email == email).one()['id'].hex()


def query_user_birth_by_id(_id: UUID.hex) -> date:
    with dao.session_scope() as session:
        return session.query(User.birth_day).filter(User.id == UUID(_id).bytes).one()['birth_day']


def query_user_by_id(_id: UUID.hex):
    with dao.session_scope() as session:
        return session.query(User).filter(User.id == UUID(_id).bytes).one()


def query_user_by_email(email: str):
    with dao.session_scope() as session:
        return session.query(User).filter(User.email == email).one()


def query_random_user():
    with dao.session_scope() as session:
        return session.query(
            User.image_path,
            User.name,
            User.introduce
        )\
            .filter(User.can_person == True)\
            .order_by(func.rand()).limit(1).one()
