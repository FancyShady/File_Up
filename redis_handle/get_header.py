import logging
import redis


logging.basicConfig(level=logging.NOTSET)
redis_client = redis.StrictRedis(host='127.0.0.1', port=6379,
                                 db=0, decode_responses=True)
keys = redis_client.keys()
print(type(keys))
print(keys)

