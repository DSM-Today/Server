from fastapi import APIRouter, status

from app.core.subject.suggest.music.service import query_music


music_router = APIRouter(
    prefix='/suggest/music'
)


@music_router.get('/', status_code=status.HTTP_200_OK)
def get_music():
    return query_music()
