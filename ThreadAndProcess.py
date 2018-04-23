'线程和进程'
import os

__author__ = 'yangzteL'


def startProcess():
    # linux ，mac系统
    # print('主进程ID：{}'.format(os.getpgid()))

    # window系统
    from multiprocessing import Process
    if __name__ == '__main__':
        print('Parent process %s.' % os.getpid())
        p = Process(target=run_proc, args=('test',))
        print('Child process will start.')
        p.start()
        p.join()
        print('Child process end.')


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

startProcess()
