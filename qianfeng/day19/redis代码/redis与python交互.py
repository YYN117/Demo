import redis

#连接
r = redis.StrictRedis(host = 'localhost',port=6379,password=1234)

#读写方式1：根据数据类型的不同，调用相应的方法
#写数据
# r.set('t1','good')
# 读数据
# print(r.get('t1'))
#1push key value [value ....]

# 方法2：pipeline
#缓存多条命令，然后依次执行，减少服务器-客户端的TCP数据包
pipe = r.pipeline()
pipe.set('t2','fuck')
pipe.set('t3','dick')
pipe.set('t4','penis')
pipe.execute()