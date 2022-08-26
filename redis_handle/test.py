from redis import StrictRedis


redispool = StrictRedis(
    host='127.0.0.1',
    port=6379,
    db=0,
    decode_responses=True)

code = redispool.get('test')
print('token is: ', code)
