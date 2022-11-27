import os

from dotenv import find_dotenv, load_dotenv

__env_file = find_dotenv()
load_dotenv(__env_file)


def get_chromedriver_path():
    return os.environ['CHROMEDRIVER_PATH']


class AWSConfig:
    ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
    SECRET_KEY = os.environ['AWS_SECRET_KEY']


class SocketConfig:
    PORT = 8000


class S3Config(AWSConfig):
    BUCKET_NAME = os.environ['BUCKET_NAME']
    LOCATION = os.environ['LOCATION']


class DatabaseConfig:
    DATABASE_URL = os.environ['DATABASE_URL']


class RedisConfig:
    HOST = os.environ['REDIS_HOST']
    PORT = os.environ['REDIS_PORT']


class JWTConfig:
    ACCESS_EXPIRE = int(os.environ['ACCESS_EXPIRE'])
    REFRESH_EXPIRE = int(os.environ['REFRESH_EXPIRE'])
    SECRET_KEY = os.environ['SECRET_KEY']
    ACCESS_NAME = os.environ['ACCESS_NAME']
    REFRESH_NAME = os.environ['REFRESH_NAME']
    ALGORITHM = os.environ['ALGORITHM']


class GoogleConfig:
    CLIENT_ID = os.environ['GOOGLE_OAUTH_CLIENT_ID']
