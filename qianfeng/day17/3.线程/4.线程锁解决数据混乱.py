import threading
lock = threading.Lock()
num = 100
def run(a):
    global num
    for i in range(10000000):
        # 锁
        #确保了代码只能由一个线程从头到尾完整执行
        #阻值了多线程的并发执行，包含锁的代码只能以单线程执行，故效率降低明显
        '''
        lock.acquire()
        try:
            num += a
            num -= a
        finally:
        #一定要释放锁
            lock.release()
        '''
        #与上述代码功能相同，with lock可以自动上锁和解锁
        with lock:
            num += a
            num -= a
if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('num = ',num)