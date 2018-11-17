#!user/bin/python
# coding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time


from code.common import table


class zhgli():

    driver=webdriver.Chrome()
    driver.get('https://testpay.hongnaga.com/merchant.html')
    # driver.get("https://pay.hongnaga.com/merchant/login")
    # driver.get('https://cpay.hypayde.com/merchant')
    # driver.get('http://47.75.86.174:8092/posa/merlogin.jsp')
    # driver.maximize_window()
    driver.find_element_by_id("mch_id").clear()
    driver.find_element_by_id("mch_id").send_keys(12001)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(123456)
    # driver.find_element_by_id("password").send_keys("chilong123456")
    driver.find_element_by_id("captcha").send_keys(0)
    driver.find_element_by_id("sub").click()
    time.sleep(5)
    #手动输入验证码

    time.sleep(2)
    driver.find_element_by_link_text("账户管理").click()
    driver.find_element_by_xpath("//*[contains(@data-index,'6')]").click()
    #切换到账户管理页面
    frame_xpath=driver.find_element_by_xpath("//*[contains(@name,'iframe6')]")
    driver.switch_to.frame(frame_xpath)
    time.sleep(1)
    zhgl=table.get_table(driver)
    zhgl_table=zhgl.get_table_content("list")
    time.sleep(3)
    zhgl_table=zhgl_table[1:]
    print "zhgl_table is\n %s "%zhgl_table
    zhsz=zhgl_table[:]
    print zhsz
    for i in range(len(zhgl_table)):
        k= 0
        for j in range(len(zhgl_table[i])):
            if j in (1,11):
                del zhsz[i][j-k]##删除成功后，j所在list总长度会减1
                k=k+1
    print"a在这里啊：%s" %zhsz
    # time.sleep(2)
    l=zhsz[8]
    # for l in range(len(zhsz)):
    if float(zhsz[l][1])==float(zhsz[l][2])+float(zhsz[l][9]):#总金额=可用余额+手续费
        if float(zhsz[l][2])==float(zhsz[l][3])+float(zhsz[l][5]):#可用余额=可提现金额+待结算金额
            print"yes:%s"%zhsz[l][0]
    else:
        print"faile:%s"%zhsz[l][0]

    
zh=zhgli()






