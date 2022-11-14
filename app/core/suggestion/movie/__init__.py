from fastapi import APIRouter, Depends, status

from app.utils.security import oauth2_scheme

from app.core.suggestion.movie.service import query_movie, add_movie_to_bookmark, delete_my_movie_bookmark

movie_router = APIRouter(
    prefix='/suggest/movie'
)


@movie_router.get('/', status_code=status.HTTP_200_OK)
def get_movie():
    return query_movie()


@movie_router.post('/', status_code=status.HTTP_201_CREATED)
def add_movie_bookmark(token: str = Depends(oauth2_scheme)):
    add_movie_to_bookmark(token)


@movie_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def delete_movie_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_movie_bookmark(token)
