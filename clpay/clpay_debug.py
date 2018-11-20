#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
#支付demo界面
class clpay():
    # def __init__(self,driver):
    #     self.driver=driver
    def clpay(self):
        def isElementExist(element):
            flag = True
            # driver = self.driver
            try:
                driver.find_element_by_link_text(element)
                return flag
            except:
                flag = False
                return flag
        driver=webdriver.Chrome()
        driver.get('https://pay.hongnaga.com/?debug=true')
        # driver.get("http://pay.frp.tinywan.top/?debug=true")
        # driver.get("https://pay.hongnaga.com/?debug=true")

        # h=driver.current_window_handle
        # print h
        # driver.maximize_window()
        a=driver.switch_to.alert
        # a.send_keys("123456778")
        a.send_keys("112233")

        # time.sleep(1)
        a.accept()
        for i in range(10,30):
            print  i
            driver.implicitly_wait(2)
        #商户ID
            driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")

        # 支付方式
            pay_type=Select(driver.find_element_by_id("pay_type"))
            driver.find_element_by_id("pay_type").click()
            # pay_type.select_by_value("13")#新支付宝转账
            # pay_type.select_by_value("5")#支付宝h5
            # pay_type.select_by_value("1")  # 网银支付
            pay_type.select_by_value("15")  # 支付宝扫码
            # pay_type.select_by_value("17")  # 支付宝wap
        # 金额
            # driver.implicitly_wait(5)

            driver.find_element_by_name("price").clear()#
            driver.find_element_by_name("price").send_keys(i)

        # 银行编码
            driver.find_element_by_xpath("//*[@name='bank_code']").clear()
            # driver.find_element_by_xpath("//*[@name='bank_code']").send_keys("01050000")

        # 姓名
            # driver.find_element_by_xpath("//*[@name='username']").clear()
            # driver.find_element_by_xpath("//*[@name='username']").send_keys("付贵炉")
        # 银行卡号
            # driver.find_element_by_xpath("//*[@name='card_no']").clear()
            # driver.find_element_by_xpath("//*[@name='card_no']").send_keys("6217001540022416380")

            time.sleep(2)
            driver.find_element_by_id("pay").click()
            driver.implicitly_wait(5)
            time.sleep(1)

            windows = driver.window_handles
            time.sleep(1)
            driver.switch_to.window(windows[0])
            time.sleep(1)
            zf11="支付完成"
            if isElementExist(zf11):
                driver.find_element_by_link_text("支付完成").click()
            else:
                pass
            time.sleep(3)
#
a=clpay()
a.clpay()
