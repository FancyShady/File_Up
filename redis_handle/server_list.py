import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0,
                            decode_responses=True)
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline()
pipe_size = 100000

len = 0
key_list = []
print(r.pipeline())
keys = r.keys()
for key in keys:
    key_list.append(key)
    pipe.get(key)
    if len < pipe_size:
        len += 1
    else:
        for (k, v) in zip(key_list, pipe.execute()):
            print(k, v)
        len = 0
        key_list = []

for (k, v) in zip(key_list, pipe.execute()):
    print(k, v)
