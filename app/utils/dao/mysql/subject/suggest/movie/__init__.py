from sqlalchemy import ForeignKey, Column, VARCHAR, TEXT

from app.utils.dao.mysql import Base


class Movie(Base):

    __tablename__ = 'tbl_movie'

    id = Column(ForeignKey('tbl_subject.id'), primary_key=True)
    image_path = Column(VARCHAR(255), nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    content = Column(TEXT, nullable=False)
    url = Column(VARCHAR(255), nullable=False)
