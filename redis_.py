"""
连接 redis-cli -h 主机 -p 端口
切换数据库 select num

string :
增 set/mset/append key value
删 del key
改 set key
查 get/mget key

list :
增 lpush/rpush key value 或 linsert key before/after value new-value
删 lrem key count value
改 lset key index value
查 lrange key index0 index1

set:
增 sadd key value
删 srem key value
查 smembers key

zset:
增 zadd key score value
删 zrem key value
查 zrange key index0 index1

hash:
增/改 hset/hmset obj key value
删 hdel obj key
查 hget/hmget obj key 或 hkeys key / hvals key

键:
查找键： keys pattern
判断键是否存在： exists key
查看值的类型： type key
删除键值对： del key1

"""

import redis
import pickle

class AA(object):
    name = "meng"

redis_cli = redis.StrictRedis(host="192.168.49.154", port=6379, db=0)
redis_cli.lpush("test", pickle.dumps(AA))
vv = pickle.loads(redis_cli.rpop("test"))
print(vv.name)

