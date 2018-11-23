#!/user/bin/python
#  -*-coding: utf-8-*-
import unittest
import time
from selenium.webdriver.common.by import By
from appium import webdriver
import time
import sys
import isElementExist

import MySQLdb

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


def query_database(self, sql):
    # coon = MySQLdb.connect(host='cpaytest.tinywan.com', user='root', passwd='123456', db='cpay', port=3306,
    #                        charset='utf8')
    coon = MySQLdb.connect(host='cpay.hypayde.com', user='root', passwd='root123456', db='cl_cpay', port=3306,
                           charset='utf8')
    # cursor = coon.cursor()
    cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
    try:
        cur = cursor.execute(sql)
        rows = cursor.fetchall()
        qrcode_url = []
        for row in rows:
            qrcode_url.append(row["qrcode_url"])
        return qrcode_url
    except:
        print "Error: This is except"
    coon.close()



class zhifubao(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfromVersion'] = '7.1.1'
        desired_caps['deviceName'] = '33d04c7c'
        # desired_caps['platfromVersion'] = '8.0.0'
        # desired_caps['deviceName'] = '73EBB18606209676'
        desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
        desired_caps['noReset']=True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_zhifubao(self):
        driver=self.driver
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
        time.sleep(1)
        # f0 = open('D:\\zxtest\\cpay.txt', 'r')#备注
        # z = len(open('D:\\zxtest\\cpay.txt', 'r').readlines())
        sql = "SELECT qrcode_url FROM `cl_merchant_qrcode`where mch_id=1006 and expire_time>0 "
        erweimas =query_database(self,sql)
        for erweima in erweimas:
            # beizhu = f0.readline()
            print "erweima:%s"%erweima
            if erweima == '':
                break
            time.sleep(2)
            driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys(erweima)
            time.sleep(4)
            driver.find_element_by_xpath("//android.widget.TextView[@text='发送']").click()
            time.sleep(2)
            lianjies=driver.find_elements_by_id("com.alipay.mobile.chatapp:id/chat_msg_text")
            print type(lianjies)
            time.sleep(2)
            lianjies[-1].click()
            time.sleep(5)
            element01="//android.widget.Button[@text='确认转账']"
            if isElementExist.isElementExist(self, element01):
                pass
            else:
                lianjies[-1].click()
                time.sleep(2)
            driver.implicitly_wait(100)
            driver.find_element_by_id("com.alipay.mobile.payee:id/payee_NextBtn").click()
            time.sleep(5)
            driver.find_element_by_xpath("//android.widget.TextView[@text='立即付款']").click()
            time.sleep(1)
            x=driver.get_window_size()['width']
            y=driver.get_window_size()['height']
            driver.tap([(140*x/1080,1500*y/1920)],0)
            driver.tap([(200*x/1080,1500*y/1920)],0)
            driver.tap([(800*x/1080,1500*y/1920)],0)
            driver.tap([(800*x/1080,1500*y/1920)],0)
            driver.tap([(500*x/1080,1680*y/1920)],0)
            driver.tap([(500*x/1080,1680*y/1920)],0)
            time.sleep(3)
            element02="//android.widget.TextView[@text='银行卡可用余额不足，请选择下列方式完成付款(ALIN37768)']"
            if isElementExist.isElementExist(self, element02):
                print "付款账号余额不足，请充值！"
                time.sleep(3)
            else:
                pass
            element="//android.widget.TextView[@text='开通指纹支付']"
            if isElementExist.isElementExist(self, element):
                driver.find_element_by_xpath("//android.widget.TextView[@text='取消']").click()
                time.sleep(3)
            else:
                pass
            time.sleep(2)
            driver.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()
            time.sleep(1)
        # f0.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
