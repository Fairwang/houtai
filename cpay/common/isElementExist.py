#!/user/bin/python
#  -*-coding: utf-8-*-
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
