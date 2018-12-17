#!/user/bin/python
#  -*-coding: utf-8-*-
import unittest
from appium import webdriver
import time
import random


class zhifubao(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfromVersion'] = '7.1.1'
        desired_caps['deviceName'] = '33d04c7c'
        # desired_caps['platfromVersion']='7.1.2'#红米5A
        # desired_caps['deviceName']='79bad8ec7d94'
        desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
        desired_caps['automationName'] = 'uiautomator2'  ##############
        desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
        desired_caps['noReset']=True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_zhifubao(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='换个账号登录']").click()
        time.sleep(3)
        username="15868314566"
        # for u in username:
        #     t1=random.randint(1,10)
        #     time.sleep(t1)
        #     self.driver.find_element_by_id("com.ali.user.mobile.security.ui:id/content").send_keys(Keys.NUMPAD1)
        #     # self.driver.switch_to.active_element.send_keys(u)
        self.driver.find_element_by_id("com.ali.user.mobile.security.ui:id/content").send_keys(username)
        time.sleep(3)
        self.driver.find_element_by_id("com.ali.user.mobile.security.ui:id/nextButton").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='换个方式登录']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='密码登录']").click()
        time.sleep(5)
        password="ymxx158"
        x=1080
        y=1920
        self.driver.tap([(593.5*x/1080, 1344.3*y/1920)], 0)
        time.sleep(2)

        # self.driver.hide_keyboard()
        for p in password:
            t=random.randint(1,10)
            time.sleep(t)
            self.driver.switch_to.active_element.send_keys(p)

        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()


    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

