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
               "一瞬间、幸福","逗比范儿i","妈，他摸我的屁股","小小小、笨蛋","明之翼","寂杀哲理","wuliwala666","光瞎有木有",
               "阿飞欧巴嘿","Win丶别泪","云逸Uu独殇","羊蛋的春天","love灬西西","m1004229765","爱De刹那","h1n1了解","9039645",
               "l2557653","孔融让翔","英俊的昊哥","我科我科","上帝不是乔丹","有个人叫炫宇","抽支天下秀","别和往事为难_",
               "baozj500","弡仲景","白大坑","爱篮球的程子","Pursuit鏏轔","nmds99","tany125","TheMonest","fly科比ni很帅",
               "舍你其谁V","bei2小jian","hgdjjjfhkydx","zz粘","变色圆珠笔","扣绿帽_小王子","全能D林林","二郎K真君","高达新人类",
               "不懂别不懂装懂","Derrick_健","风吹过的那刻","841674245","天蝎丿SAY","润岁","李翔宇哟","一贱保平安kd35",
               "翘臀的兔子","我们丶很帅气","妳在乎的蜗","俺的钛合金狗眼","Sell2","micklk","sun171390470","地狱养心",
               "life郑嘉亮","林右杰丶","CSOLNB","永恒灬C","jacklcj123","布莱克北鼻","baby又是你","我快乐的小尾巴",
               "____Luminary","天蓝之翼7","欧欧欧文控_","ROYALBAREE","birdman时代","RKO刘","可以提尔","Ps依然饭太稀",
               "哥德巴赫很兴奋","NICE无敌C罗","一只大金雕","彡岁就嚣张","碧海_James邦","神级逆天7","棱律","我已看到超神了",
               "92年生人","t246437","defend丶杜","飞天团团猪","苹果真不甜","终南山一霸","傲慢的破军","free单曲循环中",
               "很暴力苹果","洞房不败丨丶","强大猛兽","茶沫残语","卡梅隆的绝杀","哥的表情春节不","Hey_厕所诗人",
               "布莱恩特1212","章两万","蛮男入侵","liyao布莱恩特","geyuheng123456","暘光刺痛了心","永远的24","沦呐德",
               "爱五ing","那年夏天165","小铁特","MC花大虫","爱转角后遇到你","猕的的","好多鱼呀555","丶尹天敬","GDP那些年",
               "z谁是谁的谁l","张博994","小孙happy","维克多要当学霸","方丈48333","爱打篮球的胖子","小清新原来是2B",
               "爱韦德永远的FS","坎岩3","Fightback原形","wse1285295868","so终结者","smile_三生烟火","輪回の夢","转身飞翔5",
               "海鲜哥7","h357965706","疯子丶卖菜刀","羽角一冰","xin123mo123","封伈___琐爱_丶","小爪地懒希德","a417265929",
               "别nice","峰少110418","Mexicanos","xjczq88","叶落无痕ˇ","这总能注册了吧","CH9847","笨笨Medivh","ka422",
               "独爱那个妞","ysliangge","劣徒94","刘1997818","神迹￡刹血","xl80713","刺激的飞鹰","五角钱买小冰","2凯12年",
               "生来彷徨的我","Forever噬心","greatThunder35","China丶劫少","甘愿做小备胎","595阿i","苏夕露","sky篮球爱好者",
               "灬唯爱虎牙","荣耀灬小宝Dove","伊张三世","wjz344819733","你去年卖了什么","有些爱不放手","我会狠爱n1╰S",
               "港漫卡","爱kobe爱生活","电音枭子","李时珍095","zhang为wei","老刘是我ok","疯狂的大奥丶","宸血","sacral0802",
               "趁年少偷1点懒","如此如此诠释","Prince_小涷","x378405859","单打王沃克","____黄小杰","二级影帝","飞弟弟弟弟i",
               "Smil洆蓃","Love丨Shady","该昵称正在加载","夜星辰言雨","我是梅仁杏同学","暴罗詹黄啊肚","霸乐魔尊","丶拥挤c",
               "天秤HASLJ","40MJ爆麦迪","偷懒族lovely","玄余","爱泡脚的泡椒","困难飋h","所谓loseR","好man大叔","MELO瓜瓜z",
               "爱你妹妹的咪咪","故园无此声i","单身贵族阿锐","波什送我81","詹皇forever","GTA565","霖_Sama","唯爱仙女姐姐",
               "ok梦魂断","魔兽丶Howard","DLindesy","哥哥帅到爆kk","happyYakamoz","年少薄情凉","nb741kg","a7568677",
               "阳光刺痛眼眸b5","nice冷_色调","冷锋cheeks","施文paul3","魂淡sparta","lakers丶Brant","宇智波神16",
               "爱____韩妞","唯麦1001","土木逐梦者","10142298","给你看我的嘴脸","liang仔在此","你让我吃惊","悲剧的尺子",
               "绝地之狂飙","ScenlyBeach9","个1236373","zm616316310","丿烟花易冷丨","Amoremio","埘间冲淡了回忆","wjzwjz44",
               "胡家男吊丝","denghekaiok","海心沙的杯具","们2算","影流之主斯诺登","你爸洗头用飘油","ydw905385837",
               "ggghhgffhhhggg","内拉MT","矫情的活宝","科此布菜思特24","雨中取印","p595967098","单翼飞机喔","六代目旗木",
               "binglove1991","詹丶皇","即興判斷","M_Flash","上山打钟","偶你寂寞","JJLOVE哦","ISKY361","天枰我没名字",
               "硪是韦密","没事摸牛子","热火王朝jwb","打酱油的龙套哥","噢亲O你好骚","秦寿先森","____城管算个毛","季飞雨沫",
               "胡伯虎点蚊香","鳄鱼赖饼汤","__昵___称____","popopotim","wocaobing","神域玄冰","Music_nerd","天辕丶一切谁缘",
               "0lonely0","会飞的地板流","当天街角流过","我叫尹恒","4717窝科","linkobe88","回忆的路口1","不起眼的小橙子",
               "微笑15字","日月轩辕love","浅唱岁月静好","blackboy丶9","木鱼枫叶","ˇ向…右走","大苏Nsng","炮哥的西决地板",
               "ChristopgerPau","S_curry30_","美利坚大统领","李007700","丿Dream丨狼王","babylietome","高与矮","当年我也很刁",
               "生命的浪费9","尤文奥特曼","何以陌生丶3","sir刀兽","zlqfqllyjj","大一中帝国_","反手加在你身上","你有情么",
               "夜落花开人独醉","阿倫王者","昔若爱爱","YZT1454416540","dai2278","于亮250","yuzerui1992","sunny丶夕颜",
               "宦官苏溪","浓眉哥DAVISJ","775308010","扬手三分","Fgtuoj","位面第三","sunnyGala","Lai楓","三国午夜day",
               "这算个毛1","素手惹尘埃","LAC_空接之城7","哥gemeiri","霆哥的逆袭","青春不朽zj","男友女娴","Spurs29",
               "一直等你143","一袋洗衣粉","力哥002","B仔兽丶","毒丸生产者","灬蚀骨SPACE","Losememoryl2w","科比是BrYAnT",
               "丶巴黎右岸c","秋彡丨落雨","一起站过的军姿","咿你为名的小說","李艾旃","櫻風余小平","小痞子crazy","小弟陪你玩",
               "雪域电竞黑域","Freestyle水母","少年威金斯","fdfdf340","___北風乱","大饼之王","机智的阿黛爾","dashitou520",
               "昔飞啊啊","笑叹word","裘不滚","liurepent","大晖哥丶","花颜丿惜醉酒丶","我不想回忆nice","MKsq","洛基友",
               "吴旭浩天下无敌","梦游苏格拉底","feral2013","致恨我的人","罗斯送我去公牛","蜗壳别退役","科比不未恩特",
               "承诺比纸薄___","baby东北蚂蚱","迪奥托宾贝尔","笑得艹怪","爱小船爱","aoeivu点","单骑救度娘","121chewang",
               "唯一d3嗜血","AiCp3Flash","扒扒皮皮皮皮皮","唐僧洗头爱兴杨","huaiyu0123day","精圆细胞","乐观的骚年丶",
               "求飞车体验服号","眼眸迩的淡雅","Mue丨灬後","丿灬小强丨","赖子客","糖加3shao","fdyqwejkl123","天蝎Mark20",
               "快船赢西决","取什么好啊南","巫妖2号","四季猎手","有时小无敌","用户名12138880","其实我还萌","季后赛后仰男",
               "abc229466160","草狗不要钱","此次此大幅","神のJenova","布莱恩特Mamba","95至尊辉","兴447665168",
               "吾詹六步走天下","朱政南","sunny活力青春","此用户不知去哪","双脚分开就能走","周杰伦爱上科比","你真的吊炸天",
               "神级碉堡机","新迁户刘家","fan7243606","至尊宝强","孙NEXUS","wangwei9988776","G大白菜","雷锋Q358743194",
               "至死不渝像你爸","汲水解渴","846868015","白曼巴LTP","lezheerti","阿萨德传abc","不是吧833","落枫红城",
               "AL茶小荼","凯文_小麦迪","anaw19910404","nowluo6276","元帅10号","liyuqin101964","大帝James","happy雷霆三少",
               "我是你爹你知吗","50号的兰多夫","tsy19930809","知识渊博II","户外球鞋","year独恋KG","丶维斯布魯克",
               "林花谢了春红13","wywsnns","动人心弦great","成都苦力男","幻名sky","邋遢胡子大叔","败惹我我神经",
               "Fallinlovelbj","大傻VS邓全","Al宝宝老婆","聆听记忆11","Leygeyear","桑未落叶沃若1","dlllll6","黄中之子",
               "伊利特工","肩部假动作","克里斯SB","村长100","塌戈","梦幻ooij","Mrchenzb_","ybayl","Solatherine",
               "zhangcx5786","我被你冻结","shi奭","虐她999次方i","不冰墙9","扯淡小鸟","lovemiaoyang","一诚爱莉亚丝",
               "sky快到哥这来","Follow伴我","NAshizhe","扯淡的犊子丶","星睿的存钱盒","skyMrL","S4511352","日轮earth",
               "yaozhaoyu0","popswety","Bestjordan","cx894006976","cnkradsdo","我只做我自己K","尛尛丶家侑愛女","苗条滴德隆",
               "spucklion","右手丶永不停歇","霸气一个钊","b15019633046","Dallas_埃利斯","黑城白森","迷胡迷糊迷糊",
               "爱上木鱼会飞","陈先生在1992","kuang7123","刺辰","ww犹犹豫豫个毛","潮流前线16888","各种宅不解释",
               "锦州龙江小雨","free凉城______","wbshhh","做好自己自好做","不懂不懂大本营","格瑞格波波维奇","fasfdas500",
               "木耳白不白6","超爱唱歌的哑巴","淺誯蓅哖","卖二手苹果一台","康邪武圣","Nick丶y","v唐僧爱飘柔v",
               "85900737","回温过暖","白羊和平使者","萱草是我的一切","葆罗乔治","密码十四个数字","坏小子Answer","XY93earth",
               "869372347","血泪E残殇","875859012","dreamming5","丶起舞弄青影","馃槏777","夏末的柠檬茶","锅盖男神me",
               "抵笼到拐","我都比","1个人的旅途呀","为我独黑丶","吾皇威武free","优秀_青年","流年花火丶丶","zhuzichao20",
               "会疼的","淡之未远","Q饕饕饕饕餮","伤心晓明","茻骉","独龙岛上的宝盒","丶好基友","北京亚市大众","艾吃汉堡",
               "杜兰特一世","她是我的生","freeSeptember","艹744","漆黑的小小刀","钟情你g","小三丶多如狗","她H是他的唯一",
               "库里44","呵呵哈哈哟听","小的不能再小8","洪春渊吉","丿灬传说","313757502","拉里大妈","好人9号","La精彩",
               "历临风","tmac杰jay","nba篮彩推荐师","大虾坦然","谁能代表杜蕾斯","夜路的歌","雨艾叶","最爱发发发88",
               "Mz人生如戏","smile谢文东","旧梦太久","alien1987","vip8888888842","善良的猫王","JamesCT12345","小夕洛落",
               "风雨末了的雨滴","十二之月天","OnePlus丶Kobe","莫莫莫先森","东丶不忈","七弦灭世","sunxumeng26","幻297",
               "经典团队配合","执着丶windy","特玛鞋呢","小祥神","潇洒的兔子072","KG宇一前","梦三丿小布","体育渣XD",
               "演绎灬呐段情","小杯具男","金恵吉","旧巷北辰","执着也只是念","泡妞不是我的错","往事如烟oc","粑粑粑粑粑ysr",
               "Romantic149","噼咻灬","飘雪落花ok","湘情有你更给力","小水电工1","一碗拉面不加面","郁金香在曼联","时尚の火柴",
               "nba职业裁判","东四驱魔玩稀烂","正28经小少年","看破递刀犹大","kwongsh","科比詹皇好基友","hcjfhfh",
               "10电商菜鸟","NBA透析师","溯夜AI","希望的梦旅人","乐观的魏聪聪","梦与善与思与醉","当真爱来临","恐慌的DIROS",
               "1439892812","贰十肆科比","cheng离明","唱过的军歌","烽火无道雪痕","坟冒青烟","孤魂呀","cyrAP","不再说爱0",
               "cch914gdn","微博HJM","转瞬成雨sely","_昨日陌路","Solo你麻痹啊","刘诗诗真女神","郑天宇你个脑残","浮伤着年华",
               "nejer96","Sakura最好了啦","dinosor丶","饭特o稀","郭不撸","heaven盛夏未央","宫爆尐丁","敖世凌尘","天天太难不",
               "Paul第一PG","舜在心间68","李嗯嗯7","NVIDIA四路泰坦","影枫baby","舛4","少年不戴花乁","sky病态i","nice滴阿强",
               "132664qq","因帅判7年smile","卡尔康斯","弗常","2004jzt9","呦呦不知道","德克士计算机","少年花事i","仙王临世",
               "ahcfwr","沙弥595","qq724176136","陶栋栋1994","stan阿莫","徐大爷哈尼","泡椒闪耀","借我点快乐好么",
               "3克里斯3保罗3","张大晖c","徐不吹","你也惹不起Man","骑士灬勋章","河西走廊2002","ALlenLAKERS","战丿Iverson",
               "嘉文四世军旗啊","拉拉丁香港台go","小小小治PG","路人sayhello","百年无聊","小盆友818","宇神影月","非洲大苍蝇",
               "霸气雷迪克","NBAONLINE2","开车咯233","博徕顿铝门窗","deardeaded","go三三四四是","Mike轮回","Kyrie二文",
               "帖士强","hxqhzr","基安原","绝望学霸","1195653706","有喻","zhichinuolan","Y木讷人","无聊世界男","wph7860",
               "龙卷疯99","sunny期待轨迹","小磊爱锋123","O圆明圆O","ZB19910411","N0082gzhe","xuesunxue","小狗762","wkjlb",
               "409516003","1314mylovejay","bemyself_ever","mattheney","爱你大美园","KiSS_DT","瑾子倩","Lai小球","6代雷霆",
               "被骗的小处男1","baby大美圆","yagnqingchi35","jops0920","依a然如此","后勤主任辄","mlm_zjus","龍允_圓桃子",
               "穘鸂","735小四","Gardenia程","深夜fly","還念那擁抱","柏860","酒吧的小子","呓语灬℡ゝ","y依然灬","青春不优伤",
               "诸葛亮VS孔明","一个丹华","王灿710","嗨我说哥们儿","阿殇小畏","天枰的石头","张卓657","荆照照","妖红破晨",
               "卖俩酒瓶来上网","明By","lhsdn","彦丶MISS","天气晴朗76","aaronlee_2012","未来就是没来","有酒好好喝","you她无求了",
               "下页VB浩子","半度微凉的岁月","爱葽大声说出来","tlylq201","free_安好","我们一起到老灬","去二七二其二","dashannjmu",
               "被判无妻徒刑u","TheFaker大魔王","Dong景晨","还记得吗v1","圆圆控患者","伪艺青年LH","zhlsh36","点点杰90",
               "觳觫的微笑","DD艾欣ER","DL丶ZY","天真的灬无厘头","诗风铃意","傲慢与偏见6868","触雪NO紫曦","玲静致远520",
               "打雷下雨了love","森cherish","追求凤凰","Xia0蜡笔","YYB罗兰","倚楼笑看红尘","爲愛丶相濡以沫","梦里花零自飘落",
               "のNalidou","梦想再起航","Vampire景J","对你永不言齐","奈文摩尓","2014LZC","昕LOVE糕圆圆","myqawsedrf","天之蓝地之星",
               "橙子的夏沐冬至","小小小孩_neil","百里小気","L丶鹏P","最爱高园园","零度lovefly","sate丶别致","myfaye","任A鹏",
               "_V_醉柳","向日葵子民丶","WY丶是我","刚之协奏曲","深海589","ok吃碗泪流满面","唯我所爱爱唯一","子琪好high","亲亲中路",
               "哪有白富美","纪雅清丶","暗黑_魅影","深海记忆鱿鱼","我请你麻辣锅呗","点点杰杰","小九默默默","麻哥早","E_as_on_",
               "有所爲fu","狗蛋掉渣天","圆圆丿粉丝","widerun","奮鬥锺","放开那小红帽","qq1070765897","巭孬嫑开枪","陌念heaven",
               "zhoujianyu190","非东仙神","gujun4242008","清伤韵曲","诗一样的爱","A1丶冷魂","飞的更高and杜","不羁星光","文盲爱阅读",
               "吾意不可逆","强大猛兽","hyd3227","809628xiaojian","冷岷航的哥","wattfer","StephaWong","嚣张淑女jessie","季陌0",
               "bxliujia521","ii_look","Yi場夢的人生","MISS丶Y小姐","☆蟹大人","_坏耳机","涂鸦小公子","圣愿得一心心","取水赏花",
               "__JiaoPeng灬","哥很行的55","ba8313","吞噬之静","傲气俊少","丶温蕾萨","西贡少年c","擦_石头","范永新_范导","洪福齐天中",
               "草狠赞","夜深梦繁","计划你大爷","wdsilyy","furtureago","诺讠訁","er2601525152","_半城回忆","Melon瓜先森","我的倔强86",
               "辉要低调啦","薇声音","天下群雄逐鹿","彡爱天夏灬","冬天米兰","hrd0000000000","长谷川cgc11","Smile少年0","简简单单anhour",
               "438104097","liutao389","time携手夕阳下","爱克马克爱油","卖两酒瓶来上网","浪荡不羁丶少年","LeeRo57","只为关注圆圆",
               "划过天际乀","唯爱BCC","大爱女神yuan","lin544456748","筱筱潇潇萧萧","下雨旳冬天","smile红尘中","慕丶蓝秋绽放",
               "梦未在深巷","ilovecccd","Me丶小莫_","单眼皮小龙","晚安前的想念灬","rocktotime","枯叶之烬","有姿_才有味","雍伦",
               "最后v的你","肖扬LHN","Emma努力","li1434544963","shini10086","汐雨落下","耿志轶","vicioush","Evynok","1002195794峰",
               "没办法132","l649624773","杨桃大缪斯","後知後覺Stupid","青春不考究","15823489447","您大家了","邻家好学生丶",
               "HLL665321","宝宝的爱来","一水隔天紫玉","一捧凊土","zxr7298710","065060256","暗夜RAN","朱古力熊","帅哥驾到2",
               "阳光丨灬小星","真爱这感觉","飞翔的57","baby变形金肛","goodkobe24","八月天88","九尾狐君free","tomy17","lacy0711",
               "白玫先生","毕沃特","chang20056","我的同桌是小黑","yumichong9322","小巷一角","彼岸等你的家","丁男子","GYY__ZW",
               "青青藻泽","奕生奕世独ai欢","一句话jjh","赏金铜c","徐路1990","loL钻石代打M","327a3654b","小芈粥_Beyond","70亿少女的梦丨",
               "zhu361224525","pangyg","这一次幸福圆圆","好久不見丶Mark","qq845351226","活了副人摸狗样","今世怀旧","心中有核",
               "a756522766","重新开始xuan","YTwoaini1992","崬OL","Beckarc","指望赐我空欢喜","圆丶sunny","23三四year","wny0202",
               "sunny云恩","781901775qqq","淘金者自由人","LWTVINTER","阿狸桃子酱之歌","棉云之泪水","liuzw613888","人鬼韦德",
               "Snake丶黑蛇","山药蛋土豆","不好骑会死星人","1351141030","cancer121238","旧梦亦安然丶","z341501","黔灵山越雨",
               "ljszzlt","Dear邱尼玛","桃公主圆儿","温和的急停跳投","vool2013","羡慕在赶超","九之极xx","tier37","yb2239050",
               "yexing_sml","HTヽ","L逝去的青春M","zhang3153525","蜡笔小新他叔叔","仙药奇谭","愛_曾經來過","李雨点1","811381033",
               "wh丶淡忘","黑狮子的咆哮","我以为我瘋了","离城梦远","月光晴朗05","yuwei1998119","摔倒的少年","挥断时光","sunny君昊",
               "zhunaier","87308194","卖客拉我","liye19880814","yangcheng512","Smile盆盆","从来未忘过灬","折一架纸灰机丶",
               "love白首莫分离","华丽的虚伪丶22","sl_plane_9898","习喜欢你","矫情不得好死","琅妹子绵羊","月崖_祭","丨神马都给力",
               "卡尺的春天","649445100","克克714","慕风沁","Recaell_影子","魑魅魍魉的内裤","流年丶Red","天涯111ok","一夕浮生仿若梦",
               "丿123丶不哭丨","半边王伽罗","頃欢","丶上官懿","紫冰凝痕","gxb1007","蕞後j","處吻給叻煙","天下无双的霜","iopjkl9",
               "妳给过的拥抱_","悦尔无因无语","超帅ZSC","蛟龙静缘","哥_气质迷人","唐远东5120","枪易怒","niu791148952","yankui963",
               "寻找曾经的霸气","BobPanBoWen","foreverlovezhe","小猪猪ZZZ0","洋葱712","假壳","小编婷纸","随緣随風","ghhhjjj879",
               "赋闲time","武装介入Zcy","亦然也翁","精灵天使爱莎莎","伯纳乌的grass","1046876648","无法修改For","swb980831","希亚_",
               "544037331","我靠谱你随意55","ok那年夏天宁静","圆来缘聚","河西老四","旧时光沉沦DIE","日光岸丶","云淡兮风轻","missskn",
               "卷卷郁熏","好名让猪猪抢了","沐清like","我是大禹专治水","小劲儿难拿","半梦岛屿丶","suye_苏叶","花间浅笑看尘世",
               "atrmis梦","yrz408321139","爱真的不说话","g036032","阳光的眺望1991","若晴沫","丶下得起法","儒雅的大便干燥",
               "Victor_Moses","女神木头","_丁呤呤呤呤","濤音嗳乐","纯二货i","abc天荡","华吧监事长","大丽爱有天","楓丨曦","Ehome_limited",
               "house夏日秋千","黑马er丶","zz潮流825","滥情的菊花","丿小卷发灬情调","孤闻寡陋的猫","最爱深入浅出","小布_go",
               "刘巍nashkd","V0老0师","无良先森__","wHitepApertime","乱世佳人小孩","越爱越不懂fly","earth王毓杰","elnino22","qiang尊",
               "许千秋一世","偶de发型怪怪","brit依依布舍","無歡公爵","zhixiangxu1993","Mright_king","速度舆激情_","24K纯玫瑰",
               "回忆如今变追忆","叫迪哥好吗","Smile丶525","小小牛郎星","半拉月","你才我才不才","人海旅行_lau","慕丝岚","飞扬的鱼的眼泪",
               "我是谁16621","请叫我佛107","最初的灬苍老","此情追忆001","zm89666666","丶雅金香","百ting兔","张博58585","记忆里的家乡9",
               "空明与红掌","xiao熊1005","最爱11_liang","老瘦老瘦啦","胸大肌丶1","青春忧伤de子弹","好你在妈","想要的幸福01",
               "Misaya_WeiXiao","宝贝平台快充","m1159906558","天山剑祖","晓剑破寒","身死为国殇","七度王爵银尘殿","世态炎凉丶go","晓默_",
               "弔贰莨菪","紫菜花开呀开","中州队长郑吒","血色残陽6","因帅__被判无妻","sunshine5237","驭剑逍遥","peewaa","飞达伦",
               "文艺213青年丶","juven2ove","黯淡的彼岸","欧文yjp","酒言虐x1n","o苏格兰开裆裤o","achudk","顶太阳打伞","阳关小清新",
               "火柴男孩smile","花季劣徒","佳旺丬","柔情雨兴","q544786005","爱谁谁的瓶子丶","那旋律殇","夏明焱","丶兰妗沐秋",
               "午夜牛郎爱萝莉","东北丶小枫","冷清拒绝暧昧","花心摩羯zmm","Qilychee","梅子__青时雨","xsd35889","x358922687","陳思豆",
               "戒361","暗夜终魂","郑宗代","望眼欲穿穿不过","love紫色L","妙手偶得618","驹是真理","流逝D记憶","楼下有妖",
               "莫莫不得语729","曹小强19940822","xh987196267","Happpppy67","在终点等你love","凉人惜良人","Heaven丶二阳","暮色染流年",
               "hh_loverui","18607150878","专治抠脚汉","你i太诚实","怪先生LV","氵水心","龟孙小次郎","龙龙加油smile","浮萍书侠",
               "選00擇","丶冷暖自知home","祝小侃","黯淡90","斌斌有醴","亚森别克","Ast丶乖乖","衡兰芷若beyond","penelope可","两年瞬间",
               "劲爆头菜","heart丶Ruin","谈闹闹切克闹","唯爱虎牙酱","烧饼来个兰州","卯寅散人","Oo为人民oO","雪花里胡哨","某某璃某某",
               "龙少丨丨诠释","望海心广","爱恨忐忑1993","go爱是大家的错","HaikiCeltics","一生恋_雪","叫我缝小肛","bulibuqiheart","嘿夏小白",
               "路飞H9","musclewan","浪阿浪阿浪阿","复色秋","weilandefeng0","Sweet__浅爱","是井崇不是精虫","不听__Sorry",
               "fhl15850695542","95张云杰","年华安然失笑","甜蜜悠悠的记忆","981692199","wenjiaxin1994","boss吕海涵","平水火火会幸福",
               "去年是对的","18732056677qwe","九洞的月光","思绪丶Thinking","fqybyypp","手握锋利大剑","LONG_爱你","易雨迟伤",
               "闵祁","爱圆一生一世","错觉因你而生","平平淡淡486","rangerhang","很宅很宅很宅","wjg1_nbu","左左300","monckey1jack",
               "凝芸涟玂","呦丶木沐","1095623550","zhu010324","丶悟空日王母","米面年糕","iwaitingyang","拽拽衰锅","灬sweet丶oO",
               "紫梦涵go","毕生毕夏","sky小丑511","划过天空乀","陆小游66","兮Kiss丶","馨香盈室","记忆中的美丽","文明5211","wang5031535",
               "焦油好害人","褘偌","wqy巨蟹","你的笑里有毒药","楼哥log","浅唱悲伤HJ","★╮尛博","亲嘴嘴嘴嘴嘴嘴","Yuhaixin丶",
               "此生爱你虾虾","葑嗳擱淺","Smile丶简单","星期四快乐","nengjianglu","小母鸡狼","蔑浮生","龙爷20200","没有魜哆潇洒5",
               "N年的越策","rhrrt100","沧海永横流","原以为爱情不在","魔术师VS龙","海一情债","爱圆一族","晴天小小爱","没有仕相的帅",
               "最爱圆梦一生","是钉子_怕锤子","kjhyxzj","宝尊至rw","hithdzhao","ilovehao110","骚年时代life","戏弄灬青春","静看微光散",
               "絮儿_ym","小夜1721908387","小猪甜酸","deas520","ForeverSasa","qinxiaoheia2","绽放奇迹ye","Almost_lover05","浮花无泪",
               "wazjh19930901","lswaini363","忆海的阿宏","青__亦心","啊困惑咋过","不打酱油的汉子","泡虫虫","Tzy809996782","zxc莫凡",
               "y1世丨丶情深","周子豪②","轻点er","耀阳高加索","向东方year","值班重地","pangruifeng","璐璐my缪斯","彧骁萧","0红黑天空0",
               "123456粉丝","沉默小黑蛋","_记忆早已逝去","刘l涛t","无敌鸣羽","博林2013","那儿的猫","脉搏happy","poison太毒","小时代1_0",
               "ren末日的主宰","糖果火山","明小天426","Queen940810","爱笑阁_暴君","倚柳看花","yufeng1301","剑骊","烟花易冷DOVE",
               "364737255","陌小炫123","深藏blueee","为你努力为你忧","ASB丶","十分爱信","仙姿佚貌倾城雪","bennyz","Zero气质女神",
               "晓晓慧心","念∑天涯","630535979","gspz21","逸厢情愿","Pu泡泡泡泡泡丁","玛玛姑临三咩答","sunny丹老公","songkaiai3",
               "宇诗Teresa","tutu822","乐土的追逐","碎了的心_nice","喜怒哀乐忧思惊","彡华丽的转身彡","超级机器2012","不再联系过你",
               "大爱美女姐姐","广东小荣哥丶","THE_ONE_LuFFy","阿森纳Lion","圆圆圆圆圆圆桃","学做许仙敢曹蛇","王亚飞3456",
               "吃盐焗鱼的兔子","未曾绽放便枯萎","文艺summer","Pasumi","碎花舞步踩阳光","忘不掉tmd","不见澄光","丿望aud","哈哈宝贝F",
               "小爽600","凉快0000","YYzuizui","懵豪__","CCWASLJ1314","么萦","黑桃k123456789","shh0312","爱上你的床头柜",
               "破碎的方城","lu_you_w","黑木耳含香蕉","四月·甜蜜","vv任逍遥","被埋葬的爱AI","放弃PD","玉树凌风美少男","Show一表人渣",
               "夜景勿繁华灬","zhang481279","小朵特洛夫斯基","不吃饭U别叫我","用情不用钱","看楼上说的","圈圈框框day","喝醉的小强baby",
               "RamseywY","那天她说谢谢","凌乱__陌上烟雨","铁血丹心2188","1601026602","小由就是美","死亡de钢琴师","Red君子兰",
               "远地徘徊者","tforeverlovey","笑面小刀","只能相亲了","Da阿楠","y狼血沸腾","飞哥的住家鸡","阡天使陌泪","紫心雨栗",
               "无所谓了同学","阳光下的温度丶","1105916625S","2859864736","lemoncancer","承诺比慌言更假","纳纳纳纳公主","Content丶J",
               "我知道社会太假","LOL罂粟","君容未老","所谓的幸福已逝","小小o琳琅o","女神丶高圆圆","被任性的青春","唯思小强哥",
               "伊萧静澜","没有时间了so","折磁","星辰老三","什么叫做僾","ˉゝ睿丶","Alyssa雯名天下","HJX水瓶","粟豫的海水","凋画",
               "王一烽1992","我爱郑玮","蜜蜂飘过爱幂","钻石冯","咚次哒次GO","Saner丶","我是金十顺","今天要倒霉","你若成风Wind",
               "善良的李小刚","向善的野心","栅栅来迟喽","卡A卡巴斯基","呵呵你Ma渣","青柠和沥鹿","sky汪仁杰","逗比爱剑银","变相",
               "归来的洛秋","假如安若浮生","呆老头000","恋床的孩子1","丶硪们的约定","蓝色袋小当家","大爱圆圆sunny","冉静丶STing",
               "丿锦瑟","Somous丶小神","樱花树下程小杰","陌上清歌落笙","抽象中有点具体","潇水39好","盖世英雄LSC","栢嘟丶",
               "惜小小君君","金子刘金鑫","Carzy_花裤衩丶","S__S__Snake","go咸蛋超人007","蕊尓","我爱大美女_","我是梁潇洒","cst0622",
               "若能后知后觉","天蚕土豆死","草遇秋","樱木火神","mch8023惜小君","GO家有布丁","a5316613","馨染回忆VI","知我如我",
               "神一样的oO","圈圈_mona","孩子他表哥","月光老人A","i_祝你爆炸","Byiove灬沐","v点烟","滕县滴爷们","情_落兮",
               "泡8喝9搞10髦","迗秤__幻羽","zhao960803","弥敦道hhh","蕞薆姈","Mk曲终人散","南城东少year","秋去冬寒","wenflylove",
               "mosen木木木","不在微笑的脸庞","Mr玉米","何必要想念","光阴x","ptmwdgdng","泽络星辰","左手干大事","故事已结尾Pets",
               "花痴男银c","PP吧45","同桌是个禽兽","Ssatisfaction","00蛋蛋花香00","稚三绳","小L的猜想true","517818","feel耀",
               "快播少年0","yangchi0729","结婚证002","xc徐铖","情獸丶Se7en","滈圎圎","我是蜜糖没商量","4545xuhao","Baby丶默念幸福",
               "Supper浅夏","莫欺少年穷通哥","幸运女神在尖叫","水瓶座浅唯落","小悠_smiling","蚊子丶7","泪琳湿诺言","收复台湾2030",
               "dream高圆圆","ok谁家的少爷","邪败寇","糖神快到碗里来","碾碎红尘暗香残","life0忧桑","桎樽忧伤","赵小健99","婷子装C",
               "o拭目以待","西伯利亚小厄狼","7只煎蛋","青春缺妳yi个","sunny卿志云","有种思念不忘","宝宝我好强","小破孩心情",
               "最爱Fu建","2559183379","come_across13","我是吉他的老大","哈格潞里","ma1677077709","2623259759","语墨笔耕",
               "zhangyinzhen20","a1024331926","2circle_love","sonics02012","雍雍雍雍卓","迷茫de夜时代","狂爱与恨","安亲4","飞花血月16",
               "szk1799","Best丶操性","卫生棉男孩","awedfgynm1458","游kaer离","大爱圆圆姐","3漫漫星空a","最爱不过LPL","米饭炖排骨",
               "hong1993min","天山二侠","叶落霜林方知秋","心比心更","那够歇斯底里吗","染色啦","黑丑穷呆缺心眼","依卡牛仔","冀中本事",
               "那抹微笑里","梦想怀揣希望","rong960121","给力32158","坑天大圣丶","danny034562","丶独孤一方夜","灬QC","┕麯终秂散↘",
               "碧城王者","qy石头剪刀布","真没你丑","恋晨熙","canyougeelit","飞大大大少","黑小科24","D丶K丨灬悲伤","丶丨么么哒丨",
               "SN_不作解释","dd5418854188","先锋gogoing","D_Hongyang","ok淡然一切","等不到_的天晴","暴走唐人街","微young",
               "刘丶风暴烈酒","SummerCharles","酱油先生而已","___記憶_","苏志燮37","kobewudi000","俺名叫二牛","smile邓京华",
               "aa852160283","丶丶丶丶丶明天","灵曦summer","yzgaiying","Auc冠希","天才第㈡步","深海∮精灵","孔家飞","老子很帅0",
               "完美的爱08","昔亿的骚年","繁华已褪","猥琐淂坏叔叔","丶Time灬灬","ylw1103","Loyebaby","万花丛中大松鼠","Paris王heaven",
               "爽朗的黑森林","luis_MAC","空浮SKY","安以轩Ann粉友","射手百纳","奋斗君12138"]

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", db="taxi", port=3306, charset="utf8")
cursor = conn.cursor()

special_people = [
    "赵余波", "王友奎", "万淳洁", "苟朝华", "李卒", "王友平", "封华", "卞章勇", "魏宏", "彭高伦", "刘洋",
    "刘彬", "杜国孝", "陈克刚", "徐战国", "陈勇", "孙继亚", "胡正军", "张宝", "卞章永", "彭高伟"
]

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