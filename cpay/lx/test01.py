#!/user/bin/python
#  -*-coding: utf-8-*-

from selenium import webdriver
import requests
import time
import json
import re
# driver=webdriver.Chrome()
# with open("F:\\lianjie4.txt") as f:
#     lines=f.readlines()
    # i=0
    # for url in lines:
    #     driver.get(url)
    #     js="window.open('https://www.baidu.com');"
    #     driver.execute_script(js)
    #     handles=driver.window_handles
    #     driver.switch_to.window(handles[-1])
    #     i+=1
    #     if i%20==0:
    #         driver = webdriver.Chrome()
    # time.sleep(1000000)
    # #     url2=url.split("https")
    # #     print url2
    # #     with open("F:\\lianjie5.txt",'w') as f1:
    # #         for i in url2:
    # #             f1.write(i)


with open("F:\\lianjie4.txt") as f:
    lines=f.readlines()
    for url in lines:
        r1=requests.get(url,).text
        print r1
        r2=r1[-400:-1]#截取
        r3=r2.split(',')#分割出title
        r4=r3[-2].split("'")
        print r4
        r5=r4[-2]
        print r5

