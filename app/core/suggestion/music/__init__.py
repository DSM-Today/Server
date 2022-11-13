from fastapi import APIRouter, Depends, status

from app.utils.security import oauth2_scheme

from app.core.suggestion.music.service import query_music, add_music_to_bookmark, delete_my_music_bookmark


music_router = APIRouter(
    prefix='/suggest/music'
)


@music_router.get('/', status_code=status.HTTP_200_OK)
def get_music():
    return query_music()


@music_router.post('/', status_code=status.HTTP_201_CREATED)
def add_music_bookmark(token: str = Depends(oauth2_scheme)):
    add_music_to_bookmark(token)


@music_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def delete_music_bookmark(token: str = Depends(oauth2_scheme)):
    delete_my_music_bookmark(token)