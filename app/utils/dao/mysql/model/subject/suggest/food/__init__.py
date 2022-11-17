from sqlalchemy import ForeignKey, Column, VARCHAR

from app.utils.dao.mysql.model import Base


class Food(Base):
    __tablename__ = 'tbl_food'

    id = Column(ForeignKey('tbl_subject.id'), primary_key=True)
    name = Column(VARCHAR(15), nullable=False)
    image_path = Column(VARCHAR(255), nullable=False)
