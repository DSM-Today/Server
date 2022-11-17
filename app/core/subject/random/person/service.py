from uuid import uuid4

from app.core.subject.random.person import Person

from app.utils.dao.mysql.user.query import query_random_user
from app.utils.dao.mysql.cqrs.subject.comand import create_subject


def query_person():
    create_subject(uuid4().bytes, name=Person.NAME, title=Person.TITLE, kind=Person.KIND)

    return query_random_user()
