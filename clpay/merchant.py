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
from houtai.cpay import isElementExist


from code.common import table

class merchant():
    def __init__(self,driver):
        self.driver=driver
    def cash(self):

        newwindow = 'window.open("https://pay.hongnaga.com/admin/index/index.html")'
        self.driver.execute_script(newwindow)
        # 移动句柄，对新打开页面进行操作
        self.driver.switch_to.window(self.driver.window_handles[-1])
        id="username"
        iselementexist=isElementExist.isElementExist(self.driver)
        if iselementexist.isElementExistID(id):
            self.driver.maximize_window()
            self.driver.find_element_by_id("username").clear()
            mch_id="admin"
            self.driver.find_element_by_id("username").send_keys(mch_id)
            self.driver.find_element_by_id("password").clear()
            # driver.find_element_by_id("password").send_keys(123456)
            self.driver.find_element_by_id("password").send_keys("cl!@#0571")
            self.driver.find_element_by_id("captcha").send_keys(0)
            self.driver.find_element_by_id("sub").click()
            time.sleep(10)
        self.driver.refresh()
        # 手动输入验证码
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element_by_link_text("商户模块").click()
        self.driver.find_element_by_xpath("//*[contains(@data-index,'8')]").click()
        # 切换到账户管理页面
        frame_xpath = self.driver.find_element_by_xpath("//*[contains(@name,'iframe8')]")
        self.driver.switch_to.frame(frame_xpath)
        cash_xpath="//*[contains(@onclick,'merchantconfig.html?ids=18482')]"
        self.driver.find_element_by_xpath(cash_xpath).click()
    #代付界面
        frame_cash = self.driver.find_element_by_xpath("//*[contains(@src,'merchantconfig.html?ids=18482')]")
        self.driver.switch_to.frame(frame_cash)
        beifujin=table.get_table(self.driver)
        beifujin=beifujin.get_table_content("list")
        beifujin=beifujin[1:]
        wclb = beifujin[0][4]
        wcll = beifujin[0][5]
        # print wclb,wcll
        return [wclb,wcll]






#
# channel="//*[contains(@onclick,'ids=272')]"  #DDP 渠道
# a=merchant()
# a.cash()




