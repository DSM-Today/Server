from uuid import uuid4

from app.core.subject.suggest.music import Music

from app.utils.dataset.crawler.operation.music import music_crawler

from app.utils.dao.mysql.subject.comand import create_subject


def query_music():
    create_subject(uuid4().bytes, name=Music.NAME, title=Music.TITLE, kind=Music.KIND)

    return music_crawler.crawl()