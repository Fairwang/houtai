#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import MySQLdb
import random
driver = webdriver.Chrome()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("https://cpay.hypayde.com/demo.html?debug=true")
driver.get("http://newpay.shysrj.com:8085/demo.html?debug=true")
a=driver.switch_to.alert
a.send_keys("112233")
a.accept()

# time.sleep(2)
# i = 1
# f1 = open("E:\\zxtest\\ddpush.txt", 'r')
# lines = f1.readlines()      #读取全部内容 ，并以列表方式返回
# print lines
# for price in lines:
#     price=price[:-1]
i=1
while 1:
    price=random.randint(10,20)
    time.sleep(2)
    # driver.implicitly_wait(3)
    driver.find_element_by_name("mch_id").clear()
    driver.find_element_by_name("mch_id").send_keys(19001)
     # driver.find_element_by_name("sub_mch_id").send_keys(6020)#子商户号
    pay_type=Select(driver.find_element_by_id("pay_type"))
    # pay_type.select_by_value("9")#签约服务商当面付
    pay_type.select_by_value("7")#支付宝当面付
    # pay_type.select_by_value("11")  # 新支付宝wap支付
    driver.find_element_by_name("price").clear()#金额
    driver.find_element_by_name("price").send_keys(price)
    driver.find_element_by_id("pay").click()

    i = i + 1
    # windows = driver.window_handles
    # driver.switch_to.window(windows[0])
    time.sleep(2)
    # print driver.title
    if i > 12:
        time.sleep(1000)
        # driver.quit()
        print"success"
        break
