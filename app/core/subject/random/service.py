from app.core.subject.random import Random

from app.utils.security.token import get_user_id

from app.utils.dao.mysql.cqrs.subject.query import query_subject_element_by_user_id_and_kind


def query_random_subject_list(token):
    user_id = get_user_id(token)
    return {
        'random_subject_list': query_subject_element_by_user_id_and_kind(user_id, Random.KIND)
    }
