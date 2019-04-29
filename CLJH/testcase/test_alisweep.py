#! user/bin/env
# -*-coding:utf-8-*-

# 赤龙聚合 支付宝扫描相册中的二维码
import unittest
import time
import os
from selenium import webdriver
from appium import webdriver
import urllib3
urllib3.disable_warnings()

class saomiao(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platfornVersion']='7.1.1'
        desired_caps['deviceName']='33d04c7c'
        desired_caps['noReset']='true'
        desired_caps['appPackage']='com.eg.android.AlipayGphone'
        desired_caps['appActivity']='com.eg.android.AlipayGphone.AlipayLogin'
        time.sleep(10)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def test_saomiao(self):


        self.driver.find_element_by_xpath("//android.widget.TextView[@text='扫一扫']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='相册']").click()
        time.sleep(2)
        photos=self.driver.find_elements_by_class_name("android.widget.ImageView")
        print photos
        photos[0].click()#最新相册是第一张
        time.sleep(2)
        filename=str(int(time.strftime("%m%d%H%M%S",time.localtime())))
        filename = os.path.dirname(os.path.realpath(__file__)) + "\\picture\\" + filename + ".png"
        self.driver.save_screenshot(filename)
        self.driver.find_element_by_xpath("//android.widget.Button[@text='下一步']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.Button[@text='确认转账']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='立即付款']").click()
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        self.driver.find_element_by_xpath("//android.widget.Button[@text='确认转账']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='立即付款']").click()
        time.sleep(1)
        self.driver.tap([(140*x/1080,1500*y/1920)],0)
        time.sleep(1)
        self.driver.tap([(200*x/1080,1500*y/1920)],0)
        time.sleep(1)
        self.driver.tap([(800*x/1080,1500*y/1920)],0)
        time.sleep(1)
        self.driver.tap([(800*x/1080,1500*y/1920)],0)
        time.sleep(1)
        self.driver.tap([(500*x/1080,1680*y/1920)],0)
        time.sleep(1)
        self.driver.tap([(500*x/1080,1680*y/1920)],0)
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()
    def tearDown(self):
        self.driver.quit()
#
if __name__=='main':
    unittest.main()