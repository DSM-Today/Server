from datetime import datetime


def str_to_date(origin_str: str):
    return datetime.strptime(origin_str, '%Y%m%d').date()
