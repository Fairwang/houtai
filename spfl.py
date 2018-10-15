#!user/bin/python
# coding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
#
# driver=webdriver.Firefox()#初始化一个火狐浏览器实例
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://www.baidu.com/")
# driver.execute_script("alert('这是一个alert弹框')")
# text=driver.switch_to_alert().text #获取弹窗框里面的文字
# assert "alert" in text
# print "alert"
# time.sleep(5)
# driver.switch_to_alert().accept()
#
# driver.execute_script("confirm('这是一个confirm弹框')")
# time.sleep(5)
# text=driver.switch_to_alert().text #获取弹窗框里面的文字
# assert "confirm" in text
# print "confirm not alert"
# print text
# driver.switch_to_alert().dismiss()
# time.sleep(2)
#
# driver.execute_script("prompt('这是一个prompt弹框','智')")
# time.sleep(5)
# text=driver.switch_to_alert() .text
# assert u"一个" in text
# print u"智在"
# #driver.switch_to_alert().dismiss()
# time.sleep(5)
# #text=driver.switch_to.alert().text TypeError: 'Alert' object is not callable
# # driver.quit()

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
#登录网页
driver.get("http://jdshop.shopjian.cn/public/admin/index/login?url=/public/admin/dashboard?ref=addtabs")
driver.find_element_by_id("pd-form-username").clear()
driver.find_element_by_id("pd-form-username").send_keys("18042311448")
driver.find_element_by_id("pd-form-password").clear()
driver.find_element_by_xpath("//input[@id='pd-form-password']").send_keys('123456')

#
driver.implicitly_wait(2)
driver.find_element_by_tag_name("button").click()
time.sleep(15)
driver.find_element_by_link_text("商品管理").click()
# iframe=driver.find_element_by_xpath("//div/iframe")
#选择营销活动
#
# spgl=(By.LINK_TEXT,"商品管理")
# WebDriverWait(driver,20).until(EC.presence_of_element_located(spgl))
# time.sleep(2)

# driver.find_element_by_link_text("商品管理").click()
# driver.implicitly_wait(1)
time.sleep(2)
driver.find_element_by_link_text("分类管理").click()
time.sleep(2)
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
# driver.switch_to.frame("iframe")
#切换到iframe
frame_xpath=driver.find_element_by_xpath("//iframe[contains(@src,'category')]")
driver.switch_to.frame(frame_xpath)
# print frame_xpath
# frame_xpath=driver.find_element_by_xpath("//div/div/div/iframe")
# frame_xpath=driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/iframe")
# a=driver.switch_to.frame(frame_xpath).get_attribute("height")
# print a
# driver.switch_to.frame(2)
# paymentpreference

time.sleep(3)
driver.find_element_by_class_name('btn-add').click()
time.sleep(3)
# 切换到添加页面
add_path=driver.find_element_by_xpath("//iframe[contains(@src,'add?dialog')]")
driver.switch_to.frame(add_path)
driver.find_element_by_class_name('pull-left').click()
time.sleep(3)
ajfl=driver.find_elements_by_tag_name('li')#选择分类
ajfl[2].click()
driver.implicitly_wait(3)
time.sleep(3)
driver.find_element_by_id('c-name').send_keys("123")
driver.implicitly_wait(3)
driver.switch_to.parent_frame()
driver.find_element_by_class_name('btn-embossed').click()
time.sleep(3)
# 获得table中的list
table=driver.find_element_by_id("table")
trs=table.find_elements_by_tag_name('tr')
tr=trs.pop(-1).click()
driver.implicitly_wait(3)
tds=driver.find_elements_by_class_name('btn-delone')
print tds
driver.implicitly_wait(3)
tds.pop(-1).click()
# driver.switch_to.alert().accept()
time.sleep(1)
driver.find_element_by_class_name("layui-layer-btn0").click()#确定删除
time.sleep(3)

driver.switch_to.default_content()
driver.find_element_by_xpath("//*[@href='/public/admin/goods/goods']").click()
time.sleep(3)

driver.find_element_by_xpath("//*[@placeholder='搜索菜单']").send_keys(u"管理")#
time.sleep(3)

driver.find_element_by_xpath("//*[@data-url='/public/admin/company/shoptable']").click()#隐藏参数
time.sleep(3)

driver.find_element_by_id("search-btn").click()
zt=driver.find_element_by_xpath("//*[contains(@src,'shoptable?addtabs=1')]")
driver.switch_to.frame(zt)
driver.find_element_by_id("b.name").send_keys(u"台桌")
driver.find_element_by_class_name("btn-success").click()
time.sleep(2)
# tr2=driver.find_elements_by_tag_name("tr")
# tr2[2].click()
td2=driver.find_elements_by_class_name("fa-pencil")
td2[2].click()
time.sleep(5)
driver.switch_to.default_content()






