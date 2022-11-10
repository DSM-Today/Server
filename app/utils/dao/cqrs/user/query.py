from app.utils.dao.model.user import User
from app.utils.dao.cqrs import dao


def user_exist_by_email(email: str):
    with dao.session_scope() as session:
        return session.query(User.email).filter(User.email == email).scalar()