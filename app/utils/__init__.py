import sys

from fastapi import HTTPException

from functools import wraps


def show_reason(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except:
            ex_class, ex_object, ex_index = sys.exc_info()

            if isinstance(ex_object, HTTPException):
                raise ex_object

            raise HTTPException(
                status_code=500,
                detail=str(ex_class.__name__) + ' :: ' + str(ex_object)
            )

    return wrapper
