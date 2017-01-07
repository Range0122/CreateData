# -*- coding:utf-8 -*-
import xlrd
import MySQLdb
import random

data = xlrd.open_workbook("person.xlsx")
table = data.sheets()[0]

nrows = table.nrows
ncols = table.ncols

remark_name = ["S、﹏ 加名字","♫ 。 加名字","Dear 加名字","冏 rz❤ 加名字","Love, 铭记","m1ng、","丫头","。某某。乖",
               "◆╮﹏﹏xx","◇╮﹏﹏xx","暖瞳﹎丶xxx","回眸﹎丶xx","路过﹎丶xxx","幻象﹎丶xxx","疯子﹎丶xxx","傻子﹎丶xxx",
               "　　◆╮﹏﹏xx","　　◇╮﹏﹏xx","　　●﹏过电﹏●","　　●﹏佳人﹏●","　　●﹏美眉﹏●","●﹏帅哥﹏●",
               "　　●﹏过客﹏●","　　暖瞳﹎丶xxx","　　回眸﹎丶xx","　　路过﹎丶xxx","　　幻象﹎丶xxx","疯子﹎丶xxx",
               "　　傻子﹎丶xxx","— ≮誓言≯ —","— ≮谎言≯ —","— ≮思恋≯ —","— ≮等待≯ —","— ≮回忆≯ —",
               "— ≮当初≯ —","“”╬══→ 恏伖","╬══→ 姐妹","╬══→ 儭亾","╬══→ 哃敩","╬══→ 娸彵",
               "　┈━═☆佷熟哋","　┈━═☆儭嬡哋","　┈━═☆尊敬哋","　┈━═☆陌泩哋","　┈━═☆認識哋",
               "▂▃▅▆ 玩哋恏哋","▂▃▅▆ 芣忲熟哋","▂▃▅▆ 哃過敩哋","▂▃▅▆ 莪傢里哋","▂▃▅▆ 朂儭嬡哋",
               "㊣★☆——死黨","㊣★☆——兄弟","㊣★☆——姐妹","㊣★☆——蛧伖","(☆＿☆)  羙囡","(☆＿☆)  帅哥",
               "(☆＿☆)  傢亾","(☆＿☆)  陌泩","┣▇▇═—瑺聅係","┣▇▇═—芣忲熟","┣▇▇═—特莂哋","┣▇▇═—儭凊圎",
               "*@_@* 佷崇拜哋","*@_@* 珓崇拜哋","*@_@* 芣崇拜哋","〝喜欢〞","〝忘记〞","〝离开〞",
               "〝快乐〞","〝痛苦〞","〝阴霾〞","〝美丽〞","〝心碎〞","〝分手〞","〝悲伤〞","    ———————",
               "    ﹎ˋ晓","    ﹎ˋ强","    ﹎ˋ伟","    ﹎ˋ军","    ﹎ˋ丰","    ﹎ˋ杰","    ﹎ˋ兵","    ﹎ˋ豪",
               "    ﹎ˋ令","    ﹎ˋ进","    ﹎ˋ宇","メ粉色゛","メ粉色゛","メ红色゛","メ蓝色゛","メ绿色゛","メ黄色゛",
               "メ棕色゛","メ橙色゛","メ粉色゛","メ黑色゛","僅剩的余溫","在俄的世界，俄就是神丶","安安安安、心","敢问全世界",
               "轻轻歌唱","以你为荣","こ雲淡風輕ζ","冷安笑看世间繁华、","虛僞的人類","从未后悔过-","想鲨人","平凡之路@",
               "待糘荖漢","冷笑一直徘徊脸蛋上","MY ANSWER-我的答案","你的泪水‖太多","玩命丕玩鈊","暗杀γ","小三就是外星狗",
               "全球变暖人心变冷","放肆才叫青春","ㄝん值得高傲","无姓之人","只喜欢我喜欢的","2ero丶淡","承诺已泛黄","何惧情",
               "拥我家驹!","▼过敏╰︶","专属、我的devil ▓","治愈我！","陪你看日出、说不离╮","性感mmˇ","技术の总奸",
               "岁月不饶人￠","↖娜爷↗","爱坚强","她ゝ那么高傲","相爱到放弃","带着面具向前走","表面幸畐。","滒旳丗堺ㄚòひ囨懂",
               "尼古丁的诱惑\"ゝ","ジ小气的女人","じ或许卜该爱","痛并快乐着。","2014永享WIFI","ゝ 沾花惹草","蘇瑾熙 ǐ","抛来一切。",
               "泡8喝9說10話","逞强坚强在哪里-c","别回头他不爱你i","『忘掉了』你","丿爱你不变心彡","絕口不談、与你有关",
               "咬破嘴唇也不许哭。","透露着小温馨⊙","迅雷也下載不到幸福","给我根牙签我能翘起地球","硪的偶像是女汉纸i","单身真好i",
               "一瞬间、幸福","逗比范儿i","妈，他摸我的屁股","小小小、笨蛋"]

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", db="taxi", port=3306, charset="utf8")
cursor = conn.cursor()

special_people = [
    "赵余波", "王友奎", "万淳洁", "苟朝华", "李卒", "王友平", "封华", "卞章勇", "魏宏", "彭高伦", "刘洋",
    "刘彬", "杜国孝", "陈克刚", "徐战国", "陈勇", "孙继亚", "胡正军", "张宝", "卞章永", "彭高伟"
]
'''
#创建已确定的友人关系
cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '苟朝华'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '李卒'),'李卒','苟朝华')")
cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '苟朝华'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '赵余波'),'赵余波','苟朝华')")
cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '李卒'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '赵余波'),'赵余波','李卒')")

cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '王友奎'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '封华'),'封华','王友奎')")
cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '王友奎'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '魏宏'),'魏宏','王友奎')")
cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '王友奎'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '卞章永'),'卞章永','王友奎')")
cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '魏宏'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '封华'),'封华','魏宏')")
cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '卞章永'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '封华'),'封华','卞章永')")
cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '卞章永'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '魏宏'),'魏宏','卞章永')")

cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '彭高伟'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '刘洋'),'刘洋','彭高伟')")

cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '杜国孝'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '刘彬'),'刘彬','杜国孝')")

cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = '徐战国'),(SELECT accountID FROM weixinpersoninfo WHERE nickName = '陈克刚'),'陈克刚','徐战国')")
'''

#构造随机的友人关系

for i in range(0, len(special_people)):
    for j in range(0, random.randint(30, 70)):
        try:
            cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo WHERE nickName = %s),(SELECT accountID FROM weixinpersoninfo  WHERE nickName != %s ORDER BY  RAND() LIMIT 1),%s,%s)",(str(special_people[i]), str(special_people[i]), remark_name[random.randint(0, len(remark_name)-1)], str(special_people[i])))
            conn.commit()
        except:
            pass

#在这里选择需要生成的朋友关系链数量
for i in xrange(0, 2000):
    try:
        cursor.execute("INSERT INTO weixin_friends VALUES(NULL,(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1),(SELECT accountID FROM weixinpersoninfo ORDER BY  RAND() LIMIT 1), %s, %s)", (remark_name[random.randint(0, len(remark_name)-1)], remark_name[random.randint(0, len(remark_name)-1)]))
        conn.commit()
    except:
        pass

cursor.close()
conn.close()