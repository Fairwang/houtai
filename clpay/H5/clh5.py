#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from appium import webdriver
#支付demo界面
class clh5(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'#测试的目标机器
        desired_caps['platfromVersion']='7.1.1'#目标设备的系统版本
        desired_caps['deviceName']='33d04c7c'#测试机器的名称（设备名称即可）
        desired_caps['browserName']='Chrome'
        desired_caps['noReset']='true'
        desired_caps['appPackage']='com.android.chrome'#被测应用的包名（只有Android测试才用）
        desired_caps['appActivity']='org.chromium.chrome.browser.ChromeTabbedActivity'
        desired_caps['unicodeKeyboard']='true'#支持中文输入，默认false
        desired_caps['resetKeyboard'] = 'true'  # 重置输入法为系统默认
        desired_caps['noReset']='true'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def test_h5(self):
        time.sleep(5)
        # self.driver.get('https://testpay.hongnaga.com/?debug=true')
        self.driver.get('https://pay.hongnaga.com/?debug=true')
        time.sleep(3)
        a=self.driver.switch_to.alert
        # a.send_keys("123456778")
        a.send_keys("112233")
        a.accept()
        # self.driver.find_element_by_id('com.android.chrome:id/js_modal_dialog_prompt').send_keys('112233')
        # self.driver.find_element_by_id('android:id/button1').click()
        time.sleep(2)
        lines = [80,60, 102]
        i = 1
        for price in lines:
            print  price
            # 商户ID
            self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")
            # 支付方式
            pay_type = Select(self.driver.find_element_by_id("pay_type"))
            self.driver.find_element_by_id("pay_type").click()
            # pay_type.select_by_value("13")#新支付宝转账
            pay_type.select_by_value("5")#支付宝h5
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
            time.sleep(60)
            if i == 3:
                time.sleep(60000)
            i = i + 1

    def tearDown(self):
        self.driver.quit()

# clpay = clpay_pay(driver)
# clpay.clpay()


if __name__=='__main__':
    unittest.main()

