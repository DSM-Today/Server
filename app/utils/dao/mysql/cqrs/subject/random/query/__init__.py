from sqlalchemy.sql import text

from app.utils.dao.mysql.cqrs import dao


def get_rand_quiz():
    with dao.execute_query() as engine:
        return engine(
            text(
                'select level, question, answer from tbl_quiz order by rand() limit 1'
            )
        ).one()
