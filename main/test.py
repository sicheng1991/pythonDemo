from _pytest import logging

# 是否包含

def openFile(path):
    # 注意补IO异常处理
    try:
        f = open(path, 'r', encoding='utf-8')
        a = 0
        for line in f:
            if line.find('response: 400') != -1 and line.find('"platform":"2"') != -1:
                a = a + 1
                print(line)
        print('总数：{}'.format(a))
    except IOError as e:
        logging.exception(e)
    finally:
        if f:
            f.close()

openFile('D:/MyApp/python/file/access_29.log')
