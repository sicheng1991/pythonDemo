# say something
# print('please input name:')
# # name = input()
# # names = ['long','wen','jiang']
# # names.pop()
# # print('欢迎回来 {}'.format(name))
# # print(names)

# 判断
# s = input('age: ')
# age = int(s)
# if age > 18:
#     print('man ')
# elif age > 12:
#     print('young')
# else:
#     print('children')

# 循环
# sum = 0
# for x in [1,2,3,4,5,6,7,8,9,]:
#     sum += x;
#     print(x)
# print(sum)
# list1 = list(range(50))
# for x in list1:
#     print(x)

# # dict 字典
# d = {'sicheng': 18, 'chimu': 21, 'longwenjiang': 26}
# print('age:{}'.format(d['chimu']))

# set
# s = set([1, 2, 3,3])
# print(s)

# 函数
# print(abs(-3.6))
#
# print(str('12.3'))
# print(str(int(12.3)))

# 函数，带入参检测
# def getArea(r):
#     if not isinstance(r, (int, float)):
#         raise TypeError('type error')
#     return 3.14 * r * r
# print('area：{}'.format(getArea(20)))

# 空方法
# def getHeigh(x):
#     pass
# print('area：{}'.format(getHeigh(20)))

# 默认参数
# def getXY(x,y = 100):
#     return x, y
# x, y= getXY(60)
# print(x, y)
# x, y= getXY(60,200)
# print(x, y)

# 可变参数
# def sum(*num):
#     ss = 0
#     for x in num:
#         ss += x
#     return ss
# print(str.format("sum = {}",sum(1,2,3)))
# print(str.format("sum = {}",sum(*[1,2,3])))

# # 切片
# list = ['java', 'web', 'php', 'python', 'c']
# print(list[1:3])
# print(list[-3:-1])
# for index,x in enumerate(list):
#     print(index,x)

# # 列表生成
# print(list(range(2, 30)))
# print([x * x for x in range(1, 10)])

# # x 操作
# print([x * x for x in range(2, 10)])


# 过滤
# print([x * x for x in range(2, 10) if x % 2 == 0])
# filter()
# def filt(n):
#     return n % 2 == 1
#
# list = list(filter(filt, list(range(2, 10))))
# print(list)
#
#
# # 打印1000以内的素数:
# # 带yield的函数是生成器
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# def _not_divisible(n):
#     return lambda x: x % n > 0
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
# # 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# # sorted 排序
#
# print(sorted([5, 4, 3, 6, 9, 8, 7]))
# # 按绝对值排序
# print(sorted([5, 4, -3, -6, 9, 8, 7], key=abs))
# # 按绝对值排序,反序
# print(sorted([5, 4, -3, -6, 9, 8, 7], key=abs,reverse=True))

# 函数返回

# 函数作为返回值
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f())
# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
#  另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行

# 匿名函数 lambda
# lambda x: x * x
# list = list(map(lambda x: x * x, list(range(1, 10))))
# print(list)

# 装饰器：代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# # 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
# @log
# def now():
#     print('2015-3-25')
#
# print(now())

# 偏函数 functools
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单


# import hello
#
# hello.test()

# 面向对象编程
# #导入方法一
# import student
# person = student.student('longwenjiang',100)
# person.printStudent()
#
# #导入方法二
# from student import *
# person = student('longwenjiang',100)
# person.printStudent()

# print(type('fad'))
# print(isinstance(type('aaa'),type( 'aadddd')))
# print(dir('add'))

# 动态绑定方法
# class student(object):
#     __slots__ = ('name', 'age','set_age','set_score','score')
#     pass
#
#
# s = student()
#
#
# def set_age(self, age):
#     self.age = age
#
# # 给类绑定方法
# def set_score(self, score):
#     self.score = score
#
#
# from types import MethodType
#
# student.set_score = set_score # 给类绑定方法
# # s.setage = MethodType(set_age, s)  # 给对象绑定方法
# s = student()
# s.set_age = MethodType(set_age,student) # 或给对象绑定方法
#
# s.set_age(26)
# s.set_score(100)
# print(s.age)

# @propert  约束方法
# class student(object):
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s = student()
# s.score = 20
# print(s.score)


# 多继承
# class person (object):
#     pass
#
# class man(person):
#     pass
#
# class olaMan(person,man):
#     pass

# class person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __len__(self):
#         return 50
#     def __str__(self):
#         return 'name is :% s ' %(self.name)
# print(person('yangzteL'))
# print('len：%s' % len(person('yangzteL')))

# 枚举
# from enum import Enum
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


## 单元测试，异常处理
# def calc(num, bnum):
#     if bnum == 0:
#         raise ZeroDivisionError('can not be 00000000000')
#     try:
#         return num / bnum
#     except ZeroDivisionError as e:
#         print('can not be 0')
#         logging.exception(e)
#     finally:
#         print('finall  run')
# print(calc(2, 1))


