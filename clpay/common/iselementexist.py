#!/user/bin/python
#  -*-coding: utf-8-*-

class isElementExist():
    def __init__(self,driver):
        self.driver=driver

    def isElementExistXpath(self, element):
        flag = True
        try:
            self.driver.find_element_by_xpath(element)
            return flag
        except:
            flag = False
            return flag

    def isElementExistID(self, element):
        flag = True
        try:
            self.driver.find_element_by_id(element)
            return flag
        except:
            flag = False
            return flag

    def isElementExistLink(self, element):
        flag = True
        try:
            self.driver.find_element_by_link_text(element)
            return flag
        except:
            flag = False
            return flag
