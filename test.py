# -*- coding:utf-8 -*-
import xlrd
import MySQLdb
import random
import time

normal_multiple_chart = open('normal_multiple_chat.txt', 'r')
content = normal_multiple_chart.readline()
while content != '':
    print content
    content = normal_multiple_chart.readline()