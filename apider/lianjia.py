'链家'
import requests
# pip 安装要安装：BeautifulSoup4
from bs4 import BeautifulSoup
import pymysql.cursors


def get_house_info(url):
    soup = BeautifulSoup(requests.get(url).text, "lxml")
    price = soup.find("span", class_="total").text
    house_info = soup.find_all("p")
    area = house_info[0].text[3:].strip()
    house_type = house_info[1].text[5:].strip()
    floor = house_info[2].text[3:].strip()
    house_name = house_info[5].text[3:].replace("\n", "").replace(" ", "")
    position = house_info[6].text[3:].strip().replace("\n", "").replace(" ", "")
    phone = soup.find("div", class_="phone").text.strip().replace("\n", "").replace(" ", "")

    info = {
        '链接': url,
        '价格': price,
        '大小': area,
        '户型': house_type,
        '楼层': floor,
        '小区': house_name,
        '位置': position,
        '电话': phone,
    }

    return info


def get_db():
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='user',
        charset='utf8'
    )
    # 获取游标
    return connect


def insert(connect, info):
    try:
        values = "'{}'," * 7 + "'{}'"
        sql_value = values.format(info["链接"], info["价格"], info["大小"], info["户型"], info["楼层"], info["小区"], info["位置"],
                                  info["电话"])
        sql = "insert into lianjia(url,money,area,houseType,floor,houseName,position,phone) values ({})".format(
            sql_value)
        cursor = connect.cursor()
        # print(sql)
        cursor.execute(sql)
        connect.commit()
    except Exception as e:
        print('插入数据处理失败', e)


def start_spider(url, index):
    try:
        print(url)
        respon = requests.get(url)
        soup = BeautifulSoup(respon.text, "lxml")
        arr = soup.find_all("div", class_="pic-panel")
        link = {div.a.get('href') for div in arr}
        for x in link:
            info = get_house_info(x)
            # print(info)
            insert(get_db(), info)
    except Exception as e:
        print('url不存在', e)
    if index < 100:
        index += 1
        start_spider("https://cd.lianjia.com/zufang/pg{}/".format(index), index)


main_url = 'https://cd.lianjia.com/zufang'
start_spider(main_url, 1)
