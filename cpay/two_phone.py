#!/user/bin/python
#  -*-coding: utf-8-*-
import time
import unittest
from selenium.webdriver.common.by import By
from appium import webdriver
import time
import threading


class zhifubao(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platfromVersion'] = '7.1.1'
        self.desired_caps['deviceName'] = '33d04c7c'
        self.desired_caps['udid']='33d04c7c'
        self.desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
        self.desired_caps['automationName'] = 'uiautomator2'  ##############
        self.desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
        self.desired_caps['noReset'] = True
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.desired_caps6 = {}  #华为NO.9
        self.desired_caps6['platformName'] = 'Android'
        self.desired_caps6['platfromVersion'] = '8.0.0'
        self.desired_caps6['deviceName'] = '73EBB18629223414'
        self.desired_caps6['udid']='73EBB18629223414'
        self.desired_caps6['appPackage'] = 'com.eg.android.AlipayGphone'
        self.desired_caps6['automationName'] = 'uiautomator2'  ##############
        self.desired_caps6['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
        self.desired_caps6['noReset'] = True

    def task1(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
        time.sleep(1)
    
    
    def task2(self):
        driver = webdriver.Remote('http://localhost:4725/wd/hub', self.desired_caps6)
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
        time.sleep(1)

    def test_task(self):
        threads = []
        task11=self.task1()
        t1 = threading.Thread(target=task11)
        threads.append(t1)
        task22 = self.task2()
        t2 = threading.Thread(target=task22)
        threads.append(t2)
        for t in threads:
            t.start()

if __name__ == '__main__':
    unittest.main()