#!/user/bin/python
# -*-coding: utf-8-*-
from selenium import webdriver
from houtai.cpay.LK import creat_page
import unittest
class merchant_account(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def set_Up(self):
        self.driver=webdriver.Chrome()
        self.ele=creat_page.creat_page(self.driver)



    def test_add(self):
        self.driver.get("http://wangcpay.tinywan.top/merchant/index/index.html")
        aa=self.driver.switch_to.alert
        aa.send_keys("112233")
        aa.accept()
        self.name="test001"
        self.key="123456"
        self.ele.click_C2C()
        self.ele.click_app()
        self.ele.app_iframe()
        self.ele.add_app()
        self.ele.add_iframe()
        self.ele.add_app_name(self.name)
        self.ele.add_app_key(self.key)
        self.ele.add_sub()
        aa=self.driver.switch_to.alert
        print aa.text




    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main