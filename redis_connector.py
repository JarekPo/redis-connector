import os
import redis

redis_host = os.environ.get('REDIS_HOST')
redis_port = os.environ.get('REDIS_PORT')
redis_username = os.environ.get('REDIS_USERNAME')
redis_password = os.environ.get('REDIS_PASSWORD')

try:
    r = redis.Redis(
        host=redis_host,
        port=redis_port,
        decode_responses=True,
        username=redis_username,
        password=redis_password,
    )

    r.ping()
    print("Connected to Redis!")
except redis.ConnectionError as e:
    print(f"Redis connection error: {e}")
