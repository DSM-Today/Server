from uuid import uuid4

from app.core.subject.suggest.webtoon import WebToon

from app.utils.dataset.crawler.operation.webtoon import webtoon_crawler

from app.utils.dao.mysql.subject.comand import create_subject


def query_webtoon():
    create_subject(uuid4().bytes, name=WebToon.NAME, title=WebToon.TITLE, kind=WebToon.KIND)

    return webtoon_crawler.crawl()
