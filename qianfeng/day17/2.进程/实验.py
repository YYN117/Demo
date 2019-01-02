from multiprocessing import Process
import time,os,random
def ping():
    print('启动子进程')
    for i in range(100,1000):
        j = pow(i,2)
        a = list(str(j))
        b = int(''.join(a[-3:]))
        if b == i:
            print('有如下数：{}---{}'.format(i,os.getppid()))
    time.sleep(2)
    print('子进程结束')

if __name__ == '__main__':
    print('父进程启动')

    p = Process(target=ping)

    p.start()

    p.join()
    print('父进程结束')
