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
driver = webdriver.Chrome()
#我们先打开一个网页
driver.get("https://www.zhipin.com/user/login.html")
#浏览器 新窗口打开连接
newwindow = 'window.open("https://www.baidu.com")'
driver.execute_script(newwindow)
#移动句柄，对新打开页面进行操作
driver.switch_to.window(driver.window_handles[1])
#具体操作

driver.find_element_by_id("kw").send_keys("hhh")
#关闭该新打开的页面
# driver.close()
#不关闭，要移动到上一个页面，我们要移动句柄
driver.switch_to.window(driver.window_handles[0])
