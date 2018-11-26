#!user/bin/python
# coding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

from code.common import table
from houtai.cpay import isElementExist
class cash():
    def __init__(self,driver):
        self.driver=driver
    def cash(self,channel,amount,window):
        newwindow = 'window.open("https://pay.hongnaga.com/merchant/login")'
        self.driver.execute_script(newwindow)
        # 移动句柄，对新打开页面进行操作
        self.driver.switch_to.window(self.driver.window_handles[window])
        id="mch_id"
        iselementexist=isElementExist.isElementExist(self.driver)
        if iselementexist.isElementExistID(id):
            # driver = webdriver.Chrome()
            # driver.get('https://testpay.hongnaga.com/merchant.html')
            # driver.get("https://pay.hongnaga.com/merchant/login")
            # driver.get('https://cpay.hypayde.com/merchant')
            # driver.maximize_window()

            self.driver.find_element_by_id("mch_id").clear()
            self.driver.find_element_by_id("mch_id").send_keys(12001)
            self.driver.find_element_by_id("password").clear()
            # driver.find_element_by_id("password").send_keys(123456)
            self.driver.find_element_by_id("password").send_keys("chilong112233")
            # driver.find_element_by_id("captcha").send_keys(0)
            self.driver.find_element_by_id("sub").click()
            time.sleep(10)
        self.driver.refresh()
        # 手动输入验证码
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_link_text("账户管理").click()
        self.driver.find_element_by_xpath("//*[contains(@href,'merchant_account/index.html')]").click()
        #切换到账户管理页面
        frame_xpath=self.driver.find_element_by_xpath("//*[contains(@src,'merchant_account/index.html')]")
        self.driver.switch_to.frame(frame_xpath)

        self.driver.find_element_by_xpath(channel).click()
    #提现界面

        acc_name = u"付贵炉"
        acc_card = "6217001540022416380"
        acc_subbranch = u"中国建设银行"
        pay_password = "112233"

        frame_withdraw = self.driver.find_element_by_xpath("//*[contains(@id,'layui-layer-iframe1')]")
        self.driver.switch_to.frame(frame_withdraw)
        # amount=2
        self.driver.find_element_by_name("amount").clear()
        self.driver.find_element_by_name("amount").send_keys(amount)
        # acc_name=u"付贵炉"
        self.driver.find_element_by_name("acc_name").clear()
        self.driver.find_element_by_name("acc_name").send_keys(acc_name)
        # acc_card="6217001540022416380"
        self.driver.find_element_by_name("acc_card").clear()
        self.driver.find_element_by_name("acc_card").send_keys(acc_card)
        # acc_subbranch=u"中国建设银行"
        self.driver.find_element_by_name("acc_subbranch").clear()
        self.driver.find_element_by_name("acc_subbranch").send_keys(acc_subbranch)
        # pay_password="112233"
        self.driver.find_element_by_name("pay_password").clear()
        self.driver.find_element_by_name("pay_password").send_keys(pay_password)

        # captcha="112233"
        # driver.find_element_by_name("captcha").clear()
        # driver.find_element_by_name("captcha").send_keys(captcha)

        time.sleep(10)
        self.driver.find_element_by_name("btn-block")


#
# channel="//*[contains(@onclick,'ids=272')]"  #DDP 渠道
# a=cash()
# a.cash(channel,2)




