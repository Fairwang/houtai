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

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
import time
from selenium.webdriver.common.by import By
from appium import webdriver
import time
import sys
from houtai.lk import iselementexist
from jiandian.common import get_toast

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

        # self.get_toast=get_toast.get_toast(self.driver)
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
        time.sleep(5)
        # driver.tap([(500,1020),(600,1086)],2000)
        adb='adb shell input tap 524 1696'
        os.system(adb)
        time.sleep(10)
        print driver.contexts
        # adb1='adb shell input tap 400 1000'
        # os.system(adb1)
        # driver.tap([(335, 998),(500, 1172)], 4000)#点击狂欢城330 997  538  1206
        # time.sleep(3)
        # adb2='adb shell input tap 560 1782'#随意
        # adb2='adb shell input tap 900 1853'#点击我的品牌728
        # os.system(adb2)
        # driver.tap([(730, 1800),(820, 1874)], 4000)#点击我的品牌728  1790   824  1874
        # time.sleep(3)
        while True:
            # adb3 = 'adb shell input tap 794 1300'
            adb3 = 'adb shell input tap 523 1806'
            os.system(adb3)
            print"选店铺"
            time.sleep(5)
            for i in range(2):
                adb4 = 'adb shell input tap 505 1152'
                os.system(adb4)
                print"宝箱"
                a=get_toast.get_toast(self.driver)
                # driver.tap([(262, 1058), (500, 1065)], 2000)
                time.sleep(5)
                adb5 = 'adb shell input tap 400 1356'#进入包厢界面
                os.system(adb5)
                print"第一次"
                # driver.tap([(380, 1356),(520, 1395)], 2000)#进入le店铺
                time.sleep(2)
                adb5 = 'adb shell input tap 552 1383'
                os.system(adb5)
                print"第二次"
                print i
                time.sleep(2)
                # if get_toast.get_toast('本店今日投理想金次数已用完，先逛逛店铺吧'):
                #     break
            driver.tap([(968, 144),(980, 169)], 2000)#退出
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
