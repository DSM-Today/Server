import sys

from fastapi import HTTPException

from functools import wraps


def show_reason(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except:
            raise HTTPException(
                status_code=500,
                detail=str(sys.exc_info()[0].__name__) + ' :: ' + str(sys.exc_info()[1])
            )

    return wrapper
