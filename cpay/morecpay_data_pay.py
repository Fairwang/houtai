#!/user/bin/python
#  -*-coding: utf-8-*-
import unittest
import time
from selenium.webdriver.common.by import By
from appium import webdriver
import time
import sys
from houtai.lk import iselementexist
import threading

import MySQLdb

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


def query_database(self, sql):
    coon = MySQLdb.connect(host='cpaytest.tinywan.com', user='root', passwd='123456', db='cpay', port=3306,
                           charset='utf8')
    # coon = MySQLdb.connect(host='cpay.hypayde.com', user='root', passwd='root123456', db='cl_cpay', port=3306,
    #                        charset='utf8')
    # cursor = coon.cursor()
    cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
    try:
        cur = cursor.execute(sql)
        rows = cursor.fetchall()
        qrcode_url = []
        # print rows
        for row in rows:
            # print row["qrcode_url"]
            qrcode_url.append(row["qrcode_url"])
        # print rows
        return qrcode_url
    except:
        print "Error: This is except"
        # coon.commit()
    coon.close()


# class zhifubao(unittest.TestCase):
# def setUp(self):
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platfromVersion'] = '7.1.1'
desired_caps['deviceName'] = '33d04c7c'
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps['automationName'] = 'uiautomator2'  ##############
desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
desired_caps['noReset'] = True
# self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
desired_caps6 = {}
desired_caps['platformName'] = 'Android'
desired_caps['platfromVersion'] = '8.0.0'
desired_caps['deviceName'] = '73EBB18730214045'
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps['automationName'] = 'uiautomator2'  ##############
desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
desired_caps['noReset'] = True


def task1(self):
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver = self.driver
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
    time.sleep(1)


def task2(self):
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver = self.driver
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
    time.sleep(1)


if __name__ == "__main__":
    unittest.main()
