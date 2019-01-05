#!user/bin/python
# coding:utf-8
from selenium import webdriver
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

        lines = [12]
        i = 1
        handles = self.driver.window_handles
        print handles
        for price in lines:
            print  price
            # 商户ID
            # self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            # self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")
            # 支付方式
            pay_type = Select(self.driver.find_element_by_id("pay_type"))
            self.driver.find_element_by_id("pay_type").click()
            # pay_type.select_by_value("11")  # 支付宝wap
            pay_type.select_by_value("5")  # 支付宝wap
            # 金额
            self.driver.find_element_by_name("price").clear()  #
            self.driver.find_element_by_name("price").send_keys(price)
            # time.sleep(2)
            # self.driver.hide_keyboard()# The software keyboard cannot be closed

            # 银行编码
            self.driver.find_element_by_xpath("//*[@name='bank_code']").clear()
            self.driver.find_element_by_xpath("//*[@name='bank_code']").send_keys("01050000")
            # 姓名
            self.driver.find_element_by_xpath("//*[@name='username']").clear()
            self.driver.find_element_by_xpath("//*[@name='username']").send_keys(u"付贵炉")
            # 银行卡号
            self.driver.find_element_by_xpath("//*[@name='card_no']").clear()
            self.driver.find_element_by_xpath("//*[@name='card_no']").send_keys("6217001540022416380")
            # time.sleep(2)
            time.sleep(2)
            # a=self.driver.find_element_by_id("pay")
            # print a
            self.driver.find_element_by_id("pay").click() #点击了但是没有得到相应的效果
            time.sleep(10)
            windows=self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
            time.sleep(2)

            # 唤起支付宝App
            self.driver.find_element_by_link_text(u"使用支付宝App支付").click()
            time.sleep(8)
            self.driver.tap([(145,1536),(225,1596)])
            # self.driver.tap(185, 1558)
            time.sleep(8)
            self.driver.current_activity()#无法切换到支付宝界面

            time.sleep(2)
            self.driver.find_element_by_link_text(u"立即付款").click()

            if i == 1:
                time.sleep(60000)
            i = i + 1

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

