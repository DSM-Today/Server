from app.utils.dao.mysql.cqrs.subject.query import query_subject_title_list_by_kind


def query_suggest_subject_list():
    return {
        'suggest_subject_list': query_subject_title_list_by_kind('SUGGEST')
    }
