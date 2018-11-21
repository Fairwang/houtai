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

class merchant():
    def cash(self,):
        driver = webdriver.Chrome()
        # driver.get('https://testpay.hongnaga.com/merchant.html')
        driver.get("https://pay.hongnaga.com/admin/index/index.html")
        driver.maximize_window()
        driver.find_element_by_id("mch_id").clear()
        mch_id="admin"
        driver.find_element_by_id("mch_id").send_keys(mch_id)
        driver.find_element_by_id("password").clear()
        # driver.find_element_by_id("password").send_keys(123456)
        driver.find_element_by_id("password").send_keys("cl!@#0571")
        driver.find_element_by_id("captcha").send_keys(0)
        driver.find_element_by_id("sub").click()
        time.sleep(10)
        # 手动输入验证码
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_link_text("商户模块").click()
        driver.find_element_by_xpath("//*[contains(@data-index,'8')]").click()
        # 切换到账户管理页面
        frame_xpath = driver.find_element_by_xpath("//*[contains(@name,'iframe8')]")
        driver.switch_to.frame(frame_xpath)
        cash=driver.find_element_by_xpath("//*[contains(@onclick,'merchantconfig.html?ids=18482')]")
        driver.find_element_by_xpath(cash).click()
    #代付界面
        frame_cash = driver.find_element_by_xpath("//*[contains(@id,'layui-layer-iframe2')]")
        driver.switch_to.frame(frame_cash)
        beifujin=table.get_table(driver)
        beifujin=beifujin.get_table_content("list")
        beifujin=beifujin[1:]
        wclb = beifujin[0][4]
        wcll = beifujin[0][5]
        return [wclb,wcll]







# channel="//*[contains(@onclick,'ids=272')]"  #DDP 渠道
# a=cash()
# a.cash(channel)




