import os

from dotenv import find_dotenv, load_dotenv

__env_file = find_dotenv()
load_dotenv(__env_file)


def get_chromedriver_path():
    return os.environ['CHROMEDRIVER_PATH']


class DatabaseConfig:
    DATABASE_URL = os.environ['DATABASE_URL']


class JWTConfig:
    ACCESS_EXPIRE = os.environ['ACCESS_EXPIRE']
    REFRESH_EXPIRE = os.environ['REFRESH_EXPIRE']
    SECRET_KEY = os.environ['SECRET_KEY']
    ACCESS_NAME = os.environ['ACCESS_NAME']
    REFRESH_NAME = os.environ['REFRESH_NAME']
    ALGORITHM = os.environ['ALGORITHM']


class GoogleConfig:
    CLIENT_ID = os.environ['GOOGLE_OAUTH_CLIENT_ID']
    SECRET_KEY = os.environ['GOOGLE_OAUTH_SECRET']
    CODE_URI = os.environ['GOOGLE_CODE_URL']
    SCOPE = os.environ['GOOGLE_OAUTH_SCOPE']
    REDIRECT_URI = os.environ['GOOGLE_OAUTH_REDIRECT_URI']
    API_KEY = os.environ['GOOGLE_API_KEY']
