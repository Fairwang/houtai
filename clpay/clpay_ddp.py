#!user/bin/python
# coding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image,ImageEnhance
import pytesseract
from selenium import webdriver
import time
# from array import *
import numpy as np
#  Numpy
import numpy
import cv2
from code.common import table



driver=webdriver.Chrome()
driver.get('https://testpay.hongnaga.com/merchant.html')
# driver.get("https://pay.hongnaga.com/merchant/login")
# driver.get('https://cpay.hypayde.com/merchant')
# driver.get('http://47.75.86.174:8092/posa/merlogin.jsp')
driver.maximize_window()
driver.find_element_by_id("mch_id").clear()
driver.find_element_by_id("mch_id").send_keys(12001)
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys(123456)
# driver.find_element_by_id("password").send_keys("chilong123456")
driver.find_element_by_id("captcha").send_keys(0)
driver.find_element_by_id("sub").click()
time.sleep(10)
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
# print zhgl_table[3][3]
for i in range(len(zhgl_table)):
    if zhgl_table[i][2]==zhgl_table[i][3]+zhgl_table[i][10]:#总金额=可用余额+手续费
        if zhgl_table[i][3]==zhgl_table[i][4]+zhgl_table[i][6]:#可用余额=可提现金额+待结算金额
            print"%s入金账户对账信息准确"%zhgl_table[i][1]








