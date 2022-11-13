from uuid import uuid4, UUID

from app.utils.dao.cqrs.subject.comand import create_subject
from app.utils.dataset.crawler.operation.book import book_crawler


def query_book():

    create_subject(uuid4().bytes, name='BOOK', title='오늘의 책', kind='SUGGEST')

    return book_crawler.crawl()
