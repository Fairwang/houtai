#!user/bin/python
# coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from houtai.lk import cpay_database
#将数据库中expire_time>0,改为等于0
#支付demo界面:输入密码成功登录后，输入主商户号、子商户号，选择支付方式，输入金额，点击提交
#从diandian_pay.txt中取出金额，传入金额

sql="update cl_merchant_qrcode set expire_time=0 where mch_id=1006 and expire_time>0 order by price desc"

cpay_database.query_database(sql)

driver=webdriver.Chrome()
# driver.get("https://cpay.hypayde.com/index/demo/index.html?debug=true")
driver.get("http://cpaytest.tinywan.com/index/demo/index.html?debug=true")

a=driver.switch_to.alert
a.send_keys("112233")
a.accept()

i=0
# f1 = open("D:\\zxtest\\diandian_pay.txt", 'r')
while True:
    # price = f1.readline()
    # if price=='':
    #     break
    time.sleep(3)
    driver.implicitly_wait(3)
    driver.find_element_by_name("mch_id").clear()
    driver.find_element_by_name("mch_id").send_keys(1006)
    driver.find_element_by_name("sub_mch_id").clear()
    driver.find_element_by_name("sub_mch_id").send_keys(6009)

    pay_type=Select(driver.find_element_by_id("pay_type"))
    pay_type.select_by_value("5")

    driver.find_element_by_name("price").clear()#金额
    driver.find_element_by_name("price").send_keys(50)

    driver.find_element_by_id("pay").click()

    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    print i
    i=i+1
    # time.sleep(5)

