#!user/bin/python
# coding:utf-8

# from selenium import webdriver
# import re
# import time
# import requests
# sc=[]
# # faileurl1=['http://www.cnblogs.com/zhuwoyao88/p/8449053.html']
# faileurl1=[ 'https://wenku.baidu.com/view/92c33d7b0029bd64783e2cef.html\n', 'http://www.open-open.com/lib/view/open1437483697115.html\n', 'http://www.onlinedown.net/soft/989451.htm\n', 'https://www.jianshu.com/p/bfa86847f81e\n', 'http://www.cnblogs.com/wanqieddy/archive/2011/12/15/2288598.html\n', 'http://www.cnblogs.com/sushi/p/7682996.html\n', 'https://www.cnblogs.com/minieye/p/5806911.html\n', 'https://www.cnblogs.com/notepad/articles/4711528.html\n', 'http://www.cnblogs.com/chongyou/p/5374406.html\n', 'https://www.cnblogs.com/xuxuzhaozhao/p/6740046.html\n', 'https://www.cnblogs.com/brad1994/p/6540461.html\n', 'https://www.cnblogs.com/Mushishi_xu/p/7685903.html\n', 'https://testerhome.com/topics/10552\n', 'http://www.php.cn/python-tutorials-358252.html\n', 'http://www.cnblogs.com/zz-yy/p/8432815.html\n', 'http://www.cnblogs.com/yoyoketang/p/6128741.html\n', 'https://www.cnblogs.com/BlueSkyyj/p/8392628.html\n', 'http://blog.csdn.net/kaka1121http://www.51testing.com/html/15/n-3717415.html\n', 'https://www.cnblogs.com/Mushishi_xu/category/1098394.html\n', 'https://nodejs.org/dist/v6.9.4\n', 'https://www.cnblogs.com/teamemory/p/8473727.html\n', 'https://m.jb51.net/softjc/595372.html\n', 'https://www.cnblogs.com/general-seven/p/6144972.html\n', 'http://www.51testing.com/html/47/n-3719147.html?from=groupmessage\n', 'https://www.cnblogs.com/aestheticism/p/5064998.html\n']
# # faileurl1=[  'https://blog.csdn.net/column/details/12694.html\n', 'http://www.cnblogs.com/cnhkzyy/p/9252884.html\n', 'http://www.cnblogs.com/fengsiyi/p/7206537.html\n', 'http://www.360doc.com/content/11/0124/14/5480484_88697703.shtml\n', 'http://www.360doc.com/content/18/0913/13/3175779_786335678.shtml\n', 'http://0cx.cc/python_captcha_breaker.jspx\n', 'https://www.aliyun.com/jiaocheng/452316.html\n', 'https://www.sogou.com/tx?query=%E9%AA%8C%E8%AF%81%E7%A0%81+Python+%E5%80%BE%E6%96%9C%E5%BA%A6&ie=utf8&_ast=1538990336&_asf=null&w=01029901&hdq=sogou-clse-f507783927f2ec27&duppid=1&cid=&s_from=result_up&sut=1602&sst0=1538990168221&lkt=0%2C0%2C0&sugsuv=00662FD673C658C45BBAAFD6DE318500&sugtime=1538990168221\n', 'https://mp.weixin.qq.com/s/XW9geHZ9odHdI7srDiKBIg\n', 'https://www.yiibai.com/git/git-quick-start.html\n', 'https://testerhome.com/topics/12709\n', 'https://www.cnblogs.com/simple-free/p/8447358.html\n', 'https://www.aliyun.com/jiaocheng/450854.html\n', 'https://wenku.baidu.com/view/e4a23d0703d8ce2f00662335.html\n', 'https://www.cnblogs.com/NancyRM/p/8243821.html\n', 'https://www.pythontab.com/html/2017/pythonhexinbiancheng_1120/1184.html\n', 'https://www.pythontab.com/html/2017/pythonhexinbiancheng_1120/1184.html\n', 'https://www.cnblogs.com/chenlogin/p/6592228.html\n', 'https://pypi.org/project/opencv-python/#files\n', 'http://www.cnblogs.com/chensheng-zhou/p/4895332.html\n', 'https://www.linuxidc.com/Linux/2018-09/154317.htm\n', 'https://www.cnblogs.com/wuzhiming/category/665000.html\n', 'https://blog.csdn.net/reboot123\n', 'http://www.cnblogs.com/only-love-you-519920/p/Alice.html\n', 'http://www.cnblogs.com/fengpingfan\n', 'http://www.cnblogs.com/yangxia-test/p/4137519.htmlJmeter\n', 'http://www.cnblogs.com/linxinmeng/p/7207156.html\n', 'https://www.yiibai.com/jmeter/jmeter_web_test_plan.html\n', 'http://www.cnblogs.com/cnhkzyy/p/9252884.html\n', 'http://www.cnblogs.com/fengsiyi/p/7206537.html\n', 'http://www.360doc.com/content/11/0124/14/5480484_88697703.shtml\n', 'http://www.cnblogs.com/meitian/p/6103391.html\n', 'http://www.testclass.net/appium/appium-base-summary/\n', 'https://baike.sogou.com/v171812.htm?fromTitle=.bat\n']
# i=0
# for url in faileurl1:
#     url1=url.strip()
#     r=requests.post(url1,)
#     r2=r.text
#     r3=r2.split("title>",2)
#     # print r3
#     r4=r3[1]
#     # print r4
#     r5=r4[:-3]
#     i+=1
#     sc1 = '<DT><A HREF=' + '"' + url1+ '"' + ">" + r4+ "</A>"
#     sc.append(sc1)
#     if i == 10:
#         print sc
#

# with open("rsa_private_key.pem","r") as f:
#     lines=f.readlines()
#     print lines
#     a=lines[1:-1]
#     print a
#     c=[]
#     for i in a :
#         b=i.strip()
#         c.append(b)
# print c
# z=''.join(c)#list 转化为str
# print z
# with open("./rsa_private_key.pem", "w") as f2:
#     f2.write(z)
# import os
# path="12"
# print os.listdir('.')#当前目录
# print os.path.splitext(path)#以后缀名开始分割

# #输入某年某月某日，判断这一天是这一年的第几天？
# year=int(raw_input('year:'))
# month=int(raw_input('month:'))
# days=int(raw_input('days:'))
# months=(0,31,59,90,120,151,181,212,243,273,304,334)
# if 0<month<=12:
#     sum=months[month-1]
#     sums = sum + days
# else:
#     print "data error"
# leap=0
# if (year%400==0) or ((year%4==0)and(year%100!=0)):
#     leap=1
# if (leap==1) and (month>2):
#     sums+=1
# print "it is the %dth day."%sums

# # 输入三个整数x,y,z，请把这三个数由小到大输出。
# l=[]
# for i in range(3):
#     x=int(raw_input("正式:"))
#     l.append(x)
# l.sort()
# print l

# # 将一个列表的数据复制到另一个列表中。
# a=[1,2,3]
# b=a[:]
# print b

# 输出 9*9 乘法口诀表
# for i in range(1,10):
#     print ''
#     for j in range(1,i+1):
#         print "%d*%d=%d"%(i,j,i*j)


# # 暂停一秒输出。
# import time
# myD={1:'a',2:'b'}
# for key,value in dict.items(myD):
#     print key,value
#     time.sleep(1)

# # 暂停一秒输出，并格式化当前时间。
# import time
# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# time.sleep(1)

# # 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# f1=1
# f2=1
#
# n=int(raw_input("how rabbit:"))
# if 0<n<3:
#     for i in range(1,n+1):
#         print "%d month rabbit numbers is %d" % (i,f1)
# else:
#     print "1 month rabbit numbers is 1"
#     print "2 month rabbit numbers is 1"
#     for i in range(3,n+1):
#         f=f1+f2
#         print "%d month rabbit numbers is %d" %(i,f)
#         f1=f2
#         f2=f
#方法二
# f1=1
# f2=1
# for i in range(1,4):
#     print "%5ld %5ld"%(f1,f2)
#     if i%3==0:
#         print ''
#     f1=f1+f2
#     f2=f1+f2

# #判断101-200之间有多少个素数，并输出所有素数。
# from math import sqrt
# from sys import stdout
# h=0
# leap=1
# for  m in range(101,200):
#     k=int(sqrt(m+1))
#     for i in range(2,k+1):
#         if m%i==0:
#             leap=0
#             break
#     if leap==1:
#         print "%-4d"%m
#         h+=1
#         if h%10==0:
#             print ''
#     leap=1
# print "total is %s"%h
# # 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# for n in range(100,999):
#     i=n/100
#     j=n/10%10
#     k=n%10
#     if n==i**3+j**3+k**3:
#         print n

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。  15

# import datetime
# print (datetime.date.today().strftime('%Y%m%d'))

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。


# #time
# import time
# print time.time()
# print time.ctime()
# print time.localtime()
# print time.strftime("%Y %m %d %H:%M:%S",time.localtime())
#
# import os
# print os.path.abspath(os.path.abspath("aa"))

# from selenium import webdriver
# from selenium.webdriver.common.alert import Alert
# import time
# import os
# driver=webdriver.Chrome()
# driver.implicitly_wait(3)
# file='file:///F://alert.html'
# driver.get(file)
# driver.find_element_by_xpath('//*[@onclick="myFunctionPrompt()"]').click()
# time.sleep(2)
# prompt=Alert(driver)
# print ('prompt text:'+prompt.text)
# prompt.send_keys("study no jintou")
# time.sleep(2)
# prompt.accept()
# print ('what you have done is :'+driver.find_element_by_id('action').get_attribute('value'))
# time.sleep(2)
#

# import json
# a={1:2}
# print type(a)
# print json.dumps(a)
# print type(json.dumps(a))
# print type((1,2))
# print json.dumps((1,2))
# print type(json.dumps((1,2)))
#
# import time
# import os
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
# print driver.window_handles
# t=time.strftime("%Y%m%d.%H%M%S",time.localtime())
# print t
# file='./'+t+'.png'
# # file=os.path.dirname(os.path.realpath(__file__))#获得当前文件__file__所在的目录
# # print file
# driver.get_screenshot_as_file(file)
#
# import time
# import os
# print os.path.dirname(__file__)#脚本所在目录路径
# print os.path.realpath(__file__)#脚本路径
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
# filename = str(int(time.strftime("%m%d%H%M%S", time.localtime())))
# filename = os.path.dirname(os.path.realpath(__file__))+"\\picture\\"+filename + ".png"
# print filename
# driver.save_screenshot(filename)
# time.sleep(1100)
# #读取文件中的汉字
# import io
# with io.open("F:\jiandian\daifu33.txt",'w',encoding='utf-8') as f:
#     f.write(unicode("\xEF\xBB\xBF","utf-8"))
# with open("F:\jiandian\daifu33.txt" ) as file:
#     aa = file.readlines()
#     print aa
#     for i in range(len(aa) + 1):
#         print aa[i]
#         bb = aa[i].split(",")
#     print "this is bb:%s" % bb

# a="CDwindow-1"
# print type(a)
#
# import time
# from selenium   import webdriver
# from selenium.webdriver.support.ui import Select
# driver =webdriver.Chrome()
# driver.get('https://cpay.hypayde.com/demo.html?debug=true')
# # self.driver.get('https://pay.hongnaga.com/?debug=true')
# a = driver.switch_to.alert
# # a.send_keys("123456778")
# a.send_keys("112233")
# a.accept()
# time.sleep(2)
# # self.driver.tap([(523, 1825)], 890)
# lines = [18]
# i = 1
# windows1 = driver.window_handles
# print"before pay%s" % windows1
# for price in lines:
#     print  price
#     # 商户ID
#     driver.find_element_by_xpath("//*[@name='mch_id']").clear()
#     driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("1025")
#     # 支付方式
#     pay_type = Select(driver.find_element_by_id("pay_type"))
#     driver.find_element_by_id("pay_type").click()
#     # pay_type.select_by_value("11")  # 支付宝wap
#     pay_type.select_by_value("7")  # （支付宝）当面付扫码
#     # pay_type.select_by_value("5")  # 支付宝H5
#     # 金额
#     driver.find_element_by_name("price").clear()  #
#     driver.find_element_by_name("price").send_keys(price)
#
#     driver.find_element_by_id("pay").click()  # 点击了但是没有得到相应的效果
#     time.sleep(5)
#     print driver.current_window_handle
#     # print self.driver.title
#     # self.driver.switch_to.active_element.click()
#     # self.driver.find_element_by_id("pay").click()
#     # time.sleep(10)
#     windows = driver.window_handles
#     print "after pay%s" % windows
#     # print windows[-1], type(windows[-1])
#     # # w = windows[-1]
#     # # ww = w.encode('utf-8')
#     # # print type(ww)
#     # driver.switch_to.window(windows[-1])
#     driver.close()
#     print driver.current_window_handle
#
# aa={"mobile":"15868314566","code":"123456790","invite_code":"12344568"}
# print aa.get("code")
#
# bb={'token': 'd6f2c03aaae0c95755ea5c8f071dcf1a', 'Content-Type': 'application/json'}
# cc=sorted(bb.items())
# print cc

# import requests
# headers={'token': 'd7098cd6f681e07fe87c0fd60bb1b144', 'Content-Type': 'application/json'}
# url="https://wallet.herbeauty.top/api/v1/banner/1"
# print requests.get(url,headers=headers).text

# a={'a':'v'}
# # b=str(a)
# # # c=eval(a)
# # d=eval(b)
# print type(a)
# import os
# import re
# rlist=[]
# name  = "F:/Users/tinyw/PycharmProjects/untitled/hswallet/cases/"
# # print name
# # print os.walk(name)
# for dir,folde,file in os.walk(name):
#     for i in file:
#         t = "%s%s" % (dir, i)
#         if (re.match('wallet_*',i))!=None:
#         # print t
#             rlist.append(t)
# print rlist

# for i in rlist:
#     name1=re.match('wallet_*',i).span()
#     print name1

# def verify_code1():
#     verify_code=1
#     login_headers=2
#     return verify_code,login_headers
# print verify_code1()[1]

# a="1234"
# print a[-2:]
#
# import time
# import datetime
#
# t = time.time()
#
# print (t)                       #原始时间数据
# print (int(t))                  #秒级时间戳
# print (int(round(t * 1000)))    #毫秒级时间戳
#
# nowTime = lambda:int(round(t * 1000))
# print (nowTime())           #毫秒级时间戳，基于lambda
#
# print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   #日期格式化
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# b=(str(round(t * 1000)),158)
# a={}
# a["dd"]=format(int(1554107715308))
# print a,b

#
# import demjson
# data =[{'a':1,'b':2}]
# print type(data)
# data2=demjson.encode(data)
# print type(data2)
# print data2

import os,time
# aa=os.system("adb shell dumpsys cpuinfo | findstr com.example.wallet.dev")
# print aa
nn=os.popen('adb shell dumpsys cpuinfo | findstr com.eg.android.AlipayGphone')
# time.sleep(2)
print nn.readlines()
# nn=os.popen("adb shell dumpsys battery")
# # time.sleep(2)
# print nn.readlines()
# adb shell dumpsys cpuinfo | findstr com.eg.android.AlipayGphone
#  com.example.wallet.dev/com.example.wallet.core.main.MainActivity
# import requests

# headers={'token': 'ca2c2def79a8da5d9b644eaa668931d0', 'Content-Type': 'application/json'}
# r=requests.get("https://wallet.herbeauty.top/api/v1/user/set_real_name?id_type=2&credential_no=410&real_name=张三疯",headers=headers).text
# print r


