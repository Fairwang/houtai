#!/user/bin/python
#  -*-coding: utf-8-*-
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print 'Run task %s (%s)...' % (name, os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print 'Task %s runs %0.2f seconds.' % (name, (end - start))
#
# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'
#
# # !/user/bin/python
# #  -*-coding: utf-8-*-
# import unittest
# import time
# from selenium.webdriver.common.by import By
# from appium import webdriver
# import time
# import sys


import unittest
import time
from selenium.webdriver.common.by import By
from appium import webdriver
import time
import sys
from houtai.lk import iselementexist


class zhifubao(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfromVersion'] = '7.1.1'
        desired_caps['deviceName'] = '33d04c7c'
        desired_caps['appPackage'] = 'com.taobao.taobao'
        desired_caps['automationName'] = 'uiautomator2'  ##############
        desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_zhifubao(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='消息']").click()
        # driver.swipe(int(x * 0.25), int(y * 0.25), int(x * 0.97), int(y * 0.25), 5000)
        # time.sleep(3)
        # driver.implicitly_wait(5)
        # driver.find_element_by_xpath("//android.widget.TextView[@text='y***稀的战队']").click()
        # time.sleep(3)
        # driver.implicitly_wait(5)
        # driver.find_element_by_xpath("//android.view.View[@content-desc='去集能量']").click()
        # driver.implicitly_wait(5)
        # time.sleep(3)
        # print driver.contexts
        # time.sleep(3)

        # x = driver.get_window_size()['width']
        # y = driver.get_window_size()['height']
        # driver.swipe(int(x * 0.25), int(y * 0.25), int(x * 0.97), int(y * 0.25), 5000)
        driver.tap([(500,1026),(600,1089)],2000)
        time.sleep(10)
        driver.tap([(420, 1020),(442, 1072)], 2000)#jinru kuanghuanyemian
        time.sleep(5)
        driver.tap([(772, 1800),(793, 1826)], 2000)#jinru pingtai
        time.sleep(2)
        # driver.tap([(267, 1056),(277.1058)], 500)#xuanze dianpu
        driver.tap([(734, 1222),(756, 1236)], 2000)#xuanze dianpu
        time.sleep(2)
        for i in range(3):
            driver.tap([(509, 1123),(520, 11343)], 2000)#进入le店铺
            time.sleep(2)
            driver.tap([(467, 1375),(488, 1395)], 2000)
            time.sleep(2)
            driver.tap([(527, 1812),(549, 1833)], 2000)
            time.sleep(2)
        driver.tap([(968, 144),(980, 169)], 2000
                   )#退出
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
