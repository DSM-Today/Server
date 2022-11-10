from requests import post, get

from app.utils.security.oauth.impl import OAuth
from app.config import GoogleConfig as _Config


class Google(OAuth):

    def query_oauth_link(self):
        return 'https://accounts.google.com/o/oauth2/v2/auth?' \
               f'client_id={_Config.CLIENT_ID}' \
               f'&redirect_uri={_Config.CODE_URI}' \
               f'&scope={_Config.SCOPE}' \
               f'&response_type=code'

    def query_access_token(self, code: str):
        return post(
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            url=f'https://oauth2.googleapis.com/token'
                f'?code={code}'
                f'&client_id={_Config.CLIENT_ID}'
                f'&client_secret={_Config.SECRET_KEY}'
                f'&redirect_uri={_Config.CODE_URI}'
                f'&grant_type=authorization_code'
        ).json()

    def query_userinfo(self, access_token):
        return get(
            url=f"https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={access_token}"
        ).json()

    def query_birthday(self, access_token):
        return get(
            headers={
                'Authorization': 'Bearer ' + access_token
            },
            url=f'https://people.googleapis.com/v1/people/me?key={_Config.API_KEY}&personFields=birthdays'
        ).json()['birthdays'][0]['date']


google = Google()
