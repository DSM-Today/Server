from app.utils.dao.cqrs.subject.query import query_subject_title_list_by_kind


def query_information_list():
    return {
        'information_subject_list': query_subject_title_list_by_kind('INFORMATION')
    }
