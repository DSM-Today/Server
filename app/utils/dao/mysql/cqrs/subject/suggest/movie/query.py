from sqlalchemy.sql import func
from app.utils.dao.mysql.cqrs import dao

from app.utils.dao.mysql.model.subject.suggest.movie import Movie


def query_random_movie():
    with dao.session_scope() as session:
        return session.query(Movie.name, Movie.image_path, Movie.content, Movie.url).order_by(func.rand()).limit(1).one()
