from app.utils.dao.cqrs.subject.query import query_subject_title_list_by_kind


def query_random_subject_list():
    return query_subject_title_list_by_kind('RANDOM')
