from app.core import Random

from app.utils.dao.mysql.cqrs.subject.random.quiz.query import get_rand_quiz

Quiz = Random.Quiz


def get_quiz():
    return get_rand_quiz()
