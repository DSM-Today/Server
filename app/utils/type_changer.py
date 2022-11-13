from datetime import datetime, date


def str_to_date(origin_str: str):
    return datetime.strptime(origin_str, '%Y%m%d').date()


def date_to_int(from_data: date):
    return int(from_data.strftime('%Y%m%d').replace('-', ''))