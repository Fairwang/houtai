#!user/bin/python
# coding: utf-8
#正式赤龙 支付demo 发起支付 支付方式为商户代付
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

class clpay1():
    def __init__(self,driver):
        self.driver=driver
    def isElementExist(self,element):
        flag = True
        try:
            self.driver.find_element_by_link_text(element)
            return flag
        except:
            flag = False
            return flag
    def clpay(self):
        # self.driver=webdriver.Chrome()
        # self.driver.get('https://pay.hongnaga.com/?debug=true')

        # driver.get("http://pay.frp.tinywan.top/?debug=true")
        driver.get("https://testpay.hongnaga.com/?debug=true")
        # h=driver.current_window_handle
        # print h
        a=self.driver.switch_to.alert
        a.send_keys("123456778")
        a.accept()

        prices=[30,10,15,20]
        for price in prices:
            self.driver.implicitly_wait(2)
        #商户ID
            self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")

        # 支付方式
            pay_type=Select(self.driver.find_element_by_id("pay_type"))
            self.driver.find_element_by_id("pay_type").click()
            pay_type.select_by_value("11")  # 商户代付

        # 金额
            self.driver.find_element_by_name("price").clear()
            self.driver.find_element_by_name("price").send_keys(price)
        #代理商id
            self.driver.find_element_by_name("account_id").clear()
            self.driver.find_element_by_name("account_id").send_keys("201806")

        # 银行编码
            self.driver.find_element_by_xpath("//*[@name='bank_code']").clear()
            self.driver.find_element_by_xpath("//*[@name='bank_code']").send_keys("01050000")

        # 姓名
            self.driver.find_element_by_xpath("//*[@name='username']").clear()
            self.driver.find_element_by_xpath("//*[@name='username']").send_keys(u"付贵炉")#UnicodeDecodeError: 'utf8' codec can't decode byte 0xe4 in position 0: unexpected end of data
        # 银行卡号
            self.driver.find_element_by_xpath("//*[@name='card_no']").clear()
            self.driver.find_element_by_xpath("//*[@name='card_no']").send_keys("6217001540022416380")

            time.sleep(2)
            self.driver.find_element_by_id("pay").click()
            self.driver.implicitly_wait(5)
            time.sleep(1)

            windows = self.driver.window_handles#获取所有windows窗口句柄
            time.sleep(1)
            self.driver.switch_to.window(windows[0])#返回发起界面
            time.sleep(3)
            zf11="支付完成"
            clpay=clpay1(self.driver)
            if clpay.isElementExist(zf11):
                self.driver.find_element_by_link_text("支付完成").click()
            else:
                pass
            time.sleep(2)

driver=webdriver.Chrome()
daifu=clpay1(driver)
daifu.clpay()
time.sleep(1000)
