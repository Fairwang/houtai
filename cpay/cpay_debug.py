#!user/bin/python
# coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
# from houtai.lk import cpay_database
import MySQLdb
#将数据库中expire_time>0,改为等于0
#支付demo界面:输入密码成功登录后，输入主商户号、子商户号，选择支付方式，输入金额，点击提交
#从diandian_pay.txt中取出金额，传入金额



def query_database(sql):
    # coon = MySQLdb.connect(host='cpaytest.tinywan.com', user='root', passwd='123456', db='cpay', port=3306,
    #                        charset='utf8')
    # cursor = coon.cursor()

    coon = MySQLdb.connect(host='cpay.hypayde.com', user='root', passwd='root123456', db='cl_cpay', port=3306,
                           charset='utf8')

    cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
    try:
        cur = cursor.execute(sql)
        rows = cursor.fetchall()
        price = []
        # print rows
        for row in rows:
            # print row["price"]
            price.append(row["price"])
        # print rows
        return price
    except:
        print "Error: This is except"
        # coon.commit()
    coon.close()


update = "update cl_merchant_qrcode set expire_time=0 where mch_id=1006 and expire_time>0 "
query_database(update)
time.sleep(2)
driver = webdriver.Chrome()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("http://cpaytest.tinywan.com/index/demo/index.html?debug=true")

driver.get("https://cpay.hypayde.com/demo.html?debug=true")
a=driver.switch_to.alert
a.send_keys("112233")
a.accept()

price1 = "SELECT price FROM `cl_merchant_qrcode`where mch_id=1006  and  expire_time=0 and price>90"
prices = query_database(price1)
# print type(prices)
time.sleep(3)
i = 1
# f1 = open("D:\\zxtest\\diandian_pay.txt", 'r')
# while True:
    # price = f1.readline()
    # if price=='':
    #     break
for price in prices:
    # print type(price)

    price = str(price)
    time.sleep(3)
    driver.implicitly_wait(3)
    driver.find_element_by_name("mch_id").clear()
    driver.find_element_by_name("mch_id").send_keys(1006)
    driver.find_element_by_name("sub_mch_id").clear()
    driver.find_element_by_name("sub_mch_id").send_keys(6020)

    pay_type=Select(driver.find_element_by_id("pay_type"))
    pay_type.select_by_value("5")

    driver.find_element_by_name("price").clear()#金额
    driver.find_element_by_name("price").send_keys(price)

    driver.find_element_by_id("pay").click()
    print i
    i = i + 1
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    time.sleep(1)
    print driver.title
    if i > 20:
        driver.quit()
        print"success"
        break
