from datetime import date
from typing import Optional

from pydantic import BaseModel


class Request:
    class InitProfile(BaseModel):
        introduce: str
        birth_day: date
        can_person: bool

    class UpdateProfile(BaseModel):
        name: Optional[str]
        introduce: Optional[str]
        image_path: Optional[str]
        birth_day: Optional[date]
