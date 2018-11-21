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

class cash():
    def cash(self,channel,amount):
        driver = webdriver.Chrome()
        # driver.get('https://testpay.hongnaga.com/merchant.html')
        driver.get("https://pay.hongnaga.com/merchant/login")
        # driver.get('https://cpay.hypayde.com/merchant')
        # driver.maximize_window()
        driver.find_element_by_id("mch_id").clear()
        driver.find_element_by_id("mch_id").send_keys(12001)
        driver.find_element_by_id("password").clear()
        # driver.find_element_by_id("password").send_keys(123456)
        driver.find_element_by_id("password").send_keys("chilong112233")
        driver.find_element_by_id("captcha").send_keys(0)
        driver.find_element_by_id("sub").click()
        time.sleep(10)
        # 手动输入验证码
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_link_text("账户管理").click()
        driver.find_element_by_xpath("//*[contains(@data-index,'6')]").click()
        # 切换到账户管理页面
        frame_xpath = driver.find_element_by_xpath("//*[contains(@name,'iframe6')]")
        driver.switch_to.frame(frame_xpath)

        driver.find_element_by_xpath(channel).click()
    #提现界面

        acc_name = u"付贵炉"
        acc_card = "6217001540022416380"
        acc_subbranch = u"中国建设银行"
        pay_password = "112233"

        frame_withdraw = driver.find_element_by_xpath("//*[contains(@id,'layui-layer-iframe1')]")
        driver.switch_to.frame(frame_withdraw)
        # amount=2
        driver.find_element_by_name("amount").clear()
        driver.find_element_by_name("amount").send_keys(amount)
        # acc_name=u"付贵炉"
        driver.find_element_by_name("acc_name").clear()
        driver.find_element_by_name("acc_name").send_keys(acc_name)
        # acc_card="6217001540022416380"
        driver.find_element_by_name("acc_card").clear()
        driver.find_element_by_name("acc_card").send_keys(acc_card)
        # acc_subbranch=u"中国建设银行"
        driver.find_element_by_name("acc_subbranch").clear()
        driver.find_element_by_name("acc_subbranch").send_keys(acc_subbranch)
        # pay_password="112233"
        driver.find_element_by_name("pay_password").clear()
        driver.find_element_by_name("pay_password").send_keys(pay_password)

        # captcha="112233"
        # driver.find_element_by_name("captcha").clear()
        # driver.find_element_by_name("captcha").send_keys(captcha)

        time.sleep(5)
        driver.find_element_by_name("btn-block")



# channel="//*[contains(@onclick,'ids=272')]"  #DDP 渠道
# a=cash()
# a.cash(channel)




