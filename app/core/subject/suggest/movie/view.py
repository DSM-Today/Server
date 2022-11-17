from fastapi import APIRouter, Depends, status

from app.utils import show_reason
from app.utils.security import oauth2_scheme

from app.core.subject.suggest.movie.service import query_movie

movie_router = APIRouter(
    prefix='/suggest/movie'
)


@movie_router.get('/', status_code=status.HTTP_200_OK)
@show_reason
def get_movie():
    return query_movie()
