from uuid import uuid4

from app.core.subject.information.news import News

from app.utils.dao.mysql.subject.comand import create_subject

from app.utils.dataset.crawler.information.news import news_crawler


def query_news():
    subject_id = uuid4().bytes
    news = news_crawler.crawl()

    create_subject(subject_id, name=News.NAME, title=News.TITLE, kind=News.KIND)

    return news
