#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time

# a=[u'100,195.00', u'\u5143']
# # for i in a:
# #     i.encode('unicode','ignore')
# print type(a)
#
# print a[0]
# print type(a[0])
#
# b=[u'', u'0\u7b14', u'/', u'23\u7b14']
# print b
#
# print "ss %s %s"%(a,b)
#
# print 379-1.44+65-0.23+216-0.82
#
# a=[1,2]
# b=[1,2]
# if a==b:
#     print "a==b"
#
# def ii():
#     i=1
#     iii=2
#     return [i,iii]
#
# print ii()
#
# c=(1,2)
# d=(1,2)
# if c==d:
#     print "c==d"
#
#
# c=[[12,23],[45,56]]
# print  c[0][1]
# driver = webdriver.Chrome()
# #我们先打开一个网页
# driver.get("https://www.zhipin.com/user/login.html")
# #浏览器 新窗口打开连接
# newwindow = 'window.open("https://www.baidu.com")'
# print newwindow
# driver.execute_script(newwindow)
# print driver.window_handles
# # print driver.current_window_handle
#
# #移动句柄，对新打开页面进行操作
# driver.switch_to.window(driver.window_handles[-1])
# print driver.current_window_handle
# #具体操作
#
# driver.find_element_by_id("kw").send_keys("hhh")
# #关闭该新打开的页面
# # driver.close()
# #不关闭，要移动到上一个页面，我们要移动句柄
# driver.switch_to.window(driver.window_handles[0])
# #
#
# import re
# a=[]
# with open("E:\\zxtest\\lianjie3.txt", 'r') as f:
#     lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
#     print lines
#     i=0
#     k=0
#     l=len(lines)
#     # print l
#     for line in range(l-1):#以索引值遍历
#         if len(lines[i-k])==1:#第i-k个值的长度等于于1 （不为\n）,删除它
#             del lines[i-k]
#             # print lines
#             k = k + 1
#         # print lines[i-k]
#         if re.match('http',lines[i-k])==None:#lines每个值  匹配http 删除不包含http的值
#             del lines[i - k]
#             k=k+1
#         i=i+1
#     for lj in lines:  # 将list中的值取出来，将值分割  list不支持分割   split()分割str
#         re.match('\s', lj)
#         str1 = lj.split(' ', 1)
#         l = str1[0]
#         a.append(l)
# # print a
#
# with open("E:\\zxtest\\lianjie4.txt", 'w') as f2:
#     for line in a:
#         len1=len(line)
#         # print len1
#         f2.write('%s'%line)

import requests
import time
import json
import re
# driver=webdriver.Chrome()
# with open("F:\\lianjie4.txt") as f:
#     lines=f.readlines()
#     i=0
#     for url in lines:
#         driver.get(url)
#         js="window.open('https://www.baidu.com');"
#         driver.execute_script(js)
#         handles=driver.window_handles
#         driver.switch_to.window(handles[-1])
#         i+=1
#         if i%20==0:
#             driver = webdriver.Chrome()
#     time.sleep(1000000)
    #     url2=url.split("https")
    #     print url2
    #     with open("F:\\lianjie5.txt",'w') as f1:
    #         for i in url2:
    #             f1.write(i)

sc=[]
faileurl=[]
with open("E:\\zxtest\\lianjie4.txt") as f:
    lines=f.readlines()
    i=0
    for url in lines:
        i+=1
        url2=url.strip()  #清除字符串尾的\n
        # print "url:%s"%url2
        r=requests.post(url2,)
        # time.sleep(2)
        r1=r.text#获取post返回界面
        # print r1
        if re.search("page_url",r1): #在所有字符串中匹配page_url
            # print "页面打开成功：%s"%url2
            # print r1
            r2=r1[-400:-1]#截取
            r3=r2.split(',')#分割出title
            # print r3
            r4=r3[-2].split("'")#以'作为分割
            # print r4
            r5=r4[-2]
            # print r5
            # url2="u'"+r5+"'"
            sc1='<DT><A HREF='+'"'+url2+'"'+">"+r5+"</A>"
            sc.append(sc1)
        else:
            # print "页面打开失败：%s"%url2
            faileurl.append(url)
        if i==85:
            print "faileurl%s"%faileurl
            print "sc:%sc"%sc


sc=[u'<DT><A HREF="https://www.cnblogs.com/shamo89/p/9032371.html">jmeter\u63a5\u53e3\u6d4b\u8bd5\u62a5java.net.SocketException: Socket closed\u9519\u8bef\u3002 - \u90a3\u5565\u5feb\u770b - \u535a\u5ba2\u56ed</</A>', u'<DT><A HREF="https://testerhome.com/topics/12474">TesterHome</</A>', u'<DT><A HREF="https://www.cnblogs.com/imlvbu/p/7127940.html">\u3010\u4eb2\u6d4b\u3011appium_v1.4.16\u7248\u672c\u81ea\u52a8\u5316\u9002\u914dandroid7.0\u7cfb\u7edf - imlvbu - \u535a\u5ba2\u56ed</</A>', u'<DT><A HREF="https://www.cnblogs.com/windhome/p/7615251.html">appium\u542f\u52a8\u8fd0\u884clog\u5206\u6790 - \u98ce\u541f\u7684\u5c0f\u5c4b - \u535a\u5ba2\u56ed</</A>', u'<DT><A HREF="https://www.cnblogs.com/fnng/p/8486863.html">uiautomator2 \u4f7f\u7528Python\u6d4b\u8bd5 Android\u5e94\u7528 - \u866b\u5e08 - \u535a\u5ba2\u56ed</</A>', u'<DT><A HREF="http://www.cnblogs.com/fnng/p/5370433.html">\u5173\u4e8e\u81ea\u52a8\u5316\u6d4b\u8bd5\u7684\u8bef\u533a(\u4e00) - \u866b\u5e08 - \u535a\u5ba2\u56ed</</A>', u'<DT><A HREF="https://www.cnblogs.com/rookie-c/p/5755093.html">web\u6d4b\u8bd5\u4e0eapp\u6d4b\u8bd5\u7684\u533a\u522b - Rookie_C - \u535a\u5ba2\u56ed</</A>', u'<DT><A HREF="https://www.cnblogs.com/xueweihan/p/5207959.html">[python]decimal\u5e38\u7528\u64cd\u4f5c\u548c\u9700\u8981\u6ce8\u610f\u7684\u5730\u65b9 - \u524a\u5fae\u5bd2 - \u535a\u5ba2\u56ed</</A>', u'<DT><A HREF="https://www.cnblogs.com/rookie-c/p/5755093.html">web\u6d4b\u8bd5\u4e0eapp\u6d4b\u8bd5\u7684\u533a\u522b - Rookie_C - \u535a\u5ba2\u56ed</</A>', u'<DT><A HREF="http://bbs.tianya.cn/post-itinfo-437263-1.shtml">APP\u6d4b\u8bd5\u600e\u4e48\u505a\uff0cAPP\u6d4b\u8bd5\u7684\u6700\u4f73\u65b9\u6cd5(\u8f6c\u8f7d)_\uff29\uff34\u89c6\u754c_\u8bba\u575b_\u5929\u6daf\u793e\u533a</</A>']
for i in sc:
    print i



# for i in sc:
#     print i

# print 988-189

# a=['https://blog.csdn.net/test94/article/details/51519789   Android\xd7\xd4\xb6\xaf\xbb\xaf\xb2\xe2\xca\xd4Python\n','\xa3\xa8\xd4\xad\xb4\xb4\xa3\xa9\xc8\xe7\xba\xce\xb6\xd4APP\xb7\xfe\xce\xf1\xb6\xcb\xbd\xf8\xd0\xd0\xd1\xb9\xc1\xa6\xb2\xe2\xca\xd4\n']
# t=a[0]
# # print y
# re.match('\s',t)
# str1=a[0].split(' ',1)
# a=str1[0]
# print a