from pydantic import BaseModel


class DTO:
    class IdTokenRequest(BaseModel):
        id_token: str
