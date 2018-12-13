#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from appium import webdriver
#手机端--支付demo界面--赤龙--支付宝wap——C2C
class C2Cwap(unittest.TestCase):
    def setUp(self):
        self.desired_caps={}
        self.desired_caps['platformName']='Android'#测试的目标机器
        self.desired_caps['platfromVersion']='7.1.1'#目标设备的系统版本
        self.desired_caps['deviceName']='33d04c7c'#测试机器的名称（设备名称即可）
        self.desired_caps['browserName']='Chrome'
        self.desired_caps['noReset']='true'
        self.desired_caps['appPackage']='com.android.chrome'#被测应用的包名（只有Android测试才用）
        self.desired_caps['appActivity']='org.chromium.chrome.browser.ChromeTabbedActivity'
        self.desired_caps['unicodeKeyboard']='true'#支持中文输入，默认false
        self.desired_caps['resetKeyboard'] = 'true'  # 重置输入法为系统默认
        self.desired_caps['noReset']='true'
        self.desired_caps2 = {}
        self.desired_caps2['platformName'] = 'Android'
        self.desired_caps2['platfromVersion'] = '7.1.1'
        self.desired_caps2['deviceName'] = '33d04c7c'
        self.desired_caps2['udid'] = '33d04c7c'
        self.desired_caps2['appPackage'] = 'com.eg.android.AlipayGphone'
        self.desired_caps2['automationName'] = 'uiautomator2'  ##############
        self.desired_caps2['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
        self.desired_caps2['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps2)

    def test_C2Cwap(self):
        time.sleep(10)
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)
        time.sleep(5)
        # self.driver.get('https://testpay.hongnaga.com/?debug=true')
        self.driver.get('https://pay.hongnaga.com/?debug=true')
        time.sleep(3)
        a=self.driver.switch_to.alert
        # a.send_keys("123456778")
        a.send_keys("112233")
        a.accept()
        time.sleep(2)

        lines = [12]
        i = 1
        handles = self.driver.window_handles
        print handles
        for price in lines:
            print  price
            # 商户ID
            self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")
            # 支付方式
            pay_type = Select(self.driver.find_element_by_id("pay_type"))
            self.driver.find_element_by_id("pay_type").click()
            pay_type.select_by_value("17")#支付宝wap
            # 金额
            self.driver.find_element_by_name("price").clear()  #
            self.driver.find_element_by_name("price").send_keys(price)
            time.sleep(2)
            self.driver.find_element_by_id("pay").click()
            time.sleep(8)
            #唤起支付宝App



            self.driver.start_activity("com.kuaihuoyun.freight", ".KDLaunch")

            windows=self.driver.window_handles
            print windows  #[u'CDwindow-0', u'CDwindow-1']
            current=self.driver.current_window_handle
            time.sleep(1)
            print current
            for faster in windows:
                if faster !=current:

            # self.driver.switch_to.window(current)
                    self.driver.switch_to.window(faster)  # 返回发起界面
            print "yes"
            time.sleep(1)
            self.driver.find_element_by_class_name("uns_btn").click()
            # self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/p[2]").click()
            # self.driver.find_element_by_xpath("//*[@class_name='uns_btn']").click()
            time.sleep(1)
            self.driver.find_element_by_id("IDcard").send_keys("6228480218885139970")#卡号
            time.sleep(1)

            self.driver.find_element_by_id("btnSubmit").click()
            time.sleep(1)
            username=u"高攀"
            self.driver.find_element_by_id("username").send_keys(username)
            time.sleep(1)

            self.driver.find_element_by_name("idCardNo").send_keys("610481198608265032")
            time.sleep(1)

            self.driver.find_element_by_id("phone").send_keys("13772157150")
            time.sleep(1)

            self.driver.find_element_by_id("agree").click()
            time.sleep(1)

            self.driver.find_element_by_id("btnSubmit").click()
            time.sleep(6)
            #发送验证码，输入验证码
            self.driver.find_element_by_id("btnSubmit").click()


            if i == 1:
                time.sleep(60000)
            i = i + 1

    def tearDown(self):
        self.driver.quit()

# clpay = clpay_pay(driver)
# clpay.clpay()


if __name__=='__main__':
    unittest.main()

