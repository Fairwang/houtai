#!user/bin/python
# coding:utf-8

# from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from appium import webdriver

#聚合支付自动化测试
# web端--点点支付demo界面——H5发起支付-掉起起支付宝
class C2Cwap(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'  # 测试的目标机器
        self.desired_caps['platfromVersion']='7.1.1'#目标设备的系统版本
        self.desired_caps['deviceName']='33d04c7c'#测试机器的名称（设备名称即可）
        # self.desired_caps['platfromVersion'] = '8.0.0'  # 目标设备的系统版本
        # self.desired_caps['deviceName'] = '73EBB18629223414'  # 测试机器的名称（设备名称即可）
        self.desired_caps['browserName'] = 'Chrome'
        self.desired_caps['noReset'] = 'true'
        # self.desired_caps['appPackage']='com.android.chrome'#被测应用的包名（只有Android测试才用）
        self.desired_caps['appActivity'] = 'org.chromium.chrome.browser.ChromeTabbedActivity'
        # self.desired_caps['unicodeKeyboard']='true'#支持中文输入，默认false
        # self.desired_caps['resetKeyboard'] = 'true'  # 重置输入法为系统默认
        self.desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def test_C2Cwap(self):
        self.driver.get('https://testpay.hongnaga.com/?debug=true')
        # self.driver.get('https://pay.hongnaga.com/?debug=true')
        a=self.driver.switch_to.alert
        a.send_keys("123456778")
        # a.send_keys("112233")
        a.accept()
        time.sleep(2)
        self.driver.tap([(523,1825)],890)#Method has not yet been implemented
        time.sleep(3)



    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
