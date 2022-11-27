from pydantic import BaseModel


class Request:
    class IdToken(BaseModel):
        id_token: str
