'正则表达式'
__author__ = 'yangzteL'

# 常用正则
import re
test = '010-12345'
matcher = r'^\d{3}\-\d{3,8}$'
if re.match(matcher, test):
    print('ok')
else:
    print('failed')


# 正则切分
test = 'a b   c'
print(test.split(' '))
print(re.split(r'\s+',test))

# 分组 表达式用()来进行分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 贪婪匹配   正则默认为贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())

# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：

print(re.match(r'^(\d+?)(0*)$', '102300').groups())


# 预编译:便以一次后面可以直接用，多次匹配时可以提高效率
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

