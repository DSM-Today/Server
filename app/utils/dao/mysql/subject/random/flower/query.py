from sqlalchemy.sql import func

from app.utils.dao.mysql.cqrs import dao

from app.utils.dao.mysql.subject.random.flower import Flower


def query_random_flower():
    with dao.session_scope() as session:
        return session.query(Flower.name, Flower.image_path, Flower.fairy_tale)\
            .order_by(func.rand()).limit(1).one()