#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
a=[u'100,195.00', u'\u5143']
# for i in a:
#     i.encode('unicode','ignore')
print type(a)

print a[0]
print type(a[0])

b=[u'', u'0\u7b14', u'/', u'23\u7b14']
print b

print "ss %s %s"%(a,b)

print 379-1.44+65-0.23+216-0.82

a=[1,2]
b=[1,2]
if a==b:
    print "a==b"

def ii():
    i=1
    iii=2
    return [i,iii]

print ii()

c=(1,2)
d=(1,2)
if c==d:
    print "c==d"


c=[[12,23],[45,56]]
print  c[0][1]
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
a=[]
dd = ['3\n', '2\n']
for i in dd:
    print i[:-1]
print dd
f1 = open("E:\\zxtest\\ddpush.txt", 'r')
lines = f1.readlines()  # 读取全部内容 ，并以列表方式返回
print lines
# f1 = open("E:\\zxtest\\ddpush.txt", 'r')
# lines = f1.readlines()      #读取全部内容 ，并以列表方式返回
# print lines
# for i in lines:
#     i[-1]
# a=[1,2.3]
# a[-1]
zz="  1235126412"
print zz.strip("12")