#!/user/bin/python
#  -*-coding: utf-8-*-

def isElementExist(self, element):
    flag = True
    driver = self.driver
    # self.driver = driver
    try:
        driver.find_element_by_xpath(element)
        return flag
    except:
        flag = False
        return flag
