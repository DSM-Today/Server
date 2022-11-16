from app.utils.dao.mysql.model import Base

from sqlalchemy import Column, ForeignKey, VARCHAR


class Todo(Base):
    __tablename__ = 'tbl_todo'

    id = Column(ForeignKey('tbl_subject.id'), primary_key=True)
    content = Column(VARCHAR(255), nullable=False)
