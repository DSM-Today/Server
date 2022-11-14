from sqlalchemy import Column, BINARY, CHAR, VARCHAR, TEXT, DATE, BOOLEAN

from app.utils.dao.model import Base


class User(Base):
    __tablename__ = 'tbl_user'

    id = Column(BINARY(16), nullable=False, primary_key=True)
    email = Column(VARCHAR(30), nullable=False, unique=True)
    name = Column(CHAR(5), nullable=False)
    image_path = Column(VARCHAR(255), nullable=False)
    introduce = Column(VARCHAR(255), nullable=True)
    birth_day = Column(DATE, nullable=True)
    can_person = Column(BOOLEAN, nullable=False, default=False)
