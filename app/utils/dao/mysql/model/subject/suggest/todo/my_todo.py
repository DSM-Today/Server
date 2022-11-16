from app.utils.dao.mysql.model import Base

from sqlalchemy import Column, ForeignKey


class MyTodo(Base):
    __tablename__ = 'tbl_my_todo'

    user_id = Column(ForeignKey('tbl_user.id'), primary_key=True)
    todo_id = Column(ForeignKey('tbl_todo.id'), primary_key=True)
