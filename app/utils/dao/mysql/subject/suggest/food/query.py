from sqlalchemy.sql import func

from app.utils.dao.mysql.cqrs import dao
from app.utils.dao.mysql.subject.suggest.food import Food


def query_random_food():
    with dao.session_scope() as session:
        return session.query(
            Food.name, Food.image_path
        )\
            .order_by(func.rand()).limit(1).one()
