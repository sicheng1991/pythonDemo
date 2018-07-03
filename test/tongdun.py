import base64
import json
import cx_Oracle
import xlrd

from xlrd import open_workbook
from xlutils.copy import copy

# Oracle数据库，Excel处理
def get_db():
    # 获取游标
    # return cx_Oracle.connect('zhfq/kbXVExAY@192.168.7.202:1521/putest')
    return cx_Oracle.connect('ZHHAPPUSER/I4Zu1SrY@192.168.200.61:50001/phzhapp')


def testOracle():
    # python安装的是多少位oracle客户端(instantclient_11_2)就是多少位
    # conn = cx_Oracle.connect('用户名/密码@数据库ip:端口号/数据库名（SID）')

    conn = cx_Oracle.connect('zhfq/kbXVExAY@192.168.7.202:1521/putest')
    curs = conn.cursor()
    rr = curs.execute('select * from ZHH_APPLY_LOAN')
    row = curs.fetchone()
    print(row[2])
    curs.close()
    conn.close()


def get(conn, info):
    try:
        cursor = conn.cursor()
        sql = "select * from ZHH_APPLY_LOAN where APPLY_LOAN_KEY= '{}'".format(info)

        rr = cursor.execute(sql)
        row = cursor.fetchone()

        if row[60]:
            json1 = str(row[60])
        else:
            json1 = str(row[12])
        # print(json1)
        ss = base64.b64decode(json1)
        s1 = str(ss, 'utf-8')
        print(s1)
        data = json.loads(s1)
        if data['os']:
            device = data['os']
        elif data['error_init']:
            device = data['error_init']['device']
        else:
            device = data['os']

            # if data['os']:
            #     device = data['error_init']['device']
            # elif data['error_init']:
            #     device = data['device']
            # else:
            #     device = data['os']

        print(device)
        conn.commit()
        return device
    except Exception as e:
        print('处理失败', e)
        return str(e)


workbook = xlrd.open_workbook('C:/Users/Administrator/Desktop/tondun.xlsx')
sheet_names = workbook.sheet_names()

book = open_workbook(u'C:/Users/Administrator/Desktop/tondun.xlsx')
wbook = copy(book)  # wbook即为xlwt.WorkBook对象

wsheet = wbook.get_sheet(0)  # 通过get_sheet()获取的sheet有write()方法
wsheet.write(0, 8, 'value')

for sheet_name in sheet_names:
    sheet2 = workbook.sheet_by_name(sheet_name)
    conn = get_db()
    cols = sheet2.col_values(0)  # 获取第一列内容
    for index, apply_key in enumerate(cols):
        # print(index, apply_key)
        device = get(conn, apply_key)
        wsheet.write(index, 8, device)

    wbook.save(r'C:/Users/Administrator/Desktop/tondun1.xls')

# start_spider()
