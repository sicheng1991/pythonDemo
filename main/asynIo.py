'异步io'

__author__ = 'yangzteL'


# 协程

# 首先调用c.send(None)启动生成器；
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
# produce拿到consumer处理的结果，继续生产下一条消息；
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return 20
        print('[CONSUMER] Consuming %s...' % n)
        r = '{}  OK'.format(n)


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


# c = consumer()
# produce(c)



#asyncio 异步库

import asyncio
# @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
# hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()
# ，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
# 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# 用新语法重新编写如下：
# async def hello():
#     print("Hello world!")
#     r = await asyncio.sleep(1)
#     print("Hello again!")

# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# # 两个task
# import threading
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# import asyncio
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# # asyncIO
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
# # 用新语法重新编写如下：
# async def hello():
#     print("Hello world!")
#     r = await asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()


import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()