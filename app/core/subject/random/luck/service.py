from uuid import uuid4, UUID

from app.core.subject.random.luck import Luck

from app.utils.security.token import get_user_id

from app.utils.dataset.crawler.random.lucky import luck_crawler

from app.utils.dao.mysql.subject.comand import create_subject
from app.utils.dao.mysql.user.query import query_user_birth_by_id


def query_user_luck(token: str):
    user_id = UUID(get_user_id(token)).hex

    create_subject(uuid4().bytes, name=Luck.NAME, title=Luck.TITLE, kind=Luck.KIND)

    birth = query_user_birth_by_id(user_id)

    return luck_crawler.crawl(
        int(str(birth.month) + str(birth.day))
    )
