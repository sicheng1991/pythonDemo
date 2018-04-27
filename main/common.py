'常用模块'

__author__ = 'yangzteL'

######################## datetime ########################
# datetime
from datetime import datetime

# 当前时间
print(datetime.now())
# 指定时间
print(datetime(2018, 4, 27, 10, 30, 30))

# datetime变时间戳
print(datetime.now().timestamp())

# 时间戳变datetime
tt = 1234567824
print(datetime.fromtimestamp(tt))

# str 转datetime
print(datetime.strptime('2018-4-27 11:30:00', '%Y-%m-%d %H:%M:%S'))

# datetime 转str
now = datetime.now();
print(now.strftime('%a, %b %d %H:%M'))

from datetime import timedelta

# [字符符号]:https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# datetime时间转换
print(now - timedelta(hours=1) + timedelta(days=2))

######################## collections ########################

# namedtuple
from collections import namedtuple

point = namedtuple('position', ['x', 'y'])
print(point(1, 2))

###################### Pillow ######################
from PIL import Image, ImageFilter, ImageFont, ImageDraw

im = Image.open('file/1.jpg')
# 图片大小
w, h = im.size
print(w, h)
# 缩放到50%:
im.thumbnail((w // 2, h // 2))
w, h = im.size
print('Resize image to: %sx%s' % (w, h))

# 把缩放后的图像用jpeg格式保存:
# im.save('file/small.jpg', 'jpeg')

# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
# im2.save('file/blur.jpg', 'jpeg')

## PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
import random


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('file/arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('file/code.jpg', 'jpeg')

###################### request 网络访问######################

import requests

## 请求网页
r = requests.get('https://www.baidu.com', params={'wd': 'yangzteL'})
# 相应码
print(r.status_code)
# print(r.url)
# print(r.encoding)
# 正文
# print(r.text)
# print(r.content)

# get接口(加入：headers)
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
#                  ,headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.json())

# post接口
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.content)

################### chardet 编码检查  #########################
import chardet
print(chardet.detect(b'Hello, world!'))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

