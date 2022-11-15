from datetime import date
from pydantic import BaseModel


class Request:
    class InitProfile(BaseModel):
        introduce: str
        birth_day: date
        can_person: bool

