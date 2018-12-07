#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from appium import webdriver
#支付demo界面


class LoginTestjiandian(unittest.TestCase):
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
        lines = [110, 120, 100]
        i = 1
        for price in lines:
            # price = price[:-1]#从文本中取出后删除其\n标志
            # for i in range(10,30):
            print  price
            # 商户ID
            self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")

            # 支付方式
            pay_type = Select(self.driver.find_element_by_id("pay_type"))
            self.driver.find_element_by_id("pay_type").click()
            # pay_type.select_by_value("13")#新支付宝转账
            pay_type.select_by_value("5")#支付宝h5
            # pay_type.select_by_value("1")  # 网银支付
            # pay_type.select_by_value("15")  # 支付宝扫码
            # pay_type.select_by_value("17")  # 支付宝wap
            # pay_type.select_by_value("11")  # 商户代付
            # pay_type.select_by_value("3")  # QQ扫码
            # pay_type.select_by_value("16")  # 微信扫码
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
            time.sleep(100)

            if i == 3:
                time.sleep(60000)
            i = i + 1

    # self.driver.switch_to.alert.send_keys("112233").accept()

    # clpay = clpay_pay(driver)
    # clpay.clpay()


    def tearDown(self):
        self.driver.quit()

# clpay = clpay_pay(driver)
# clpay.clpay()


if __name__=='__main__':
    unittest.main()

# class clpay_pay():
#     def __init__(self,driver):
#         self.driver=driver
#     def isElementExist(self,element):
#         flag = True
#         try:
#             self.driver.find_element_by_link_text(element)
#             return flag
#         except:
#             print "none"
#             flag = False
#             return flag
#     def clpay(self):
#         # driver=webdriver.Chrome()
#
#         self.driver.get('https://pay.hongnaga.com/?debug=true')
#         # driver.get("https://pay.sunspay.com/?debug=true")
#         # driver.get("https://pay.hongnaga.com/?debug=true")
#         a=self.driver.switch_to.alert
#         # a.send_keys("123456778")
#         a.send_keys("112233")
#         a.accept()
#         # f1 = open("E:\\zxtest\\ddpush.txt", 'r')
#         # lines = f1.readlines()  # 读取全部内容 ，并以列表方式返回
#         # print lines
#         lines=[1]
#         i=1
#         for price in lines:
#             # price = price[:-1]
#         # for i in range(10,30):
#             print  price
#             self.driver.implicitly_wait(2)
#         #商户ID
#             self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
#             self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")
#
#         # 支付方式
#             pay_type=Select(self.driver.find_element_by_id("pay_type"))
#             self.driver.find_element_by_id("pay_type").click()
#             # pay_type.select_by_value("13")#新支付宝转账
#             # pay_type.select_by_value("5")#支付宝h5
#             # pay_type.select_by_value("1")  # 网银支付
#             # pay_type.select_by_value("15")  # 支付宝扫码
#             # pay_type.select_by_value("17")  # 支付宝wap
#             # pay_type.select_by_value("11")  # 商户代付
#             pay_type.select_by_value("3")  # QQ扫码
#             # pay_type.select_by_value("16")  # 微信扫码
#         # 金额
#             self.driver.find_element_by_name("price").clear()#
#             self.driver.find_element_by_name("price").send_keys(price)
#
#         # 银行编码
#             self.driver.find_element_by_xpath("//*[@name='bank_code']").clear()
#             # driver.find_element_by_xpath("//*[@name='bank_code']").send_keys("01050000")
#
#         # 姓名
#             # driver.find_element_by_xpath("//*[@name='username']").clear()
#             # driver.find_element_by_xpath("//*[@name='username']").send_keys("付贵炉")
#         # 银行卡号
#             # driver.find_element_by_xpath("//*[@name='card_no']").clear()
#             # driver.find_element_by_xpath("//*[@name='card_no']").send_keys("6217001540022416380")
#
#             time.sleep(2)
#             self.driver.find_element_by_id("pay").click()
#             self.driver.implicitly_wait(5)
#             time.sleep(1)
#
#             windows = self.driver.window_handles
#             time.sleep(1)
#             self.driver.switch_to.window(windows[0])
#             time.sleep(1)
#             zf11="支付完成"
#             clpay=clpay_pay(self.driver)
#             if clpay.isElementExist(zf11):
#                 print "yes"
#                 self.driver.find_element_by_link_text("支付完成").click()
#                 time.sleep(1)
#             else:
#                 pass
#             time.sleep(3)
#             if i==1:
#                 time.sleep(60000)
#             i=i+1
#
