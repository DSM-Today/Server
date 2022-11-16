from app.utils.dao.mysql.cqrs.subject.query import query_subject_element_by_user_id_and_kind


def query_random_subject_list(token):
    return {
        'random_subject_list': query_subject_element_by_user_id_and_kind(token, 'RANDOM')
    }

