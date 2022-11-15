import redis

from app.config import RedisConfig as _Config

Redis = redis.StrictRedis(host=_Config.HOST, port=_Config.PORT, db=0)
