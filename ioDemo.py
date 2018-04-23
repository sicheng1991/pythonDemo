'IO操作'
import os
from io import StringIO, BytesIO

from pip.utils import logging

__author__ = 'yangzteL'


class IOHandler(object):
    def openFile(self, path):
        # 注意补IO异常处理
        try:
            f = open(path, 'r')
            print(f.read())
        except IOError as e:
            logging.exception(e)
        finally:
            if f:
                f.close()

    def openFile1(self, path):
        with open(path, 'r') as f:
            print(f.read())

    def writefile(self, path):
        with open(path, 'w') as f:
            print(f.write('写点什么呢'))
    def getString(self):
        f = StringIO()
        f.write('往StringIO里面写')
        f.write('写些什么呢')
        # getvalue()：获取写入的数据
        print(f.getvalue())

    # 二进制的
    def getBytes(self):
        f = BytesIO()
        f.write('中文'.encode('utf-8'))
        f.write('往StringIO里面写'.encode('utf-8'))
        f.write('写些什么呢'.encode('utf-8'))
        # getvalue()：获取写入的数据
        print(f.getvalue())

    # 操作系统
    def getOs(self):
        # nt 为window系统，posix为linux，unix，macos系统
        print(os.name)
        print(os.environ)
        # 系统详细细信息，winddow 系统没有这个api
        # print(os.uname())


    # 环境变量
    def getOs(self):
        print(os.environ)
        #具体哪个环境变量
        print(os.environ.get('path'))



    def handlePath(self):

        #获取相对路径
        print(os.path.abspath('.'))

        # 路径组合
        # os.path.join('C:/Users/Administrator/Desktop/app', 'testdir')

        # 然后创建一个目录:
        # os.mkdir('C:/Users/Administrator/Desktop/app/test')
        # 删掉一个目录:
        # os.rmdir('C:/Users/Administrator/Desktop/app')
        # 创建文件

        # 对文件重命名:
        # os.rename('C:/Users/Administrator/Desktop/app/json1111.txt', 'C:/Users/Administrator/Desktop/app/json.txt')
        # 删掉文件:
        # os.remove('test.py')

        # #拆分路径和文件名
        # path,name = os.path.split('C:/Users/Administrator/Desktop/app/json.txt')
        # print(path,name)
        # #获取文件后缀
        # type1 = os.path.splitext('C:/Users/Administrator/Desktop/app/json.txt')
        # print(type1)

    def serializeHandel(self):
        from student import student
        import json
        student1 = student('yangzteL',89)
        str = json.dumps(student1,default = student.student2dict)
        print(str)
        print(json.loads(str, object_hook=student.dict2student))


