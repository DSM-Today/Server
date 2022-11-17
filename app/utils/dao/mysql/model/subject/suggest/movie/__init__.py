from sqlalchemy import ForeignKey, Column, VARCHAR

from app.utils.dao.mysql.model import Base


class Movie(Base):

    __tablename__ = 'tbl_movie'

    id = Column(ForeignKey('tbl_subject.id'), primary_key=True)
    image_path = Column(VARCHAR(255), nullable=False)
    title = Column(VARCHAR(255), nullable=False)
    content = Column(VARCHAR(255), nullable=False)
    direct_url = Column(VARCHAR(255), nullable=False)
