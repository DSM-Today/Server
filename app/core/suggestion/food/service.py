from uuid import uuid4, UUID

from app.core import Suggestion

from app.utils.security.token import get_user_id

from app.utils.dataset.crawler.operation.food import food_crawler

from app.utils.dao.mysql.cqrs.subject.comand import create_subject
from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name

Food = Suggestion.Food


def query_food():
    create_subject(uuid4().bytes, name=Food.NAME, title=Food.TITLE, kind=Suggestion.KIND)

    return food_crawler.crawl()


def add_food_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id=user_id, name=Food.NAME, title=Food.TITLE, kind=Suggestion.KIND)


def delete_my_food_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, Food.NAME)
