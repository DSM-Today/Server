from sqlalchemy import Column, ForeignKey, CHAR, VARCHAR

from app.utils.dao.mysql.model import Base


class LionWord(Base):
    __tablename__ = 'tbl_lion_word'

    id = Column(ForeignKey('tbl_subject.id'), primary_key=True)
    korean = Column(CHAR(15), nullable=False)
    chinese = Column(CHAR(15), nullable=False)
    content = Column(VARCHAR(255), nullable=False)
