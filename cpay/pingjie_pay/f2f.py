#!user/bin/python
# coding:utf-8
# from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from appium import webdriver

# app端--chrome,点点支付demo界面——H5当面付扫码发起支付-打开另一个窗口，出现启动支付宝App支付--点击后出现弹框alert--自动跳转至确认付款界面，点击立即付款--输入支付密码
class C2Cwap(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'  # 测试的目标机器
        self.desired_caps['platfromVersion']='7.1.1'#目标设备的系统版本
        self.desired_caps['deviceName']='33d04c7c'#测试机器的名称（设备名称即可）
        self.desired_caps['browserName'] = 'Chrome'
        self.desired_caps['noReset'] = 'true'
        # self.desired_caps['appPackage']='com.android.chrome'#被测应用的包名（只有Android测试才用）
        self.desired_caps['appActivity'] = 'org.chromium.chrome.browser.ChromeTabbedActivity'
        # self.desired_caps['unicodeKeyboard']='true'#支持中文输入，默认false
        # self.desired_caps['resetKeyboard'] = 'true'  # 重置输入法为系统默认
        self.desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def test_C2Cwap(self):
        self.driver.get('https://cpay.hypayde.com/demo.html?debug=true')
        # self.driver.get('https://pay.hongnaga.com/?debug=true')
        a=self.driver.switch_to.alert
        # a.send_keys("123456778")
        a.send_keys("112233")
        a.accept()
        time.sleep(2)
        # self.driver.tap([(523, 1825)], 890)
        lines = [18]
        i = 1
        windows1 = self.driver.window_handles
        print"before pay%s" %windows1
        for price in lines:
            print  price
            # 商户ID
            self.driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            self.driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("1025")
            # 支付方式
            pay_type = Select(self.driver.find_element_by_id("pay_type"))
            self.driver.find_element_by_id("pay_type").click()
            # pay_type.select_by_value("11")  # 支付宝wap
            pay_type.select_by_value("7")  # （支付宝）当面付扫码
            # pay_type.select_by_value("5")  # 支付宝H5
            # 金额
            self.driver.find_element_by_name("price").clear()  #
            self.driver.find_element_by_name("price").send_keys(price)

            self.driver.find_element_by_id("pay").click() #点击了但是没有得到相应的效果
            time.sleep(5)

            windows=self.driver.window_handles
            print "after pay%s"%windows
            print windows[-1],type(windows[-1])
            w=windows[-1]
            ww=w.encode('utf-8')
            print type(ww)
            self.driver.switch_to.window(ww)#提示name 必须是string
            # for i in windows:
            #     self.driver.switch_to.window(i)
            #     if '点点支付测试DEMO':
            #         pass
            #     else:
            #         self.driver.switch_to.window(i)
            print self.driver.title
            # time.sleep(2)
            # print self.driver.current_activity
            # self.driver.find_element_by_id("com.android.chrome:id / tab_switcher_button").click()
            # time.sleep(3)
            # self.driver.tap([600,1553],1000)
            time.sleep(3)
            # 唤起支付宝App
            self.driver.find_element_by_xpath("//android.widget.Button[@text='启动支付宝App支付']").click()
            time.sleep(8)
            bb=self.driver.switch_to.alert()
            bb.dismiss()
            print "quxioa"
            # self.driver.tap([(145,1536),(225,1596)])
            # self.driver.tap(185, 1558)
            time.sleep(8)
            bb.dismiss()
            print "quxioa23"
            # self.driver.current_activity()#无法切换到支付宝界面
            lijifukuan=self.driver.current_activity
            print "aaa:  %s"%lijifukuan
            # self.driver.wait_activity("com.alipay.mobile.payee.ui.PayeeQRPayFormActivity",5,2)
            self.driver.start_activity("com.eg.android.AlipayGphone","com.alipay.android.msp.ui.views.MspContainerActivity")
            time.sleep(10)
            print "hhahh"
            self.driver.switch_to.active_element.click()

            print self.driver.current_activity
            time.sleep(3)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='立即付款']").click()#no such element
            # self.driver.find_element_by_xpath("// android.widget.FrameLayout[ @ index = '0']").click()#定位不到,
            self.driver.tap([(523,1825)],890)#Method has not yet been implemented
            time.sleep(3)

            print "sucess"
            if i == 1:
                time.sleep(60000)
            i = i + 1

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

