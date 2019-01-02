'''

multiprocessing 库       Linux中可以使用fock
跨平台模块，提供了一个Process类来代表一个进程对象

'''

from multiprocessing import Process
from time import sleep
import os

def run(str1,str2):
    print('启动子进程')
    sleep(3)
    print('结束子进程')

if __name__ == '__main__':
    print('主（父）进程启动')

    p = Process(target = run, args=('yyn','a1'))

    p.start()

    #父进程的结束不会影响子进程，让父进程等待子进程结束后再执行
    p.join()
    print('父进程结束')