#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
#支付demo界面

driver=webdriver.Chrome()

driver.get("https://auth.alipay.com/login/index.htm?bizFrom=mrchportal&goto=https%3A%2F%2Fenterpriseportal.alipay.com%2Findex.htm")
time.sleep(5)
driver.find_element_by_tag_name("账密登录").click()
time.sleep(5)
driver.find_element_by_name("logonId").send_keys("chilongzhifu@hongnaga.com")
driver.find_element_by_id("UA_InputId").send_keys("chilong123.")
driver.find_element_by_id("J-login-btn") .click()
# time.sleep(1)
# a.accept()
# f1 = open("D:\\zxtest\\diandian_pay.txt", 'r')
# while True:
#     print "stast"
#     price = f1.readline()
#     print price
#     if price=='':
#         break
#     # print  i
#     driver.implicitly_wait(2)
#     driver.find_element_by_name("mch_id").clear()
#     driver.find_element_by_name("mch_id").send_keys(1006)
#     driver.find_element_by_name("sub_mch_id").clear()
#     driver.find_element_by_name("sub_mch_id").send_keys(6009)
#
#     pay_type=Select(driver.find_element_by_id("pay_type"))
#     # driver.find_element_by_id("pay_type").click()
#     pay_type.select_by_value("5")
#     driver.implicitly_wait(5)
#
#     driver.find_element_by_name("price").clear()#金额
#     driver.find_element_by_name("price").send_keys(price)
#     time.sleep(2)
#     driver.find_element_by_id("pay").click()
#     time.sleep(1)
#     print"yes"
#     windows = driver.window_handles
#     time.sleep(1)
#     driver.switch_to.window(windows[0])
#     time.sleep(1)

