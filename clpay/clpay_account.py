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

class account():
    def __init__(self,driver):
        self.driver=driver
    def account(self):
        newwindow = 'window.open("https://pay.hongnaga.com/merchant/login")'# 浏览器 新窗口打开连接 js语法
        self.driver.execute_script(newwindow) #调用js
        self.driver.switch_to.window(self.driver.window_handles[-1])# 移动句柄，对最新打开页面进行操作
        iselementexist=isElementExist.isElementExist(self.driver)
        id="mch_id"
        if iselementexist.isElementExistID(id):
            # driver=webdriver.Chrome()
            # # driver.get('https://testpay.hongnaga.com/merchant.html')
            self.driver.find_element_by_id("mch_id").clear()
            self.driver.find_element_by_id("mch_id").send_keys(12001)
            self.driver.find_element_by_id("password").clear()
            self.driver.find_element_by_id("password").send_keys("chilong112233")
            # driver.find_element_by_id("password").send_keys("chilong123456")
            self.driver.find_element_by_id("captcha").send_keys(0)
            self.driver.find_element_by_id("sub").click()
            time.sleep(10)
        #手动输入验证码
        self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_link_text("账户管理").click()
        self.driver.find_element_by_xpath("//*[contains(@href,'merchant_account/index.html')]").click()
        #切换到账户管理页面
        frame_xpath=self.driver.find_element_by_xpath("//*[contains(@src,'merchant_account/index.html')]")
        self.driver.switch_to.frame(frame_xpath)
        time.sleep(1)
        zhgl=table.get_table(self.driver)
        zhgl_table=zhgl.get_table_content("list")
        time.sleep(3)
        zhgl_table=zhgl_table[1:]
        print "zhgl_table is\n %s "%zhgl_table
        zhsz=zhgl_table[:]
        print zhsz
        for i in range(len(zhgl_table)):
            k= 0
            for j in range(len(zhgl_table[i])):
                if j in (1,11):
                    del zhsz[i][j-k]##删除成功后，j所在list总长度会减1
                    k=k+1
        print"a在这里啊：%s" %zhsz
        #取出xfp所在的的list
        z=[]
        for i in range(len(zhsz)):
            for j in zhsz[i]:
                if j=="XFP":
                # if j=="DDP":
                    print i
                    z=zhsz[i]
                    print z
        return z

## driver=webdriver.Chrome()
# a=account(driver)
# t=a.account(1)
# print t







