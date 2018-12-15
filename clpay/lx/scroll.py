#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("file:///C:/Users/WYJ/Desktop/scroll.html")
# time.sleep(2)
js='var q=document.getElementByClassName("scroll").scrollTop=10000'
# js2='document.getElementsByClassName("scroll")[0].scrollHeight'
driver.execute_script(js)

# a=driver.execute_script(js2)
# print a