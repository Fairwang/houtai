#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
#支付demo界面


class LoginTestjiandian(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platfromVersion']='7.1.1'
        desired_caps['deviceName']='33d04c7c'
        desired_caps['appPackage']='com.android.chrome'
        desired_caps['appActivity']='org.chromium.chrome.browser.ChromeTabbedActivity'



        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(3)

    def test_h5(self):
        driver = webdriver.Chrome()
        driver.get('https://pay.hongnaga.com/?debug=true')
        a=self.driver.switch_to.alert

        a.send_keys("112233")
        a.accept()
        clpay = clpay_pay(driver)
        clpay.clpay()

    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()

class clpay_pay():
    def __init__(self,driver):
        self.driver=driver
    def isElementExist(self,element):
        flag = True
        try:
            self.driver.find_element_by_link_text(element)
            return flag
        except:
            print "none"
            flag = False
            return flag
    def clpay(self):
        # driver=webdriver.Chrome()

        self.driver.get('https://pay.hongnaga.com/?debug=true')
        # driver.get("https://pay.sunspay.com/?debug=true")
        # driver.get("https://pay.hongnaga.com/?debug=true")
        a=self.driver.switch_to.alert
        # a.send_keys("123456778")
        a.send_keys("112233")
        a.accept()
        # f1 = open("E:\\zxtest\\ddpush.txt", 'r')
        # lines = f1.readlines()  # 读取全部内容 ，并以列表方式返回
        # print lines
        lines=[1]
        i=1
        for price in lines:
            # price = price[:-1]
        # for i in range(10,30):
            print  price
            self.driver.implicitly_wait(2)
        #商户ID
            self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")

        # 支付方式
            pay_type=Select(self.driver.find_element_by_id("pay_type"))
            self.driver.find_element_by_id("pay_type").click()
            # pay_type.select_by_value("13")#新支付宝转账
            # pay_type.select_by_value("5")#支付宝h5
            # pay_type.select_by_value("1")  # 网银支付
            # pay_type.select_by_value("15")  # 支付宝扫码
            # pay_type.select_by_value("17")  # 支付宝wap
            # pay_type.select_by_value("11")  # 商户代付
            pay_type.select_by_value("3")  # QQ扫码
            # pay_type.select_by_value("16")  # 微信扫码
        # 金额
            self.driver.find_element_by_name("price").clear()#
            self.driver.find_element_by_name("price").send_keys(price)

        # 银行编码
            self.driver.find_element_by_xpath("//*[@name='bank_code']").clear()
            # driver.find_element_by_xpath("//*[@name='bank_code']").send_keys("01050000")

        # 姓名
            # driver.find_element_by_xpath("//*[@name='username']").clear()
            # driver.find_element_by_xpath("//*[@name='username']").send_keys("付贵炉")
        # 银行卡号
            # driver.find_element_by_xpath("//*[@name='card_no']").clear()
            # driver.find_element_by_xpath("//*[@name='card_no']").send_keys("6217001540022416380")

            time.sleep(2)
            self.driver.find_element_by_id("pay").click()
            self.driver.implicitly_wait(5)
            time.sleep(1)

            windows = self.driver.window_handles
            time.sleep(1)
            self.driver.switch_to.window(windows[0])
            time.sleep(1)
            zf11="支付完成"
            clpay=clpay_pay(self.driver)
            if clpay.isElementExist(zf11):
                print "yes"
                self.driver.find_element_by_link_text("支付完成").click()
                time.sleep(1)
            else:
                pass
            time.sleep(3)
            if i==1:
                time.sleep(60000)
            i=i+1

