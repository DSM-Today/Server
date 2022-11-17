from datetime import datetime, date


def str_to_date(origin_str: str):
    return datetime.strptime(origin_str, '%Y%m%d').date()


def str_to_month_with_day(origin_str: str):
    origin_date = datetime.strptime(origin_str, '%m%d').date()
    return f'{origin_date.month}-{origin_date.day}'


def date_to_int(from_data: date):
    return int(from_data.strftime('%Y%m%d').replace('-', ''))
