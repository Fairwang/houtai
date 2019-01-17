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
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from PIL import Image,ImageEnhance
import pytesseract
import time
import numpy as np
import cv2
import json
from houtai.zijinguiji.tx_yinshua import tx_yinshua

def linktext_iselement(element):
    flag=True
    try:
        driver.find_element_by_link_text(element)
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
        flag=False
        return flag

def get_track(distance):

    '''
    拿到移动的轨迹，模仿人的滑动行为，先加速后匀减速
    匀变速运动基本公式：
    v=v0+at
    s=v0t+(1/2)att
    v*v-v0*v0=2as

    :param distance: 需要移动的距离
    :return: 存放每0.2秒移动的距离
    '''
    v=0
    t=0.2

    tracks=[]   #位移
    current=0   #当前位移
    mid=distance*2/3    #到达mid 开始减速
    while current < distance:
        if current< mid:
            a=random.randint(1,4)   #加速运动
        else:
            a=-random.randint(2,5)  #减速运动
        v0=v
        s=v0*t+0.5*a*(t**2)
        current+=s
        tracks.append(round(s)) #添加到轨迹列表
        v=v0+a*t
    return tracks

def erzhihua(fiepath):
    #处理图片
    img = Image.open(fiepath).convert('L')  # 二ZZZ值化
    img = ImageEnhance.Contrast(img)  # 增强对比度
    img = img.enhance(2.0)  # 增加饱和度
    # w,h=img.size
    x=0
    y=0
    img.save('./tupian/daichuli.png')
    img = np.array(Image.open('./tupian/daichuli.png'))
    h, w = img.shape[:2]
    for y in range(1, w-1):
        for x in range(1, h-1 ):
            count = 0
            # cur_pixel = easy_img.getpixel((x, y+1))
            # print"当前像素：%s"%cur_pixel
            if img[x, y ] > 127:
                img[x, y] = 0
            else:
                img[x,y] =255
    cv2.imwrite('./tupian/yichuli.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    time.sleep(1)


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
        #账户为邮箱  视为公司账户，只能转到对公账户多绑定的银行卡，否则只能绑定成功，不能转账成功
        #已经绑定银行卡
        time.sleep(2)
        driver=webdriver.Chrome()
        driver.get('https://auth.alipay.com/login/index.htm')
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='J-loginMethod-tabs']/li[2]").click()
        print "yes1"
        for i in user:
            t=random.randint(1,3)
            # print i
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
        # bind=u'添加银行账户'#定位不到 定位上级试试
        bind='seed="miNoticeTitle-miButtonT1"'
        if xpath_iselement(bind):
            #未绑定银行卡，需要先绑定银行卡
            # bind2 = 'seed="miNoticeTitle-miButtonT1"'
            driver.find_element_by_xpath(bind).click()
            driver.refresh()
            yinhangzhanghu="6217001540022416380"
            yinhang=u"中国建设银行"
            kaihuhang=u"西溪支行"
            #银行账户
            for p in yinhangzhanghu:
                y = random.randint(1, 3)
                time.sleep(y)
                driver.find_element_by_xpath('//*[@id="J_card"]').send_keys(p)
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
            driver.find_element_by_xpath('//*[@title="杭州市"]').click()#杭州市
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
        #已经绑定银行卡
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
        if linktext_iselement(result):
            print "tixian success"
    else:
        #账号为个人，转账到个人
        driver=webdriver.Chrome()
        driver.get('https://auth.alipay.com/login/index.htm')
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='J-loginMethod-tabs']/li[2]").click()
        print "yes1"
        for i in user:
            t=random.randint(1,3)
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
        wait_text = '//*[@class="wait-text"]'
        # wait_text=u'顾客太多，客官请稍候'
        if xpath_iselement(wait_text):
            time.sleep(1)
            driver.find_element_by_xpath('//*[@href="https://www.alipay.com/"]').click()
            time.sleep(1)
            driver.refresh()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@class="personal-login"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@href="https://my.alipay.com/portal/i.htm"]').click()

        time.sleep(1)
        #获取当前金额
        driver.find_element_by_xpath('//*[@class="show-text"]').click()
        time.sleep(1)
        price=driver.find_element_by_xpath('//*[@id="account-amount-container"]').text
        price=price.split('.')[0]
        print price
        #点击、进入转账
        driver.find_element_by_xpath('//*[@title="转账"]').click()
        time.sleep(6)
        #点击、进入转账
        # driver.find_element_by_link_text('转账到银行卡').click()
        # driver.find_element_by_xpath('//*[@data-id="10053"]').click()#定位不到转账银行卡这一级
        driver.find_elements_by_xpath('//*[@class="myapp-item  fn-clear"]')[1].click()#定位银行卡上一级 定位成功
        yinhang = u"中国建设银行"
        yinhangzhanghu = "6217001540022416380"
        kaihuhang = u"付贵炉"
        price=10
        # 银行
        driver.find_element_by_xpath('//*[@id="bankName"]').send_keys(yinhang)
        driver.find_element_by_xpath('//*[@id="bankName"]').send_keys(Keys.TAB)
        # 银行卡号
        driver.find_element_by_xpath('//*[@id="bankCardNo"]').send_keys(yinhangzhanghu)
        driver.find_element_by_xpath('//*[@id="bankCardNo"]').send_keys(Keys.TAB)
        # 开户人姓名
        driver.find_element_by_xpath('//*[@name="optCardName"]').send_keys(kaihuhang)
        driver.find_element_by_xpath('//*[@name="optCardName"]').send_keys(Keys.TAB)
        #金额
        driver.find_element_by_xpath('//*[@id="amount"]').send_keys(price)
        driver.find_element_by_xpath('//*[@id="amount"]').send_keys(Keys.TAB)
        time.sleep(2)
        #提交
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        time.sleep(1)
        #验证码界面，滑动验证，点击验证码
        huakuai=driver.find_element_by_xpath('//*[@class="nc_iconfont btn_slide"]')
        print"点击活动按钮"
        ActionChains(driver).click_and_hold(on_element=huakuai).perform()
        time.sleep(1)
        print "开始拖动"
        huaban=driver.find_element_by_xpath('//*[@id="nc_1_n1t"]')
        distanceh=huaban.size
        print  distanceh   #滑板长度
        track_list=get_track(distanceh['width'])
        for track  in track_list:
            ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()  #开始移动到当前xy
            time.sleep(0.005)
        ActionChains(driver).release(on_element=huakuai).perform()
        time.sleep(2)

        yes_text='//*[@data-nc-lang="_yesTEXT"]'
        while not xpath_iselement(yes_text):    #验证通过不存在 进行点选汉字
            #获取需要点击的汉字
            time.sleep(5)
            hanzi=driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/i').text    # “词”
            print type(hanzi)   #unicode
            hanzi=hanzi.split(u'“')[1].split(u'”')[0] #分割出需要被识别的汉字  词
            print "hanzi: %s"%hanzi
            print type(hanzi)
            #截图点选汉字图片
            img=driver.find_element_by_tag_name('img')
            size=img.size
            print "size:%s"%size          #size:{'width': 230, 'height': 230}
            location=img.location   #location:{'y': 563.0, 'x': 311.0}
            print "location:%s"%location
            print type(location)    #<type 'dict'>

            driver.save_screenshot('./tupian/datu.png')
            rangle = (int(location['x']), \
                      int(location['y']), \
                      int(location['x'] + size['width']), \
                      int(location['y'] + size['height']))
            png = Image.open('./tupian/datu.png')
            png2 = png.crop(rangle)
            pic = png2.save('./tupian/xiaotu.png')
            #处理图片
            # erzhihua('./tupian/xiaotu.png')
            #处理图片/识别汉字,引入tx_yinshua模块
            hanzi_location=tx_yinshua(hanzi,'./tupian/xiaotu.png')    #{'x':121,'y':197}
            print"hanzi_location:%s" %hanzi_location
            if hanzi_location!=None:
                time.sleep(2)
                print "zheli"
                ActionChains(driver).move_to_element_with_offset(img,hanzi_location["x"],hanzi_location["y"]).click().perform()
                time.sleep(3)

            else:
                time.sleep(2)
                ActionChains(driver).move_to_element_with_offset(img, "-100","-100").click().perform()
                time.sleep(3)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@value="确认信息并付款"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="payPassword_container"]').click()
        for z in zpassw:
            time.sleep(random.randint(1,3))
            driver.switch_to_active_element().send_keys(z)
        driver.find_element_by_xpath('//*[@id="J_authSubmit"]').click()
        time.sleep(1)
        already_pay='//*[@class="notice-box  notice-success  fn-clear"]'
        if xpath_iselement(already_pay):
            print "银行卡转账提交成功"
        else:
            print "银行卡转账提交失败"







