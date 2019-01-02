import threading

def run():
    print('sunck is a good man')


#根据时间延时执行线程
t = threading.Timer(5,run)  #5秒后执行run
t.start()

t.join()
print('父线程结束')