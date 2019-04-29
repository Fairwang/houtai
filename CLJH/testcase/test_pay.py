#! user/bin/env
# -*-coding:utf-8-*-
#  赤龙聚合
#  支付宝H5 提交订单后，截图保存
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
from appium import webdriver
import urllib3
urllib3.disable_warnings()

class JHWENDING(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platfornVersion']='7.1.1'
        desired_caps['deviceName']='33d04c7c'
        desired_caps['browserName']='Chrome'
        desired_caps['noReset']='true'
        # desired_caps['appActivity']='org.chromium.chrome.browser.ChromeTabbedActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def test_pay(self):
            # time.sleep(2)
            self.driver.get("https://www.herbeauty.top/Home_Index_test.html?debug=true")
            # time.sleep(2)
            # a=self.driver.switch_to.alert
            # a.send_keys("112233")
            # a.accept()
            time.sleep(5)

            # price=random.randint(10,30)
            # 商户ID
            # self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            # self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")
            # 支付方式
            pay_type = Select(self.driver.find_element_by_id("pay_type"))
            self.driver.find_element_by_id("pay_type").click()
            time.sleep(1)
            pay_type.select_by_value("904")  # 支付宝H5
            # 金额
            # self.driver.find_element_by_name("price").clear()
            # self.driver.find_element_by_name("price").send_keys(price)
            time.sleep(1)
            self.driver.find_element_by_id("pay").click()
            time.sleep(1)
            # self.driver.background_app(100)
            print self.driver.current_activity
            adb="adb shell screencap -p /sdcard/fb01.png"
            os.system(adb)
            time.sleep(1)



    def tearDown(self):
        self.driver.quit()

if __name__=='main':
    unittest.main()




