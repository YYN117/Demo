from multiprocessing import Process,Queue
import os,time
def write(q):
    print('启动写子进程%s'% (os.getpid()))
    for chr in ['A','B','C','D']:
        q.put(chr)
        time.sleep(1)
    print('结束写子进程%s' % (os.getpid()))

def read(q):
    print('启动读子进程%s' % (os.getppid()))
    while True:
        value = q.get(True)
        print('value = '+ value)
    print('结束读子进程%s' % (os.getppid()))

if __name__ == '__main__':
    #父进程创建队列并传递给子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()

    pw.join()
    # pr进程中是死循环，无法等待其结束，只能强制结束
    pr.terminate()

    print('父进程结束')
