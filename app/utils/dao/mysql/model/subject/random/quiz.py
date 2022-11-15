from sqlalchemy import Column, ForeignKey, BINARY, CHAR, VARCHAR

from app.utils.dao.mysql.model import Base


class Quiz(Base):
    __tablename__ = 'tbl_quiz'

    id = Column(ForeignKey('tbl_subject.id'), primary_key=True)
    level = Column(CHAR(1), nullable=False)
    question = Column(VARCHAR(255), nullable=False)
    answer = Column(VARCHAR(255), nullable=False)


