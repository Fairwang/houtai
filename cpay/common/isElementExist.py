#!/user/bin/python
#  -*-coding: utf-8-*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class isElementExist():
    def __init__(self,driver):
        self.driver=driver

    def isElementExist(self, element):
        flag = True
        # driver = self.driver
        # self.driver = driver
        try:
            self.driver.find_element_by_xpath(element)
            return flag
        except:
            flag = False
            return flag

    def isElementExistID(self, element):
        flag = True
        # driver = self.driver
        # self.driver = driver
        try:
            self.driver.find_element_by_id(element)
            return flag
        except:
            flag = False
            return flag

    def isElementExistWait(self,element):
        flag=True
        try:
            WebDriverWait(self.driver,1).until(EC.presence_of_element_located(element))#element=(By.ID,"jeo")
            return flag
        except:
            flag=False
            return flag

    def isElementExistLinktext(self,element):
        flag=True
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_link_text(element)
            return flag
        except:
            flag=False
            return flag
