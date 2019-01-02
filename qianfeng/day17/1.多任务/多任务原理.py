'''
现代操作系统均支持多任务

多任务：操作系统可以同时运行多个任务

单核CPU原理：操作系统轮流让各个任务交替执行

多核原理：真正的并行执行多任务只能在多核CPU实现，但当任务量多于cpu核心数量，所以操作系统会自动将任务轮流调度

并发： 看上去一起执行，任务数 > 核心数
并行： 真一起执行，任务数 <= 核心数

实现方式：
1、多进程模式
2、多线程模式
3、协程模式
4、多进程 + 多线程

'''