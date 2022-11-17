from app.core.subject.information import Information

from app.utils.security.token import get_user_id
from app.utils.dao.mysql.subject.query import query_subject_element_by_user_id_and_kind


def query_information_list(token):
    user_id = get_user_id(token)

    return {
        'information_subject_list': query_subject_element_by_user_id_and_kind(user_id, Information.KIND)
    }
