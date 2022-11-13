from sqlalchemy import ForeignKey, Column, CHAR
from sqlalchemy.orm import relationship

from app.utils.dao.model import Base


class Bookmark(Base):
    __tablename__ = 'tbl_bookmark'

    user_id = Column(ForeignKey('tbl_user.id'), primary_key=True)
    subject_name = Column(CHAR(15), nullable=False)
    subject_kind = Column(CHAR(15), nullable=False)
    subject_title = Column(CHAR(15), nullable=False)

    user = relationship('User')