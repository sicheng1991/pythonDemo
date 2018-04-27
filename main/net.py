'网络编程'
import os

__author__ = 'yanzteL'



##################################  客服端 ############################################
# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

# b''是一个空字节,join是连接列表的函数,buffer是一个字节串的列表
data = b''.join(buffer)
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:


path2 = os.path.abspath('..')#回到上级目录
with open(path2 + '/file/sina.html', 'wb') as f:
    f.write(html)

#################### 服务端 #################################

