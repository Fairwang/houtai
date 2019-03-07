#! user/bin/env
# -*-coding:utf-8-*-
import unittest
import time
from selenium import webdriver


class qiehuan02(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfornVersion'] = '7.1.1'
        desired_caps['deviceName'] = '33d04c7c'
        desired_caps['noReset'] = 'true'
        # desired_caps['appActivity']='org.chromium.chrome.browser.ChromeTabbedActivity'

        desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
        desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_02(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='扫一扫']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='相册']").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "main":
    unittest.main()

