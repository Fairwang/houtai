#!/user/bin/python
# -*-coding: utf-8-*-
from selenium import webdriver
from houtai.cpay.LK import creat_page
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from houtai.cpay.common.isElementExist import isElementExist
from selenium.webdriver.support.ui import Select
class merchant_account(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.ele=creat_page.creat_page(self.driver)
        self.isElementExist=isElementExist(self.driver)
        self.driver.get("http://wangcpay.tinywan.top/merchant/index/index.html")
        time.sleep(10)
        self.driver.maximize_window()
        # aa=self.driver.switch_to.alert
        # aa.send_keys("112233")
        # aa.accept()
        self.name="test001"
        self.key="123456"
@
    def test_add(self):

        time.sleep(2)
        self.ele.click_C2C()
        time.sleep(2)
        self.ele.click_app()
        time.sleep(2)
        self.ele.app_iframe()
        time.sleep(2)
        self.ele.add_app()
        time.sleep(2)
        self.ele.add_iframe()
        time.sleep(2)
        self.ele.add_app_name(self.name)
        self.ele.add_app_key(self.key)
        self.ele.bind_alipay()
        time.sleep(1)
        # self.driver.find_element_by_link_text("hongshan8@shopjian.com").click()
        time.sleep(2)
        self.ele.bind_alipay2()#元素不存在
        time.sleep(2)
        self.ele.add_sub()
    #未选择支付宝账号，提示至少绑定一个账号
        # 弹框 layer.msg 获取文本
        # layer3=(By.LINK_TEXT,'至少绑定一个账号')
        # WebDriverWait(self.driver,2).until(EC.presence_of_element_located(layer3))
        # if self.isElementExist.isElementExistWait(layer3) :
        #     print "yes"
        # else:
        #     print "no"

    def test_del(self):



    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()