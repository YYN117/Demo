from multiprocessing import Process
from time import sleep

num = 100

def run():
    print('子进程开始')
    global num  # 效果同 num = 100
    num += 1
    print('子进程结束')

if __name__ == '__main__':
    print('父进程开始')

    #是run，不是run()
    p = Process(target=run)
    p.start()
    p.join()

    #在子进程中修改全局变量对父进程中的全局变量无影响
    #在创建子进程时对全局变量做了备份，父进程中与子进程的num是不同的变量
    print('父进程结束--%d'%num)