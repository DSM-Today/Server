from requests import get

from fastapi import HTTPException

from app.utils.security.oauth.impl import OAuth
from app.config import GoogleConfig as _Config


class Google(OAuth):

    def query_client_id(self):
        return _Config.CLIENT_ID

    def check_id_token_verify(self, id_token: str):
        response = get(
            f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}'
            ).json()

        if 'error' in response:
            raise HTTPException(400, "ID TOKEN NOT VERIFIED")

        return response


google = Google()
