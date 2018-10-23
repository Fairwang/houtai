#!/user/bin/python
#  -*-coding: utf-8-*-

from PIL import Image,ImageEnhance
import pytesseract
from selenium import webdriver
import time
# import cv2

#支付demo界面
driver=webdriver.Chrome()
# driver.get('https://testpay.hongnaga.com/merchant.html')
# driver.get('https://cpay.hypayde.com/merchant')
driver.get('http://47.75.86.174:8092/posa/merlogin.jsp')
driver.maximize_window()
driver.save_screenshot('E://yanzhengma.png')

# id=driver.find_element_by_id("captcha_img")
id=driver.find_element_by_id("randImage")
size=id.size
location=id.location
print  size,location
rangle=(int(location['x']),\
        int(location['y']), \
        int(location['x']+size['width']), \
        int(location['y']+size['height']))
png=Image.open('E:yanzhengma.png')
png2=png.crop(rangle)
png3=png2.save('E://yanzhengma3.png')
time.sleep(5)
png4=Image.open('E://yanzhengma3.png')
png5=png4.convert('L')#二值化
png6=png5.save('E://yanzhengma6.png')
# png999=pytesseract.image_to_string(png5)#使用image_to_string识别验证码
# print "png999 %s"%png999
# data=png5.getdata()
# w,h=png5.size
# print w,h
# png5.show()
# black_point = 0
#
# for x in xrange(2,w-1,4):
#     for y in xrange(2,h-1,4):
#         mid_pixel = data[y+x] #中央像素点像素值
#         if mid_pixel == 0: #找出上下左右四个方向像素点像素值
#             top_pixel = data[(y-4)+x]
#             left_pixel = data[y+(x-4)]
#             down_pixel = data[(y+4)+x]
#             right_pixel = data[y+(x+4)]
#             #判断上下左右的黑色像素点总个数
#             if top_pixel == 0:
#                 black_point += 1
#             if left_pixel == 0:
#                 black_point += 1
#             if down_pixel == 0:
#                 black_point += 1
#             if right_pixel == 0:
#                 black_point += 1
#             if black_point >= 4:
#                 png5.putpixel((x,y),0)
#             #print black_point
#             black_point = 0
# png7=png5.save('E://yanzhengma7.png')
# png5.show()
# png6=png5.save('E://yanzhengma6.png')

# png6=png5.save('E://yanzhengma6.png')
# time.sleep(3)
# # sharpness=ImageEnhance.Contrast(png5)
# # png6= sharpness.enhance(4)
# # png7=png6.save('E://yanzhengma6.png')
#
# # sharp_img=sharpness.enhance(2.0)
# # png6=png5.save('E://yanzhengma6.png')
# # png5=cv2.imread('E://yanzhengma3.png')
# # png6=cv2.cvtColor(png5,cv2.COLOR_BGR2GRAY)
# # out =png5.point(table,'1')
# #

# png999=pytesseract.image_to_string(png7)#使用image_to_string识别验证码
# print "png777 %s"%png999

# def pIx(data):
        # data=self.Im
#图片的长宽
# data=png5
# w=size['width']
# h=size['height']
#         data=a
#         w=a.size["width"]
#         h=a.size['height']
#data.getpixel((x,y))获取目标像素点颜色。
#data.putpixel((x,y),255)更改像素点颜色,255代表颜色。


# try:
# for x in xrange(1,w-1):
#         if x>1 and x!=w-2:
# #获取目标像素点左右位置
#             left=x-1
#             right=x+1
#
#             for y in xrange(1,h-1):
#     #获取目标像素点上下位置
#                 up=y-1
#                 down=y+1
#
#                 if x<=2 or x>=(w-2):
#                     data.putpixel((x,y),255)
#
#                 elif y<=2 or y>=(h-2):
#                     data.putpixel((x,y),255)
#
#                 elif data.getpixel((x,y))==0:
#                     if y>1 and y!=h-1:
#
# #以目标像素点为中心点,获取周围像素点颜色
# #0为黑色,255为白色
#                         up_color=data.getpixel((x,up))
#                         down_color=data.getpixel((x,down))
#                         left_color=data.getpixel((left,y))
#                         left_down_color=data.getpixel((left,down))
#                         right_color=data.getpixel((right,y))
#                         right_up_color=data.getpixel((right,up))
#                         right_down_color=data.getpixel((right,down))
# #去除竖线干扰线
#                         if down_color==0:
#                             if left_color==255 and left_down_color==255 and right_color==255 and right_down_color==255:
#                                 data.putpixel((x,y),255)
# #去除横线干扰线
#                         elif right_color==0:
#                             if down_color==255 and right_down_color==255 and up_color==255 and right_up_color==255:
#                                 data.putpixel((x,y),255)
#     #去除斜线干扰线
#                         if left_color==255 and right_color==255 and up_color==255 and down_color==255:
#                             data.putpixel((x,y),255)
#                         else:
#                              pass
#
# #保存去除干扰线后的图片
#                         data.save("E://test.png","png")
# except:
#         print "except raise"

