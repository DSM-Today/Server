from requests import get

from app.utils.security.oauth.impl import OAuth
from app.config import GoogleConfig as _Config

from app.utils.exception.custom import NotVerifiedIdToken


class Google(OAuth):

    def query_client_id(self):
        return _Config.CLIENT_ID

    def check_id_token_verify(self, id_token: str):
        response = get(
            f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}'
        ).json()

        if 'error' in response:
            raise NotVerifiedIdToken

        return response


google = Google()
