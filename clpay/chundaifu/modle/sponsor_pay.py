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
    def clpay(self,account_id,bank_code,bank_name,username,card_no):
        # self.driver=webdriver.Chrome()
        # self.driver.get('https://pay.hongnaga.com/?debug=true')

        # driver.get("http://pay.frp.tinywan.top/?debug=true")
        driver.get("https://testpay.hongnaga.com/?debug=true")
        # h=driver.current_window_handle
        # print h
        a=self.driver.switch_to.alert
        a.send_keys("123456778")
        a.accept()
        prices=[]
        for i in range(200):
            if i%6==0:
                prices.append(i)
        print prices
        i=0
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
            self.driver.find_element_by_name("account_id").send_keys(account_id)
        # 银行编码
            self.driver.find_element_by_xpath("//*[@name='bank_code']").clear()
            self.driver.find_element_by_xpath("//*[@name='bank_code']").send_keys(bank_code)
            # 银行信息
            self.driver.find_element_by_xpath("//*[@name='bank_name']").clear()
            self.driver.find_element_by_xpath("//*[@name='bank_name']").send_keys(bank_name)
        # 姓名
            self.driver.find_element_by_xpath("//*[@name='username']").clear()
            self.driver.find_element_by_xpath("//*[@name='username']").send_keys(username)#UnicodeDecodeError: 'utf8' codec can't decode byte 0xe4 in position 0: unexpected end of data
        # 银行卡号
            self.driver.find_element_by_xpath("//*[@name='card_no']").clear()
            self.driver.find_element_by_xpath("//*[@name='card_no']").send_keys(card_no)
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
            i+=1
            time.sleep(180)

driver=webdriver.Chrome()
daifu=clpay1(driver)
account_id="201806"
bank_code="01050000"
bank_name=u"中国建设银行"
username=u"付贵炉"
card_no="6217001540022416380"
daifu.clpay(account_id,bank_code,bank_name,username,card_no)
time.sleep(100000)

# driver=webdriver.Chrome()
# daifu=clpay1(driver)
# account_id="201806"
# bank_code="01050000"
# bank_name=u"工商银行"
# username=u"丁双"
# card_no="6222031203005565673"
# daifu.clpay(account_id,bank_code,bank_name,username,card_no)
# time.sleep(1000)

# driver=webdriver.Chrome()
# daifu=clpay1(driver)
# account_id="201801"
# bank_code="01050000"
# bank_name=u"中国工商银行"
# username=u"丁双"
# card_no="6217001540022416380"
# daifu.clpay(account_id,bank_code,bank_name,username,card_no)
# time.sleep(1000)
