from fastapi import APIRouter, status

from app.core.subject.suggest.movie.service import query_movie

movie_router = APIRouter(
    prefix='/suggest/movie'
)


@movie_router.get('/', status_code=status.HTTP_200_OK)
def get_movie():
    return query_movie()
