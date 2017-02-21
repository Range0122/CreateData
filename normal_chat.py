# -*- coding:utf-8 -*-
import xlrd
import MySQLdb
import random
import time
import datetime


def create_datetime():
    time = str(random.randint(2010, 2016)) + '-' + str('%.2d' % random.randint(1, 12)) + '-' + str('%.2d' % random.randint(1, 28)) + ' ' + \
           str('%.2d' % random.randint(0, 23)) + ':' + str('%.2d' % random.randint(0, 59)) + ':' + str('%.2d' % random.randint(0, 59))
    return time


def time_plus(t):
    d = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    time_sec_float = time.mktime(d.timetuple())
    time_sec_float += random.randint(30, 200)
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_sec_float))
    return str_time

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", db="taxi", port=3306, charset="utf8")
cursor = conn.cursor()

normal_single_chart = open('normal_single_chat.txt', 'r')
content = normal_single_chart.readline()
while content != '':
    cursor.execute("SELECT friendAId FROM weixin_friends ORDER BY RAND() LIMIT 1")
    send_id = cursor.fetchone()[0]
    cursor.execute("SELECT friendBId FROM weixin_friends WHERE friendAid = %s ORDER BY RAND() LIMIT 1 ", (send_id,))
    receive_id = cursor.fetchone()[0]
    send_time = create_datetime()
    for i in range(random.randint(2, 30)):
        cursor.execute("INSERT INTO weixinchatrecord VALUE(NULL, %s, %s, %s, %s)",
                       (str(send_id), str(receive_id), str(content), str(send_time)))
        conn.commit()
        content = normal_single_chart.readline()
        if content == '':
            break
        send_time = time_plus(send_time)


normal_multiple_chart = open('normal_multiple_chat.txt', 'r')
send_time = create_datetime()
for i in range(0, 100):
    content = normal_multiple_chart.readline()
    cursor.execute("SELECT id FROM weixin_group WHERE groupName = '的士联盟'")
    group_id = cursor.fetchone()[0]
    cursor.execute("SELECT personId FROM group2person WHERE groupId = %s ORDER BY RAND() LIMIT 1", (group_id,))
    send_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO weixingroupchatrecord VALUES(NULL,%s,%s,%s,%s)", (str(group_id), str(send_id), str(send_time), str(content)))
    conn.commit()
    send_time = time_plus(send_time)
    if i%20 == 0 :
        send_time = create_datetime()

for i in range(0, 70):
    content = normal_multiple_chart.readline()
    cursor.execute("SELECT id FROM weixin_group WHERE groupName = '贵阳出租车'")
    group_id = cursor.fetchone()[0]
    cursor.execute("SELECT personId FROM group2person WHERE groupId = %s ORDER BY RAND() LIMIT 1", (group_id,))
    send_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO weixingroupchatrecord VALUES(NULL,%s,%s,%s,%s)", (str(group_id), str(send_id), str(send_time), str(content)))
    conn.commit()
    send_time = time_plus(send_time)
    if i%20 == 0 :
        send_time = create_datetime()

for i in range(0, 40):
    content = normal_multiple_chart.readline()
    cursor.execute("SELECT id FROM weixin_group WHERE groupName = '涨工资啊啊啊'")
    group_id = cursor.fetchone()[0]
    cursor.execute("SELECT personId FROM group2person WHERE groupId = %s ORDER BY RAND() LIMIT 1", (group_id,))
    send_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO weixingroupchatrecord VALUES(NULL,%s,%s,%s,%s)", (str(group_id), str(send_id), str(send_time), str(content)))
    conn.commit()
    send_time = time_plus(send_time)
    if i%12 == 0 :
        send_time = create_datetime()

for i in range(0, 53):
    content = normal_multiple_chart.readline()
    cursor.execute("SELECT id FROM weixin_group WHERE groupName = '没钱过年吃蛇?'")
    group_id = cursor.fetchone()[0]
    cursor.execute("SELECT personId FROM group2person WHERE groupId = %s ORDER BY RAND() LIMIT 1", (group_id,))
    send_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO weixingroupchatrecord VALUES(NULL,%s,%s,%s,%s)", (str(group_id), str(send_id), str(send_time), str(content)))
    conn.commit()
    send_time = time_plus(send_time)
    if i%12 == 0 :
        send_time = create_datetime()

normal_family_chart = open('normal_family_chat.txt', 'r')
content = normal_family_chart.readline()
cursor.execute("SELECT id FROM weixin_group WHERE groupName = '超级无敌银建公司哦'")
group_id = cursor.fetchone()[0]
send_time = create_datetime()

while content != '':
    group_id += 1
    for i in range(0, random.randint(8, 20)):
        cursor.execute("SELECT personId FROM group2person WHERE groupId = %s ORDER BY RAND() LIMIT 1", (group_id,))
        send_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO weixingroupchatrecord VALUES(NULL,%s,%s,%s,%s)", (str(group_id), str(send_id), str(send_time), str(content)))
        conn.commit()
        send_time = time_plus(send_time)
        content = normal_family_chart.readline()
        if content == '':
            break

conn.commit()
cursor.close()
conn.close()
