from uuid import uuid4

from app.core.subject.suggest.food import Food

from app.utils.dataset.crawler.operation.food import food_crawler

from app.utils.dao.mysql.cqrs.subject.comand import create_subject

from app.utils.dao.mysql.cqrs.subject.suggest.food.query import query_random_food


def query_food():
    create_subject(uuid4().bytes, name=Food.NAME, title=Food.TITLE, kind=Food.KIND)

    return query_random_food()

    # return food_crawler.crawl()
