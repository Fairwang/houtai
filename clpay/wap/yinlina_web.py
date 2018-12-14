#!user/bin/python
# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import  Keys
from houtai.clpay.common import isElementExist
#电脑端--支付demo界面--赤龙--银联wap--银生宝

class yinlian_web():
    def yinlian_web(self):
        driver = webdriver.Chrome()
        driver.get('https://testpay.hongnaga.com/?debug=true')

        # driver.get('https://pay.hongnaga.com/?debug=true')
        time.sleep(3)
        a= driver.switch_to.alert
        a.send_keys("123456778")
        # a.send_keys("112233")
        a.accept()
        time.sleep(2)
        zf01 = "支付方式"
        iselement01 = isElementExist.isElementExist(driver)
        if iselement01.isElementExistLink(iselement01):
            print "支付方式"

        lines = [11,16,13]
        i = 1
        handles = driver.window_handles
        print handles
        for price in lines:
            print  price
            # 商户ID
            driver.find_element_by_xpath("//*[@name='mch_id']").clear()
            driver.find_element_by_xpath("//*[@name='mch_id']").send_keys("12001")
            # 支付方式
            pay_type = Select(driver.find_element_by_id("pay_type"))
            driver.find_element_by_id("pay_type").click()
            pay_type.select_by_value("6")#银联wap
            # 金额
            driver.find_element_by_name("price").clear()  #
            driver.find_element_by_name("price").send_keys(price)
            # 银行编码
            # driver.find_element_by_xpath("//*[@name='bank_code']").clear()
            # driver.find_element_by_xpath("//*[@name='bank_code']").send_keys("01050000")
            # 姓名
            # driver.find_element_by_xpath("//*[@name='username']").clear()
            # driver.find_element_by_xpath("//*[@name='username']").send_keys("付贵炉")
            # 银行卡号
            # driver.find_element_by_xpath("//*[@name='card_no']").clear()
            # driver.find_element_by_xpath("//*[@name='card_no']").send_keys("6217001540022416380")
            time.sleep(2)
            driver.find_element_by_id("pay").click()
            time.sleep(8)
            windows=driver.window_handles
            print windows  #[u'CDwindow-0', u'CDwindow-1']
            current=driver.current_window_handle
            time.sleep(1)
            print current

            driver.switch_to.window(windows[-1])  # 返回发起界面
            print "yes"
            time.sleep(1)
            driver.find_element_by_class_name("uns_btn").click()
            time.sleep(1)
            driver.find_element_by_id("IDcard").send_keys(Keys.F12)
            time.sleep(1)
            driver.find_element_by_id("IDcard").send_keys("6228480218885139970")#卡号
            time.sleep(1)
            driver.find_element_by_id("btnSubmit").click()
            time.sleep(1)
            username=u"高攀"
            driver.find_element_by_id("username").send_keys(username)
            time.sleep(1)
            driver.find_element_by_name("idCardNo").send_keys("610481198608265032")
            time.sleep(1)
            driver.find_element_by_id("phone").send_keys("13772157150")
            time.sleep(1)
            driver.find_element_by_id("agree").click()
            time.sleep(1)
            driver.find_element_by_id("btnSubmit").click()
            time.sleep(6)
            #发送验证码，输入验证码
            # wxts=driver.switch_to.alert()
            # print wxts.text
            # wxts.accept()


            driver.find_element_by_id("btnSubmit").click()
            time.sleep(2)
            windows = driver.window_handles
            time.sleep(2)
            driver.switch_to.window(windows[0])
            time.sleep(1)
            zf11 = "支付完成"
            iselement01=isElementExist.isElementExist(driver)
            if iselement01.isElementExistLink(zf11):
                print "支付完成元素存在"
                driver.find_element_by_link_text("支付完成").click()
                time.sleep(1)
            else:
                pass
            time.sleep(3)
            if i == 3:
                time.sleep(60000)
            i = i + 1
yinlian=yinlian_web()
yinlian2=yinlian.yinlian_web()




