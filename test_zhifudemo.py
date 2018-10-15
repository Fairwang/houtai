#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
#支付demo界面
def isElementExist(element):
    flag = True
    # driver = self.driver
    try:
        driver.find_element_by_link_text(element)
        return flag
    except:
        flag = False
        return flag
driver=webdriver.Chrome()
driver.get('https://pay.hongnaga.com/?debug=true')
# h=driver.current_window_handle
# print h
# driver.maximize_window()
a=driver.switch_to.alert
a.send_keys("112233")
# time.sleep(1)
a.accept()
for i in range(1,11):
    print  i
    driver.implicitly_wait(2)
    pay_type=Select(driver.find_element_by_id("pay_type"))
    driver.find_element_by_id("pay_type").click()
    pay_type.select_by_value("13")
    # driver.implicitly_wait(5)
    driver.find_element_by_name("price").clear()#金额
    driver.find_element_by_name("price").send_keys("0.01")
    time.sleep(2)
    driver.find_element_by_id("pay").click()
    driver.implicitly_wait(5)
    time.sleep(1)
    windows = driver.window_handles
    time.sleep(1)
    driver.switch_to.window(windows[0])
    time.sleep(1)
    zf11="支付完成"
    if isElementExist(zf11):
        driver.find_element_by_link_text("支付完成").click()
    else:
        pass



