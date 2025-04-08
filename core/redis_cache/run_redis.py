import redis

from core.settings import settings

r = redis.Redis(host=settings.Redis.HOST, port=settings.Redis.PORT, decode_responses=True)