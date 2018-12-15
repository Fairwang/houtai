#!user/bin/python
# coding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from houtai.cpay.LK import creat_page
from selenium import webdriver
import time
from houtai.clpay.common import isElementExist

from code.common import table

class merchant():
    def __init__(self,driver):
        self.driver=driver
        self.creat_page=creat_page.creat_page(driver)
    def cash(self,username,password):

        newwindow = 'window.open("http://wangcpay.tinywan.top/merchant/index/index.html")'
        self.driver.execute_script(newwindow)
        # 移动句柄，对新打开页面进行操作
        self.driver.switch_to.window(self.driver.window_handles[-1])
        id="email"
        iselementexist=isElementExist.isElementExist(self.driver)
        if iselementexist.isElementExistID(id):
            self.driver.maximize_window()
            self.creat_page.input_user(username)
            self.creat_page.input_pws(password)
            time.sleep(10)
            # 输入验证码
            # self.creat_page.click_btnlogin()
        self.driver.refresh()
        # 手动输入验证码
        self.driver.maximize_window()
        time.sleep(5)
        self.creat_page.click_C2C()
        time.sleep(2)
        self.creat_page.click_app()
        # 切换到app账号页面--应用id为10086的
        self.creat_page.app_iframe()
        #点击编辑
        self.creat_page.app_edit()
        #切换至编辑账号界面
        self.creat_page.edit_iframe()
    #编辑APP应用列表界面界面
        name="app05"
        key="123456"
        self.creat_page.edit_name(name)
        self.creat_page.edit_app_key(key)
        chosens=self.driver.find_elements_by_class_name("chosen-single")
        chosens[0].click()
        self.driver.find_element_by_xpath("//*[contains(@data-option-array-index,'4')]").click()
        chosens[1].click()
        self.driver.find_element_by_xpath()
        self.driver.find_element_by_id("sub")
        self.driver.switch_to.parent_content()
        self.driver.find_element_by_xpath("//*[contains(@layeropen,'merchant_app/create.html')]").click()








driver=webdriver.Chrome()

mch_id = "1025"
password = "123456"
a=merchant(driver)
a.cash(mch_id,password)




