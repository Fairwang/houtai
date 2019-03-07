#! user/bin/env
# -*-coding:utf-8-*-
import unittest
import time
from selenium import webdriver
class qiehuan01(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platfornVersion']='7.1.1'
        desired_caps['deviceName']='33d04c7c'
        desired_caps['browserName']='Chrome'
        desired_caps['noReset']='true'
        # desired_caps['appActivity']='org.chromium.chrome.browser.ChromeTabbedActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_01(self):
        self.driver.get("https://testpay.hongnaga.com/?debug=true")
        a=self.driver.switch_to.alert
        a=a.send_keys("112233")
        a.accept()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__=="main":
    unittest.main()
