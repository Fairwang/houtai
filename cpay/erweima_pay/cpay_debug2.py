#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
#支付demo界面:输入密码成功登录后，输入主商户号、子商户号，选择支付方式，输入金额，点击提交


driver = webdriver.Chrome()
# driver.get("http://wangcpay.tinywan.top/demo.html?debug=true")
driver.get("https://cpay.hypayde.com/demo.html?debug=true")
a=driver.switch_to.alert
a.send_keys("112233")
# a.send_keys("123456778")
a.accept()


i = 1
# f1 = open("D:\\zxtest\\diandian_pay.txt", 'r')
# while True:
    # price = f1.readline()
    # if price=='':
    #     break
prices=[1,1.01,2,25,15]
for price in prices:
    price = str(price)
    time.sleep(3)
    driver.implicitly_wait(3)
    driver.find_element_by_name("mch_id").clear()
    driver.find_element_by_name("mch_id").send_keys(1035)
    # driver.find_element_by_name("sub_mch_id").clear()
    # driver.find_element_by_name("sub_mch_id").send_keys(6020)
    pay_type=Select(driver.find_element_by_id("pay_type"))
    pay_type.select_by_value("11")
    driver.find_element_by_name("price").clear()#金额
    driver.find_element_by_name("price").send_keys(price)
    driver.find_element_by_id("pay").click()
    print i
    i = i + 1
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    driver.switch_to.window(windows[0])
    # time.sleep()
    print driver.title
    if i > len(prices):
        # driver.quit()
        time.sleep(10)
        print"success"
        break
