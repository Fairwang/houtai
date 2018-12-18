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
from houtai.cpay.common import isElementExist
from houtai.cpay.common import table
#cpay C2C app账号 编辑/添加app账号
#添加app应用名称/密码，绑定支付宝号/状态，并保存
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
        name1="app05"
        key1="123456"
        self.creat_page.edit_name(name1)
        self.creat_page.edit_app_key(key1)
        chosens=self.driver.find_elements_by_class_name("chosen-single")#选择需要绑定的支付宝号
        chosens[0].click()
        # self.driver.find_element_by_xpath("//*[contains(@data-option-array-index,'4')]").click()
        # chosens[1].click()
        state=self.driver.find_elements_by_class_name("iCheck-helper")
        state[0].click()#禁用
        self.driver.find_element_by_id("sub")#点击提交
        self.driver.switch_to.parent_content()
        # self.driver.find_element_by_xpath("//*[contains(@layeropen,'merchant_app/create.html')]").click()
        #对比添加的设置是否正确
        table_id="list"
        app_tables=table.get_table(driver)
        app_tables=app_tables.get_table_content(table_id)
        try:
            app_tables[1][1]=name1
            app_tables[1][2]=key1
            app_tables[1][3]=chosens[0].text
            app_tables[1][6]=state[0].text
        except AttributeError:
            print "添加的信息错误"














driver=webdriver.Chrome()

mch_id = "1025"
password = "123456"
a=merchant(driver)
a.cash(mch_id,password)




