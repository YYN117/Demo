'''

multiprocessing 库       Linux中可以使用fock
跨平台模块，提供了一个Process类来代表一个进程对象

'''

from multiprocessing import Process
from time import sleep
import os
#子进程需要执行的代码
def run(str):
    while True:
        # os.getpid()获取当前进程id号
        print('big penis in %s---%s'%(str, os.getpid()))
        sleep(1.2)

if __name__ == '__main__':
    print('主（父）进程启动----%s'%(os.getpid()))

    #创建一个子进程
    # target说 明进程执行的任务
    p = Process(target = run, args=('yyn',))
    #启动进程
    p.start()

    while True:
        print('big dick')
        sleep(1)
