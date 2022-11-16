from uuid import uuid4, UUID

from app.core import Suggestion

from app.utils.security.token import get_user_id

from app.utils.dataset.crawler.operation.music import music_crawler

from app.utils.dao.mysql.cqrs.subject.comand import create_subject
from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name

Music = Suggestion.Music


def query_music():
    create_subject(uuid4().bytes, name=Music.NAME, title=Music.TITLE, kind=Suggestion.KIND)

    return music_crawler.crawl()


def add_music_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id=user_id, name=Music.NAME, title=Music.TITLE, kind=Suggestion.KIND)


def delete_my_music_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, Music.NAME)
