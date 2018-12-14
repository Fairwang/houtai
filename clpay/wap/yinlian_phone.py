#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from appium import webdriver
from houtai.clpay.common import isElementExist
#手机端--支付demo界面--赤龙--银联wap--银生宝
class yinlian(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'#测试的目标机器
        desired_caps['platfromVersion']='7.1.1'#目标设备的系统版本
        desired_caps['deviceName']='33d04c7c'#测试机器的名称（设备名称即可）
        desired_caps['browserName']='Chrome'
        desired_caps['appPackage']='com.android.chrome'#被测应用的包名（只有Android测试才用）
        desired_caps['appActivity']='org.chromium.chrome.browser.ChromeTabbedActivity'
        desired_caps['unicodeKeyboard']='true'#支持中文输入，默认false
        desired_caps['resetKeyboard'] = 'true'  # 重置输入法为系统默认
        desired_caps['noReset']='true'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def test_yinlian(self):
        time.sleep(5)
        # driver=webdriver.Chrome()  chrome已经作为APP启动了
        self.driver.get('https://testpay.hongnaga.com/?debug=true')
        # self.driver.get('https://pay.hongnaga.com/?debug=true')
        time.sleep(3)
        a = self.driver.switch_to.alert
        a.send_keys("123456778")
        # a.send_keys("112233")
        a.accept()
        time.sleep(2)
        lines = [11, 16, 13]
        i = 1
        handles = self.driver.window_handles
        print "打开前%s "%handles
        current = self.driver.current_window_handle
        time.sleep(1)
        print "current%s " % current
        for price in lines:
            print  price
            # 商户ID
            self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")
            # 支付方式
            pay_type = Select(self.driver.find_element_by_id("pay_type"))
            self.driver.find_element_by_id("pay_type").click()
            pay_type.select_by_value("6")  # 银联wap
            # 金额
            self.driver.find_element_by_name("price").clear()  #
            self.driver.find_element_by_name("price").send_keys(price)

            time.sleep(2)
            self.driver.find_element_by_id("pay").click()
            time.sleep(8)
            windows = self.driver.window_handles
            print "after%s"%windows  # [u'CDwindow-0', u'CDwindow-1']
            current = self.driver.current_window_handle
            time.sleep(1)
            # print "current%s "%current
            #
            # print windows[-1].encode("utf-8")
            print type(windows[-1])
            self.driver.switch_to.window(windows[-1])  # 返回发起界面
            # self.driver.switch_to.active_element()
            print "web switch success"
            time.sleep(1)
            self.driver.find_element_by_class_name("uns_btn").click()#风险提示
            time.sleep(1)
            self.driver.find_element_by_id("IDcard").send_keys(Keys.F12)
            time.sleep(1)
            self.driver.find_element_by_id("IDcard").send_keys("6228480218885139970")  # 卡号
            time.sleep(1)
            self.driver.find_element_by_id("btnSubmit").click()
            time.sleep(1)
            username = u"高攀"
            self.driver.find_element_by_id("username").send_keys(username)
            time.sleep(1)
            self.driver.find_element_by_name("idCardNo").send_keys("610481198608265032")
            time.sleep(1)
            self.driver.find_element_by_id("phone").send_keys("13772157150")
            time.sleep(1)
            self.driver.find_element_by_id("agree").click()
            time.sleep(1)
            self.driver.find_element_by_id("btnSubmit").click()
            time.sleep(6)


            # 发送验证码，输入验证码
            self.driver.find_element_by_id("btnSubmit").click()
            time.sleep(2)

            windows = self.driver.window_handles
            time.sleep(2)
            self.driver.switch_to.window(windows[0])
            time.sleep(1)
            zf11 = "支付完成"
            iselement01 = isElementExist.isElementExist(self.driver)
            if iselement01.isElementExistLink(zf11):
                print "支付完成元素存在"
                self.driver.find_element_by_link_text("支付完成").click()
                time.sleep(1)
            else:
                pass
            time.sleep(3)
            if i == 3:
                time.sleep(60000)
            i = i + 1

    def tearDown(self):
        self.driver.quit()



if __name__=='__main__':
    unittest.main()

