#! user/bin/env
# -*-coding:utf-8-*-

# 赤龙聚合 点点银行卡支付
import unittest
import time
from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select
import os
from appium import webdriver

class JHWENDING(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platfornVersion']='7.1.1'
        desired_caps['deviceName']='33d04c7c'
        desired_caps['browserName']='Chrome'
        desired_caps['noReset']='true'
        # desired_caps['appActivity']='org.chromium.chrome.browser.ChromeTabbedActivity'

        desired_caps['appPackage']='com.eg.android.AlipayGphone'
        desired_caps['appActivity']='com.eg.android.AlipayGphone.AlipayLogin'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def test_JHWENDING(self):
        time.sleep(2)
        self.driver.get("https://pay.hongnaga.com/?debug=true")
        time.sleep(2)
        a=self.driver.switch_to.alert
        a.send_keys("112233")
        a.accept()
        time.sleep(2)

        price=random.randint(1,10)
        # 商户ID
        self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
        self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")
        # 支付方式
        pay_type = Select(self.driver.find_element_by_id("pay_type"))
        self.driver.find_element_by_id("pay_type").click()
        # pay_type.select_by_value("13")#新支付宝转账
        pay_type.select_by_value("5")  # 支付宝H5
        # pay_type.select_by_value("7")  # 微信H5
        # pay_type.select_by_value("17")  # 支付宝wap
        # pay_type.select_by_value("11")  # 商户代付

        # 金额
        self.driver.find_element_by_name("price").clear()  #
        self.driver.find_element_by_name("price").send_keys(price)
        # 银行编码
        # self.driver.find_element_by_xpath("//*[@name='bank_code']").clear()
        # driver.find_element_by_xpath("//*[@name='bank_code']").send_keys("01050000")
        # 姓名
        # driver.find_element_by_xpath("//*[@name='username']").clear()
        # driver.find_element_by_xpath("//*[@name='username']").send_keys("付贵炉")
        # 银行卡号
        # driver.find_element_by_xpath("//*[@name='card_no']").clear()
        # driver.find_element_by_xpath("//*[@name='card_no']").send_keys("6217001540022416380")
        # time.sleep(2)
        self.driver.find_element_by_id("pay").click()
        time.sleep(2)
        # self.driver.background_app(100)
        b=self.driver.switch_to.alert
        b.accept()

        time.sleep(2)
        c=self.driver.switch_to.alert
        c.dismiss()
        print self.driver.current_activity
        adb="adb shell screencap -p /sdcard/fb01.png"
        os.system(adb)
        time.sleep(2)
        self.driver.launch_app('com.eg.android.AlipayGphone','com.eg.android.AlipayGphone.AlipayLogin')  #start_activity(package,activity)  窗口句柄还停留在chrome页面
        time.sleep(2)
        print self.driver.current_activity
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='扫一扫']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='相册']").click()
        time.sleep(2)
        photos=self.driver.find_elements_by_id("com.alipay.mobile.beehive:id/iv_photo")
        time.sleep(2)
        photos[-1].click()
        time.sleep(2)
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

if __name__=='main':
    unittest.main()