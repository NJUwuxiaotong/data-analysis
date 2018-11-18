import redis

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
r.set('site', 'www.qi.cn')

print(r.get('site'))
