import redis

yandex_key = 'YOUR YANDEX KEY'

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

db = redis.Redis(connection_pool=pool)

