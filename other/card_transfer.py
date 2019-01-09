#!/user/bin/python
#  -*-coding: utf-8-*-
# import unittest
# from jiandian01 import getmsg_ex, swipe
#个人转账时需要校验验证码
#企业不需要验证
#alip  支付宝转账到银行卡
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def tagname_iselement(element):
    flag=True
    try:
        driver.find_element_by_tag_name(result)
        return flag
    except :
        flag=False
        return flag
def xpath_iselement(element):
    flag=True
    try:
        driver.find_element_by_xpath(element)
        return flag
    except:
        flag=True
        return flag

f = open("E:\\zxtest\\zijinguiji.txt", 'r')
lines = f.readlines()      #读取全部内容 ，并以列表方式返回
print lines
for line in lines:
    line=line.strip()
    print line
    user=line.split(",")[0]
    passw=line.split(",")[1]
    zpassw=line.split(",")[2]
    print user
    print passw
    if len(user)>11:
        #账户为邮箱  视为公司账户
        #已经绑定银行卡
        time.sleep(2)
        driver=webdriver.Chrome()
        driver.get('https://auth.alipay.com/login/index.htm')
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='J-loginMethod-tabs']/li[2]").click()
        print "yes1"
        for i in user:
            t=random.randint(1,3)
            print i
            time.sleep(t)
            driver.find_element_by_xpath("//*[@id='J-input-user']").send_keys(i)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='J-input-user']").send_keys(Keys.TAB)
        time.sleep(1)
        for p in  passw:
            t2=random.randint(1,3)
            time.sleep(t2)
            driver.switch_to.active_element.send_keys(p)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@type='submit']").click()
        print "login success"

        time.sleep(3)
        #点击、进入资金管理界面
        driver.find_element_by_xpath('//*[@id="react-content"]/div/div[1]/div[2]/div/div[4]/div[1]/div/div[4]/div/a').click()
        windows=driver.window_handles
        driver.switch_to.window(windows[-1])
        #获取当前金额
        price=driver.find_element_by_xpath('//*[@id="react-content"]/div/div[2]/div[2]/div[1]/span/div[1]/div[2]').text
        #点击、进入提现
        driver.find_element_by_xpath('//*[@id="react-content"]/div/div[2]/div[2]/div[1]/div/a[3]').click()
        windows=driver.window_handles
        driver.switch_to.window(windows[-1])
        #判断是否已经绑定银行卡
        # bind=u"添加银行账户"
        bind='//*[@class="mi-button-text"]'
        if xpath_iselement(bind):
            driver.find_element_by_xpath(bind).click()
            driver.refresh()
            yinhangzhanghu="6217001540022416380"
            yinhang=u"中国建设银行"
            kaihuhang=u"西溪支行"
            #银行账户
            driver.find_element_by_xpath('//*[@id="J_card"]').send_keys(yinhangzhanghu)
            driver.find_element_by_xpath('//*[@id="J_card"]').send_keys(Keys.TAB)
            #开户行
            for p in yinhang:
                y = random.randint(1, 3)
                time.sleep(y)
                driver.find_element_by_xpath('//*[@id="J_bankName"]').send_keys(p)
            driver.find_element_by_xpath('//*[@id="J_bankName"]').send_keys(Keys.TAB)
            driver.find_element_by_xpath('//*[@id="J_bankName"]').send_keys(Keys.TAB)

            #选择省份
            driver.find_element_by_xpath('//*[@id="J_districtView11"]').click()
            driver.find_element_by_xpath('//*[@title="浙江省"]').click()#浙江省
            driver.find_elements_by_xpath('//*[@title="杭州市"]').click()#杭州市
            # driver.find_element_by_xpath('/html/body/div[11]/div/div/div[31]').click()#浙江省
            # driver.find_elements_by_xpath('/html/body/div[10]/div/div[2]/div[1]').click()#杭州市
            for p in kaihuhang:
                y = random.randint(1, 3)
                time.sleep(y)
                driver.find_element_by_xpath('//*[@id="J_branchBankName"]').send_keys(p)
            driver.find_element_by_xpath('//*[@id="J_bankName"]').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@type="submit"]').click()
            driver.refresh()
            windows=driver.window_handles
            driver.switch_to.window(windows[-2])
        #点击、进入提现   企业转账只能转账到支付宝，转账到银行卡只能用提现
        driver.find_element_by_xpath('//*[@id="react-content"]/div/div[2]/div[2]/div[1]/div/a[3]').click()
        #输入提现
        price=float(price)/2
        driver.find_element_by_xpath('//*[@id="J_paymentToBankCardAmount"]').send_keys(price)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="J_formSubmitButton"]').click()
        #进入输入密码界面
        driver.find_element_by_xpath("//*[@id='payPassword_rsainput']").click()
        for p in zpassw:
            t3=random.randint(1,3)
            time.sleep(t3)
            driver.switch_to.active_element.send_keys(p)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        driver.refresh()
        time.sleep(1)
        result=u"转账记录"
        if tagname_iselement(result):
            print "tixian success"
    else:
        driver=webdriver.Chrome()
        driver.get('https://auth.alipay.com/login/index.htm')
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='J-loginMethod-tabs']/li[2]").click()
        print "yes1"
        for i in user:
            t=random.randint(1,3)
            print i
            time.sleep(t)
            driver.find_element_by_xpath("//*[@id='J-input-user']").send_keys(i)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='J-input-user']").send_keys(Keys.TAB)
        time.sleep(1)
        for p in  passw:
            t2=random.randint(1,3)
            time.sleep(t2)
            driver.switch_to.active_element.send_keys(p)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@type='submit']").click()
        print "login success"
        time.sleep(3)
        #点击、进入资金管理界面
        driver.find_element_by_xpath('//*[@id="react-content"]/div/div[1]/div[2]/div/div[4]/div[1]/div/div[4]/div/a').click()
        windows=driver.window_handles
        driver.switch_to.window(windows[-1])
        #获取当前金额
        price=driver.find_element_by_xpath('//*[@id="react-content"]/div/div[2]/div[2]/div[1]/span/div[1]/div[2]').text
        #点击、进入转账
        driver.find_element_by_xpath('//*[@href="https://bizfundprod.alipay.com/payment/transfer/index.htm"').click()
        windows=driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.find_element_by_link_text(u'转账到银行卡').click()

        yinhang = u"中国建设银行"
        yinhangzhanghu = "6217001540022416380"
        kaihuhang = u"付贵炉"
        price=price/2
        # 银行
        driver.find_element_by_xpath('//*[@id="bankName"]').send_keys(yinhang)
        driver.find_element_by_xpath('//*[@id="bankName"]').send_keys(Keys.TAB)
        # 银行卡号
        driver.find_element_by_xpath('//*[@id="bankCardNo"]').send_keys(yinhangzhanghu)
        driver.find_element_by_xpath('//*[@id="bankCardNo"]').send_keys(Keys.TAB)
        # 开户人姓名
        driver.find_element_by_xpath('//*[@name="optCardName"]').send_keys(yinhangzhanghu)
        driver.find_element_by_xpath('//*[@name="optCardName"]').send_keys(Keys.TAB)
        #金额
        driver.find_element_by_xpath('//*[@id="amount"').send_keys(price)
        driver.find_element_by_xpath('//*[@id="amount"').send_keys(Keys.TAB)
        #提交
        driver.find_element_by_xpath('//*[@type="submit"').click()
        windows=driver.window_handles
        driver.switch_to.window(windows[-1])
