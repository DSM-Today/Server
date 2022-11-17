from uuid import UUID

from app.core import Random

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.bookmark.command import create_bookmark, delete_bookmark_by_user_id_and_name

from app.utils.dao.mysql.cqrs.subject.random.quiz.query import get_rand_quiz

Quiz = Random.Quiz


def get_quiz():
    return get_rand_quiz()


def add_quiz_to_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_bookmark(user_id, name=Quiz.NAME, title=Quiz.TITLE, kind=Random.KIND)


def delete_my_quiz_bookmark(token: str):
    user_id = UUID(get_user_id(token)).hex

    delete_bookmark_by_user_id_and_name(user_id, subject_name=Quiz.NAME)
