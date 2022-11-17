from uuid import uuid4

from app.utils.type_changer import str_to_date

from app.utils.dataset.crawler.information.lotto import lotto_crawler

from app.utils.dao.mysql.cqrs.subject.comand import create_subject

from app.core.subject.information.lotto import Lotto


def query_lotto():
    lotto = lotto_crawler.crawl()
    lotto['date'] = str_to_date(lotto['date'].replace('.', ''))

    create_subject(_id=uuid4().bytes, name=Lotto.NAME, title=Lotto.TITLE, kind=Lotto.KIND)
    return lotto
