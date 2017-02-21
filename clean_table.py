# -*- coding:utf-8 -*-
import xlrd
import MySQLdb
import random
import time
import datetime



conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", db="taxi", port=3306, charset="utf8")
cursor = conn.cursor()

cursor.execute("DELETE FROM weixinchatrecord")
cursor.execute("DELETE FROM group2person")
cursor.execute("DELETE FROM weixin_group")
cursor.execute("DELETE FROM weixin_friends")
cursor.execute("DELETE FROM weixinpersoninfo")

conn.commit()

cursor.close()
conn.close()