#!/user/bin/python
# -*-coding:utf-8-*-
import base_page
from selenium.webdriver.common.by import By


class creat_page(base_page.BaseAaction):
    def __init__(self,driver):
        self.driver=driver

# 登录界面

    user_loc=(By.ID,'email')
    pws_loc=(By.ID,'password')
    cap_loc=(By.ID,'password')
    login_loc=(By.ID,'sub')
    def input_user(self,username):
        self.send_keys(username,*self.user_loc)
    def input_pws(self,password):
        self.send_keys(password,*self.pws_loc)
    def click_login(self):
        self.click(*self.login_loc)


#C2C配置_账号编辑
    C2C_loc=(By.LINK_TEXT,"C2C配置")
    app_loc=(By.LINK_TEXT,"APP账号")
    appiframe_loc=(By.XPATH,"//*[contains(@src,'merchant_app/index.html')]")#app账号页面的iframe
    app_edit_loc=(By.XPATH,"//*[contains(@onclick,'10086.html')]")#点击编辑按钮
    edit_iframe_loc=(By.XPATH,"//*[contains(@src,'edit/id/10086.html')]")#app账号中的APP账号编辑页面iframe
    # paytype_loc=(By.ID,'')

    def click_C2C(self):
        self.click(*self.C2C_loc)
    def click_app(self):
        self.click(*self.app_loc)
    def app_iframe(self):
        self.iframe(*self.appiframe_loc)
    def app_edit(self):
        self.click(*self.app_edit_loc)
    def edit_iframe(self):
        self.iframe(*self.edit_iframe_loc)

#APP账号-APP账号列表-某个app账号的编辑
    app_name_loc=(By.NAME,"name")
    app_key_loc=(By.NAME,"app_key")
    app_ali_chosen=(By.CLASS_NAME,"chosen-single")

    def edit_name(self,app_name):
        self.send_keys(app_name,*self.app_name_loc)

    def edit_app_key(self,app_key):
         self.send_keys(*self.app_key_loc)








