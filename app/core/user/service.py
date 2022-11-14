from app.utils.security.token import get_user_id

from app.utils.dao.cqrs.bookmark.query import query_my_bookmark_list_by_id


def query_my_bookmark_list(token: str):
    user_id = get_user_id(token)

    return {
        'bookmark_list': query_my_bookmark_list_by_id(user_id)
    }
