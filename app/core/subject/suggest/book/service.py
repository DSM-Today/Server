from uuid import uuid4

from app.core.subject.suggest.book import Book

from app.utils.dao.mysql.subject.comand import create_subject

from app.utils.dataset.crawler.operation.book import book_crawler


def query_book():
    create_subject(uuid4().bytes, name=Book.NAME, title=Book.TITLE, kind=Book.KIND)

    return book_crawler.crawl()