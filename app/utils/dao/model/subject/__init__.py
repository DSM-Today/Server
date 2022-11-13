from sqlalchemy import Column, BINARY, CHAR

from app.utils.dao.model import Base


class Subject(Base):
    __tablename__ = 'tbl_subject'

    id = Column(BINARY(16), primary_key=True)
    kind = Column(CHAR(15), nullable=False)
    name = Column(CHAR(15), nullable=False)
    title = Column(CHAR(15), nullable=False)

