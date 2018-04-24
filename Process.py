'进程'
import os

__author__ = 'yangzteL'


# 开启子进程
def startProcess():
    # linux ，mac系统
    # print('主进程ID：{}'.format(os.getpgid()))

    # window系统
    from multiprocessing import Process
    if __name__ == '__main__':
        print('Parent process %s.' % os.getpid())
        p = Process(target=new_process, args=('test',))
        print('Child process will start.')
        p.start()
        p.join()
        print('Child process end.')


def new_process(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# startProcess()

# 线程池
from multiprocessing import Pool
# import os, time, random


# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.3f seconds.' % (name, (end - start)))
#

# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     # 线程池最大为4
#
#     p = Pool(4)
#     # 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到类似效果。
#     # p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
#     p.close()
#     p.join()
#     print('All subprocesses done.')


# 子进程
def child_process():
    import subprocess
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    # print(output.decode('utf-8'))
    print(output.decode('gbk'))
    print('Exit code:', p.returncode)
    #上面的代码相当于在命令行执行命令nslookup，然后手动输入：
    #set q=mx
    #python.org
    #exit
# child_process()


# 进程间通信
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()