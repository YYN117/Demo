import threading,time

a = 10
def run(num):
    print('子线程(%s)开始'% (threading.current_thread().name))

    time.sleep(2)
    #实现线程功能
    print('打印',num)


    print('子线程(%s)结束'% (threading.current_thread().name))

if __name__ == '__main__':
    #任何进程默认启动一个线程，称为主线程，主线程可以启动新的子线程
    # current_thread():返回当前线程的实例
    print('主线程(%s)启动'% (threading.current_thread().name))

    #创建子线程
    t = threading.Thread(target=run,name='runThread',args=(1,))
    t.start()

    #等待线程结束
    t.join()

    print('主线程(%s)结束' % (threading.current_thread().name))