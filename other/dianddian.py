#!/user/bin/python
#  -*-coding: utf-8-*-
from selenium import webdriver
#商户界面
driver=webdriver.Chrome()
driver.get('https://testpay.hongnaga.com/merchant/login.html')

driver.find_element_by_name("mch_id").send_keys("18365")
driver.find_element_by_name("password").send_keys("123456")
#验证码
driver.find_element_by_id("sub").click()
