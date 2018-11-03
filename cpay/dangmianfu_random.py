#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import MySQLdb
import random

driver = webdriver.Chrome()
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://cpay.hypayde.com/demo.html?debug=true")
a = driver.switch_to.alert
a.send_keys("112233")
a.accept()

time.sleep(3)
i = 1
# f1 = open("D:\\zxtest\\diandian_pay.txt", 'r')
while True:
    # price = f1.readline()
    # if price=='':
    #     break
    # for price in random.randint(50,500):
    #     price = str(price)
    price = random.randint(50, 500)
    time.sleep(3)
    driver.implicitly_wait(3)
    driver.find_element_by_name("mch_id").clear()
    driver.find_element_by_name("mch_id").send_keys(1006)
    driver.find_element_by_name("sub_mch_id").clear()
    driver.find_element_by_name("sub_mch_id").send_keys(6020)
    pay_type = Select(driver.find_element_by_id("pay_type"))
    # pay_type.select_by_value("5")#app转账
    pay_type.select_by_value("7")  # 支付宝当面付
    # pay_type.select_by_value("2")#支付宝转账
    # pay_type.select_by_value("3")#支付宝转账查询
    # pay_type.select_by_value("1")#支付宝支付PC
    # pay_type.select_by_value("4")#支付宝支付wap
    # pay_type.select_by_value("6")#微信转账

    driver.find_element_by_name("price").clear()  # 金额
    driver.find_element_by_name("price").send_keys(price)
    driver.find_element_by_id("pay").click()
    print i
    i = i + 1
    # windows = driver.window_handles
    # driver.switch_to.window(windows[0])
    time.sleep(3)
    print driver.title
    if i > 20:
        driver.quit()
        print"success"
        break
