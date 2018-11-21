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

driver = webdriver.Chrome()

#获取 admin 商户列表中 代付利润提现号中的备付金
beifu=merchant()
bf=beifu.cash()


#获取账户管理信息并记录
a=account()
a=a.account()
print a

# 提现
# channel="//*[contains(@onclick,'ids=272')]"  #DDP 渠道
channel="//*[contains(@onclick,'cashnew.html?ids=253')]"#XFP 渠道
c=cash()
amount = 2
c.cash(channel,amount)

driver.refresh()
#再次获取账户管理信息并记录
a2=account()
a2=a2.account()
print a2
a2[2]=float(a2[2])-7
a2[3]=float(a2[3])-7
a2[8]=float(a2[8])+2
if a==a2:
    print "account true"
else:
    print  "account false"

#再次 获取 admin 商户列表中 代付利润提现号中的备付金
beifu2=merchant()
bf2=beifu.cash()
bf2[0]=float(bf2[0])-7
bf2[1]=float(bf2[1])+1

