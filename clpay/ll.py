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

with open("E:\\zxtest\\lianjie2.txt", 'r') as f:
    lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
    print lines
    with open("E:\\zxtest\\lianjie4.txt", 'r') as f2:
        lines2 = f2.readlines()  # 读取全部内容 ，并以列表方式返回
        print lines2
        for i in lines:
            print i
            for j in lines2:
                print j
                if j==i:
                    print i
                    with open("E:\\zxtest\\lianjie5.txt", 'w') as f5:
                        f5.write('%s'%j)
                else:
                    with open("E:\\zxtest\\lianjie5.txt", 'w') as f5:
                        f5.write('%s'%j)
                    with open("E:\\zxtest\\lianjie5.txt", 'w') as f5:
                        f5.write('%s'%i)
# a=['https://blog.csdn.net/test94/article/details/51519789   Android\xd7\xd4\xb6\xaf\xbb\xaf\xb2\xe2\xca\xd4Python\n','\xa3\xa8\xd4\xad\xb4\xb4\xa3\xa9\xc8\xe7\xba\xce\xb6\xd4APP\xb7\xfe\xce\xf1\xb6\xcb\xbd\xf8\xd0\xd0\xd1\xb9\xc1\xa6\xb2\xe2\xca\xd4\n']
# t=a[0]
# # print y
# re.match('\s',t)
# str1=a[0].split(' ',1)
# a=str1[0]
# print a