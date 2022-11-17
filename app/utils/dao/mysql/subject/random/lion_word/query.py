from sqlalchemy.sql import func

from app.utils.dao.mysql import dao

from app.utils.dao.mysql.subject.random.lion_word import LionWord


def query_random_lion_word():
    with dao.session_scope() as session:
        return session.query(
            LionWord.korean, LionWord.chinese, LionWord.content.label('describe')
        ).order_by(func.rand()).limit(1).one()
