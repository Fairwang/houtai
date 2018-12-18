#!/user/bin/python
#  -*-coding: utf-8-*-
import unittest
import time
from appium import webdriver
import time
import random
class zhifubao(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfromVersion'] = '7.1.1'
        desired_caps['deviceName'] = '192.168.1.118:5555'
        # desired_caps['deviceName'] = '33d04c7c'
        # desired_caps['platfromVersion']='8.0.0'
        # desired_caps['deviceName']='73EBB18629223414'
        desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
        # desired_caps['automationName'] = 'uiautomator2'  ##############
        desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
        desired_caps['noReset']=True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_zhifubao(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='换个账号登录']").click()
        time.sleep(3)
        username="15868314566"
        # for u in username:
        #     t1=random.randint(1,10)
        #     time.sleep(t1)
        #     self.driver.find_element_by_id("com.ali.user.mobile.security.ui:id/content").send_keys(Keys.NUMPAD1)
        #     # self.driver.switch_to.active_element.send_keys(u)
        self.driver.find_element_by_id("com.ali.user.mobile.security.ui:id/content").send_keys(username)
        time.sleep(3)
        self.driver.find_element_by_id("com.ali.user.mobile.security.ui:id/nextButton").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='换个方式登录']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='密码登录']").click()
        time.sleep(5)
        password=""
        x=1080
        y=1920
        self.driver.tap([(593.5*x/1080, 1344.3*y/1920)], 0)
        time.sleep(2)

        # self.driver.hide_keyboard()
        for p in password:
            t=random.randint(1,10)
            time.sleep(t)
            self.driver.switch_to.active_element.send_keys(p)

        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()











        # driver=self.driver
        # time.sleep(3)
        # driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
        # time.sleep(1)
        # f0 = open('D:\\zxtest\\zhifubao.txt', 'r')
        # z = len(open('D:\\zxtest\\zhifubao.txt', 'r').readlines())
        # x=[]
        # while True:
        #     dat0 = f0.readline()
        #
        #     driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='更多']").click()
        #     time.sleep(2)
        #     zhuanzhang=driver.find_elements_by_xpath("//android.widget.TextView[@text='转账']")
        #     zhuanzhang[-1].click()
        #     time.sleep(1)
        #     driver.find_element_by_xpath("//android.widget.EditText[@content-desc='输入转账金额']").click()
        #     time.sleep(1)
        #     x=driver.get_window_size()['width']
        #     y=driver.get_window_size()['height']

            # time.sleep(10)
            # driver.tap([(476*x/1080, 1795*y/1920)], 0)
            # driver.tap([(735*x/1080, 1806*y/1920)], 0)
            # driver.tap([(476*x/1080, 1795*y/1920)], 0)
            # driver.tap([(278*x/1080, 1313*y/1920)], 0)

        # driver.find_element_by_id("com.ali.user.mobile.security.ui:id/loginButton").click()
        # time.sleep(3)
        # driver.find_element_by_id("com.ali.user.mobile.security.ui:id/userAccountInput").send_keys("15868314566")
        # time.sleep(3)
        # driver.find_element_by_id("com.ali.user.mobile.security.ui:id/userPasswordInput").send_keys("ymxx158")
        # time.sleep(3)
        # driver.find_element_by_id("com.ali.user.mobile.security.ui:id/loginButton").click()
        # time.sleep(2)
        # driver.tap([(1,1380),(100,1400)],500)
        # time.sleep(2)
        # driver.tap([(1,1380),(100,1400)],500)
        # time.sleep(2)
        # driver.tap([(1000,1400),(1079,1559)],500)
        # time.sleep(2)
        # driver.tap([(1000,1400),(1079,1559)],500)
        # time.sleep(2)
        # driver.tap([(500,1600),(500,1739)],500)
        # time.sleep(2)
        # driver.tap([(500,1600),(500,1739)],500)
        #
        # driver.find_element_by_      #     time.sleep(1)#红米5A
        #     driver.tap([(355*x/720, 1207*y/1280)], 0)
        #     driver.tap([(44*x/720, 877*y/1280)], 0)
        #     driver.tap([(355*x/720, 1207*y/1280)], 0)
        #     driver.tap([(184*x/720, 886*y/1280)], 0)
        #
        #
        #
        #     driver.find_element_by_xpath("//android.widget.EditText[@text='添加备注(50字以内)']").send_keys(dat0)
        #     time.sleep(1)
        #
        #     driver.find_element_by_xpath("//android.widget.Button[@text='确认转账']").click()
        #     time.sleep(3)
        #     driver.find_element_by_xpath("//android.widget.TextView[@text='立即付款']").click()
        #     time.sleep(1)
        #     driver.tap([(140*x/1080,1500*y/1920)],0)
        #     time.sleep(1)
        #     driver.tap([(200*x/1080,1500*y/1920)],0)
        #     time.sleep(1)
        #     driver.tap([(800*x/1080,1500*y/1920)],0)
        #     time.sleep(1)
        #     driver.tap([(800*x/1080,1500*y/1920)],0)
        #     time.sleep(1)
        #     driver.tap([(500*x/1080,1680*y/1920)],0)
        #     time.sleep(1)
        #     driver.tap([(500*x/1080,1680*y/1920)],0)
        #     time.sleep(3)
        #     driver.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()
        #     time.sleep(1)
        #     if dat0 == '':
        #         break
        # f0.close()xpath("//android.widget.ImageView[@content-desc='图片 4, 2018-08-27 16:25']").click()




    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

