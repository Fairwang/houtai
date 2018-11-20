#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import MySQLdb

driver = webdriver.Chrome()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://cpay.hypayde.com/demo.html?debug=true")
a=driver.switch_to.alert
a.send_keys("112233")
a.accept()

time.sleep(2)
i = 1
for price in range(1,10):
    price = str(price)
    time.sleep(2)
    # driver.implicitly_wait(3)
    driver.find_element_by_name("mch_id").clear()
    driver.find_element_by_name("mch_id").send_keys(1015)
    driver.find_element_by_name("sub_mch_id").clear()
    # driver.find_element_by_name("sub_mch_id").send_keys(6020)
    pay_type=Select(driver.find_element_by_id("pay_type"))
    pay_type.select_by_value("9")#签约服务商当面付
    # pay_type.select_by_value("7")#支付宝当面付

    driver.find_element_by_name("price").clear()#金额
    driver.find_element_by_name("price").send_keys(price)
    driver.find_element_by_id("pay").click()
    print i
    i = i + 1
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    time.sleep(1)
    print driver.title
    if i > 10:
        time.sleep(1000)
        # driver.quit()
        print"success"
        break
