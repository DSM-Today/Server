from uuid import uuid4

from app.core.subject.suggest.movie import Movie

from app.utils.dao.mysql.cqrs.subject.suggest.movie.query import query_random_movie
from app.utils.dao.mysql.subject.comand import create_subject


def query_movie():
    create_subject(uuid4().bytes, name=Movie.NAME, title=Movie.TITLE, kind=Movie.KIND)

    return query_random_movie()

#    return movie_crawler.crawl()
