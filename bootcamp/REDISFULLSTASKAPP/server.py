import redis
import random

with redis.Redis() as redis_server:
    redis_server.lpush("queue", random.randint(1,10))
