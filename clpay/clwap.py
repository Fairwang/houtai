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
        self.driver.get('https://testpay.hongnaga.com/?debug=true')
        # self.driver.get('https://pay.hongnaga.com/?debug=true')
        time.sleep(3)
        a=self.driver.switch_to.alert
        a.send_keys("123456778")
        # a.send_keys("112233")
        a.accept()
        # self.driver.find_element_by_id('com.android.chrome:id/js_modal_dialog_prompt').send_keys('112233')
        # self.driver.find_element_by_id('android:id/button1').click()
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
            pay_type.select_by_value("6")#银联wap
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
            time.sleep(2)
            self.driver.find_element_by_id("pay").click()
            time.sleep(8)
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

            self.driver.find_element_by_id("btnSumbit").click()
            time.sleep(1)
            username=u"高攀"
            self.driver.find_element_by_id("username").send_keys(username)
            time.sleep(1)

            self.driver.find_element_by_name("idCardNo").send_keys("610481198608265032")
            time.sleep(1)

            self.driver.find_element_by_name("phone").send_keys("13772157150")
            time.sleep(1)

            self.driver.find_element_by_id("agree").click()
            time.sleep(1)

            self.driver.find_element_by_id("btnSumbit").click()
            time.sleep(6)
            #发送验证码，输入验证码
            self.driver.find_element_by_id("btnSumbit").click()






            if i == 1:
                time.sleep(60000)
            i = i + 1

    def tearDown(self):
        self.driver.quit()

# clpay = clpay_pay(driver)
# clpay.clpay()


if __name__=='__main__':
    unittest.main()

