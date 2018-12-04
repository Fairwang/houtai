#!user/bin/python
# coding: utf-8

from selenium import webdriver

#商户后台  账户管理获取数据，记录   admin 18482  备付金利润数据记录   admin 代付商户 备付金美付宝余额等数据记录

# 商户后台 账户管理 提现
#对比提现后的账户管理数据
# 对比 admin 18482数据 对比admin代付商户备付金等数据

from clpay_cash import cash
from clpay_account import  account
from code.common import table
from merchant import merchant
from profit_cash import profit_cash
import time

driver = webdriver.Chrome()

#获取 admin 商户列表中 代付利润提现号中的备付金
beifu=merchant(driver)
bf=beifu.cash()
print "....bf%s"%bf
time.sleep(2)
#获取 admin 代付商户列表中的美付宝利润

meifubao=profit_cash(driver)
mfb=meifubao.profit_cash()
print "....mfb%s"%mfb
time.sleep(2)
#获取账户管理信息并记录
a=account(driver)
a=a.account()
print "....a%s"%a
time.sleep(2)
# 提现
# channel="//*[contains(@onclick,'ids=272')]"  #DDP 渠道
channel="//*[contains(@onclick,'cashnew.html?ids=253')]"#XFP 渠道
# channel="//*[contains(@onclick,'cashnew.html?ids=311')]"#DDCP 渠道
c=cash(driver)
amount = 2
c=c.cash(channel,amount)
print "提现成功"

time.sleep(2)
#再次获取账户管理信息并记录
a2=account(driver)
a2=a2.account()
print "a2%s"%a2
a2[2]=float(a2[2])-7
a2[3]=float(a2[3])-7
a2[8]=float(a2[8])+2
if a==a2:
    print "account true"
else:
    print  "account false"
time.sleep(2)
#再次 获取 admin 商户列表中 代付利润提现号中的备付金
beifu2=merchant(driver)
bf2=beifu.cash()
print "bf2%s"%bf2

bf2[0]=float(bf2[0])-7
bf2[1]=float(bf2[1])+1
if bf==bf2:
    print "admin 商户列表 true"
else:
    print  "admin 商户列表 false"

time.sleep(2)
#获取 admin中代付列表中的利润
meifubao=profit_cash(driver)
mfb2=meifubao.profit_cash()
print "mfb2%s"%mfb2
mfb2[0]=float(mfb2[0])-2
mfb2[1]=float(mfb2[1])-7
mfb2[2]=float(mfb2[2])+1
mfb2[3]=float(mfb2[3])
mfb2[4]=float(mfb2[4])+3
mfb2[5]=mfb2[5]
mfb2[6]=mfb2[6]+3
if bf==bf2:
    print "admin 代付列表 true"
else:
    print  "admin 代付列表 false"



