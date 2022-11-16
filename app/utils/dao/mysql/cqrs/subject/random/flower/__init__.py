from sqlalchemy import Column, ForeignKey, VARCHAR

from app.utils.dao.mysql.model import Base


class Flower(Base):
    __tablename__ = 'tbl_flower'

    id = Column(ForeignKey('tbl_subject.id'), primary_key=True)
    name = Column(VARCHAR(25), nullable=False)
    fairy_tale = Column(VARCHAR(25), nullable=False)
    image_path = Column(VARCHAR(255), nullable=False)
