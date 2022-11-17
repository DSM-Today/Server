from sqlalchemy.sql import text

from app.utils.dao.mysql import dao


def get_rand_menu():
    with dao.execute_query() as engine:
        return engine(
            text(
                'select image_path, brand_name, name  from tbl_menu order by rand() limit 1'
            )
        ).one()
