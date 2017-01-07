# -*- coding:utf-8 -*-
import xlrd
import MySQLdb
import random

group_words = ["幸福", "之家", "美满", "平安", "安康", "小屋", "一家人", "快乐", "开心", "乐园", "相伴", "家人", "美好",
               "之树", "生活", "哈哈哈", "蛇皮", "富足", "愉悦", "海洋", "森林", "家园", "之门", "光明"]

def create_datetime():
    time = str(random.randint(2010, 2016)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)) + ' ' + \
           str(random.randint(0, 23)) + ':' + str(random.randint(0, 59)) + ':' + str(random.randint(0, 59))
    return time

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", db="taxi", port=3306, charset="utf8")
cursor = conn.cursor()

#特定微信群
cursor.execute("INSERT INTO weixin_group VALUES(NULL,'的士联盟',%s)", (create_datetime(),))
for i in xrange(0, 789):
    cursor.execute(
        "INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))",('的士联盟',))
    conn.commit()

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'贵阳出租车',%s)", (create_datetime(),))
for i in xrange(0, 300):
    cursor.execute(
        "INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))",('贵阳出租车',))
    conn.commit()

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'涨工资啊啊啊',%s)", (create_datetime(),))
for i in xrange(0, 38):
    cursor.execute(
        "INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))",('涨工资啊啊啊',))
    conn.commit()

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'钱钱钱钱钱',%s)", (create_datetime(),))
for i in xrange(0, 26):
    cursor.execute(
        "INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))",('钱钱钱钱钱',))
    conn.commit()

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'黑车真不要脸',%s)", (create_datetime(),))
for i in xrange(0, 120):
    cursor.execute(
        "INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))",('黑车真不要脸',))
    conn.commit()

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'没钱过年吃蛇?',%s)", (create_datetime(),))
for i in xrange(0, 17):
    cursor.execute(
        "INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))",('没钱过年吃蛇?',))
    conn.commit()

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'寻找正义',%s)", (create_datetime(),))
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '寻找正义'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '苟朝华'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '寻找正义'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '李卒'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '寻找正义'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '赵余波'))")
for i in xrange(0, 33):
    cursor.execute(
        "INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))",('寻找正义',))
    conn.commit()

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'好基友一辈子',%s)", (create_datetime(),))
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '好基友一辈子'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '彭高伟'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '好基友一辈子'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '刘洋'))")
for i in xrange(0, 21):
    cursor.execute(
        "INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))",('好基友一辈子',))
    conn.commit()

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'秘密行动',%s)", (create_datetime(),))
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '秘密行动'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '王友奎'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '秘密行动'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '封华'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '秘密行动'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '魏宏'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '秘密行动'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '卞章永'))")
for i in xrange(0, 5):
    cursor.execute(
        "INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))",('秘密行动',))
    conn.commit()

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'为了工资',%s)", (create_datetime(),))
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '为了工资'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '刘彬'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '为了工资'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '杜国孝'))")

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'统一战线',%s)", (create_datetime(),))
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '统一战线'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '陈克刚'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '统一战线'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '徐战国'))")
for i in xrange(0, 71):
    cursor.execute(
        "INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))",('统一战线',))
    conn.commit()

cursor.execute("INSERT INTO weixin_group VALUES(NULL,'超级无敌银建公司哦',%s)", (create_datetime(),))
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '超级无敌银建公司哦'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '王友平'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '超级无敌银建公司哦'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '封华'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '超级无敌银建公司哦'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '卞章勇'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '超级无敌银建公司哦'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '魏宏'))")
cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = '超级无敌银建公司哦'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '彭高伦'))")
conn.commit()

for i in xrange(0, 40):
    datetime = create_datetime()
    group_name = str(group_words[random.randint(0, len(group_words)-1)]) + str(group_words[random.randint(0, len(group_words)-1)])
    cursor.execute("INSERT INTO weixin_group VALUES(NULL, %s, %s)", (group_name, datetime))
    for j in xrange(3, 7):
        cursor.execute("INSERT INTO group2person VALUES(NULL, (SELECT id FROM weixin_group WHERE groupName = %s ORDER BY  RAND() LIMIT 1),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1))", (group_name,))
    conn.commit()

cursor.close()
conn.close()