#!user/bin/python
# coding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from houtai.clpay.common import isElementExist
import time
from houtai.cpay.common import table
class profit_cash():
    def __init__(self,driver):
        self.driver=driver
    def profit_cash(self):
        # driver=webdriver.Chrome()
        # driver.get('https://pay.hongnaga.com/admin/index/index.html')
        newwindow = 'window.open("https://pay.hongnaga.com/admin/index/index.html")'
        self.driver.execute_script(newwindow)
        # 移动句柄，对新打开页面进行操作
        self.driver.switch_to.window(self.driver.window_handles[-1])
        id="username"
        iselementexist=isElementExist.isElementExist(self.driver)
        if iselementexist.isElementExistID(id):
            # driver.maximize_window()
            self.driver.find_element_by_id("username").clear()
            self.driver.find_element_by_id("username").send_keys("admin")
            self.driver.find_element_by_id("password").clear()
            # driver.find_element_by_id("password").send_keys(123456)
            # driver.find_element_by_id("password").send_keys("chilong112233")
            self.driver.find_element_by_id("password").send_keys("cl!@#0571")
            self.driver.find_element_by_id("captcha").send_keys(0)
            self.driver.find_element_by_id("sub").click()
            time.sleep(10)
        #手动输入验证码
        self.driver.refresh()
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_link_text("支付管理").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(@href,'/admin/payment_interface/index.html')]").click()
        #切换到代付商户页面
        frame_xpath=self.driver.find_element_by_xpath("//*[contains(@src,'payment_interface/index.html')]")
        self.driver.switch_to.frame(frame_xpath)

        #选中温州赤龙利润兑现
        lrdx=self.driver.find_elements_by_xpath("//a[contains(@onclick,'layeropen')]")
        lrdx[-1].click()
        #切换到利润兑现界面
        frame_xpath=self.driver.find_element_by_xpath("//*[contains(@name,'layui-layer-iframe1')]")
        self.driver.switch_to.frame(frame_xpath)

        lrdx=self.driver.find_elements_by_xpath("//h2[contains(@class,'text-success')]")
        mfb=lrdx[0].text#获取美付宝
        print mfb
        mfb=mfb.split(' ')#以list切割分成list，将2元 分割为 [2,元] 取出金额
        print mfb
        mfb=mfb[1]
        print u"美付宝金额%s"%mfb

        bfj=lrdx[1].text#获取备付金
        print bfj
        bfj=bfj.split(' ')
        print bfj
        bfj=bfj[0]
        print u"获取备付金%s"%bfj

        jylr=self.driver.find_elements_by_xpath("//h2[contains(@class,'text-navy')]")
        print  jylr
        jy=jylr[0].text#交易量统计
        print jy
        jy=jy.split(u'笔')

        print jy
        jrjy=jy[0]
        jrzjy=jy[1].split('/')
        jrzjy=jrzjy[1]
        print jrzjy
        print u"交易量统计%s%s"%(jrjy,jrzjy)

        zlr=jylr[1].text#总利润
        zlr=zlr.split(' ')
        zlr=zlr[0]
        print u"总利润%s"%zlr


        lr=self.driver.find_elements_by_xpath("//h2[contains(@class,'text-danger')]")
        print  lr
        lrye=lr[0].text#利润余额
        print lrye
        lrye=lrye.split(' ')
        print lrye
        lrye=lrye[2]
        print u"利润余额%s"%lrye

        dfz=self.driver.find_elements_by_xpath("//h2[contains(@class,'text-warning')]")
        sfzlr=dfz[0].text#代付中的利润
        print sfzlr
        sfzlr=sfzlr.split(' ')
        print sfzlr
        sfzlr=sfzlr[0]
        print u"代付中的利润%s"%sfzlr
        profit=[]
        for i in (mfb,bfj,jrjy,jrzjy,zlr,lrye,sfzlr):
            profit.append(i)
        print profit
        return profit
#
# a=profit_cash(driver)
# b=a.profit_cash(2)
# print "hhhhh%s:"%b

