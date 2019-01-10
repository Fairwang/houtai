#!/user/bin/python
#  -*-coding: utf-8-*-
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random
#阿里云识别印刷体，UI定位还是上传图片
url='http://duguang.aliyun.com/demo/general.htm?type=contract'
driver=webdriver.Chrome()
driver.get(url)
time.sleep(3)
user_iframe = driver.find_element_by_xpath('//*[@id="alibaba-login-box"]')  # iframe
time.sleep(3)
driver.switch_to.frame(user_iframe)
driver.find_element_by_xpath('//*[@attr-type="alipay"]').click()
f=open('E:\\zxtest\\aliyun.txt','r')
account=f.readlines()
for a in account:
    aa=a.strip()
    user=aa.split(',')[0]
    passw=aa.split(',')[1]
    time.sleep(2)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='J-loginMethod-tabs']/li[2]").click()
    print "yes1"
    for i in user:
        t = random.randint(1, 3)
        print i
        time.sleep(t)
        driver.find_element_by_xpath("//*[@id='J-input-user']").send_keys(i)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='J-input-user']").send_keys(Keys.TAB)
    time.sleep(1)
    for p in passw:
        t2 = random.randint(1, 3)
        time.sleep(t2)
        driver.switch_to.active_element.send_keys(p)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@type='submit']").click()
    print "login success"
    # for u in usr:
    #     time.sleep(random.randint(1,4))
    #     driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(u)
    # for p in passw:
    #     time.sleep(random.randint(1,4))
    #     driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(p)
    #     time.sleep(2)
    #     driver.find_element_by_xpath('//*[@type="submit"]').click()
    time.sleep(2)
    js="var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    driver.maximize_window()
    print driver.current_window_handle
    driver.find_element_by_xpath('//*[@class="btn upload-file-btn"]').click()
    ##这里需要Windows系统的弹窗，需要安装使用spy++工具以及引入python（pywin32）库

    driver.switch_to.active_element.send_keys('E:\zxtest\la.png')
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    wenzi=driver.find_element_by_xpath('//*[@class="textbox-list"]').text
    print "wenzi:   "%wenzi
    json=driver.find_element_by_xpath('//*[@class="json-pretty"]').text
    print "json:   "%json








