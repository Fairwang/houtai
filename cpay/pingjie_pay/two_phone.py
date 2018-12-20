#!/user/bin/python
#  -*-coding: utf-8-*-
import unittest
import time
from selenium.webdriver.common.by import By
from appium import webdriver
import time
import sys
from houtai.common import iselementexist
import threading

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platfromVersion'] = '7.1.1'
desired_caps['deviceName'] = '192.168.1.118:5557'
# desired_caps['deviceName'] = '33d04c7c'
desired_caps['udid'] = '192.168.1.118:5557'  # 坚果pro
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps['automationName'] = 'uiautomator2'  ##############
desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
desired_caps['noReset'] = True

desired_caps6 = {}
desired_caps6['platformName'] = 'Android'
# desired_caps6['platfromVersion'] = '8.0.0'
# desired_caps6['deviceName'] = '73EBB18629223414'#华为9
desired_caps6['platfromVersion'] = '8.0.0'
desired_caps6['deviceName'] = '192.168.1.152:5555'
desired_caps6['udid'] = '192.168.1.152:5555'
# desired_caps6['udid']='73EBB18629223414'
desired_caps6['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps6['automationName'] = 'uiautomator2'  ##############
desired_caps6['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
desired_caps6['noReset'] = True

def task1():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # time.sleep(3
    driver.find_element_by_xpath("//android.widget.TextView[@text='扫一扫']").click()
    # driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
    time.sleep(10)
    # driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
    time.sleep(1)


def task2():

    driver1 = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps6)
    # driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
    driver1.find_element_by_xpath("//android.widget.TextView[@text='扫一扫']").click()##这条执行时，未找到该元素，但只有task2运行时，可以找到钙元素
    time.sleep(3)
    # driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
    time.sleep(1)


threads = []
t1 = threading.Thread(target=task1)
threads.append(t1)

t2 = threading.Thread(target=task2)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        # time.sleep(2)
        t.start()


























#
# class zhifubao(unittest.TestCase):
#     def setUp(self):
#         self.desired_caps = {}
#         self.desired_caps['platformName'] = 'Android'
#         self.desired_caps['platfromVersion'] = '7.1.1'
#         self.desired_caps['deviceName'] = '33d04c7c'
#         self.desired_caps['udid']='33d04c7c'
#         self.desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
#         self.desired_caps['automationName'] = 'uiautomator2'  ##############
#         self.desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
#         self.desired_caps['noReset'] = True
#         # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
#         self.desired_caps6 = {}  #华为NO.9
#         self.desired_caps6['platformName'] = 'Android'
#         self.desired_caps6['platfromVersion'] = '8.0.0'
#         self.desired_caps6['deviceName'] = '73EBB18629223414'
#         self.desired_caps6['udid']='73EBB18629223414'
#         self.desired_caps6['appPackage'] = 'com.eg.android.AlipayGphone'
#         self.desired_caps6['automationName'] = 'uiautomator2'  ##############
#         self.desired_caps6['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
#         self.desired_caps6['noReset'] = True
#
#     def task1(self):
#         driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
#         time.sleep(3)
#         driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
#         time.sleep(3)
#         driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
#         time.sleep(1)
#
#
#     def task2(self):
#         driver = webdriver.Remote('http://localhost:4725/wd/hub', self.desired_caps6)
#         time.sleep(3)
#         driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
#         time.sleep(3)
#         driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
#         time.sleep(1)
#
#     def test_task(self):
#         threads = []
#         task11=self.task1()
#         t1 = threading.Thread(target=task11)
#         threads.append(t1)
#         task22 = self.task2()
#         t2 = threading.Thread(target=task22)
#         threads.append(t2)
#         for t in threads:
#             t.start()
#
# if __name__ == '__main__':
#     unittest.main()