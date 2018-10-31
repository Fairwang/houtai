#!/user/bin/python
#  -*-coding: utf-8-*-
from PIL import Image,ImageEnhance
import pytesseract
from selenium import webdriver
import time
# import cv2
import numpy
#支付demo界面
driver=webdriver.Chrome()
driver.get('https://testpay.hongnaga.com/merchant.html')
# driver.get('https://cpay.hypayde.com/merchant')
# driver.get('http://47.75.86.174:8092/posa/merlogin.jsp')
driver.maximize_window()
driver.save_screenshot('D:\\code\\code.png')

id=driver.find_element_by_id("captcha_img")
# id=driver.find_element_by_id("randImage")
size=id.size
location=id.location
rangle=(int(location['x']),\
        int(location['y']), \
        int(location['x']+size['width']), \
        int(location['y']+size['height']))
png=Image.open('D:\\code\\code.png')
png2=png.crop(rangle)
png3=png2.save('D:\\code\\code2.png')
time.sleep(5)
png4=Image.open('D:\\code\\code2.png')
png5=png4.convert('L')#二值化
img=png5.save('D:\\code\\code22.png')
# img=pytesseract.image_to_string(png6)#使用image_to_string识别验证码
# print "png999 %s"%img

h, w = img.shape[:2]
# ！！！opencv矩阵点是反的
# img[1,2] 1:图片的高度，2：图片的宽度
for y in range(1, w - 1):
        for x in range(1, h - 1):
                count = 0
                if img[x, y - 1] > 245:
                        count = count + 1
                if img[x, y + 1] > 245:
                        count = count + 1
                if img[x - 1, y] > 245:
                        count = count + 1
                if img[x + 1, y] > 245:
                        count = count + 1
                if count > 2:
                        img[x, y] = 255
png7=img.save('E://yanzhengma7.png')
x=0;y=0
cur_pixel = png7[x, y]  # 当前像素点的值
height, width = img.shape[:2]
for y in range(0, width - 1):
        for x in range(0, height - 1):
                if y == 0:  # 第一行
                        if x == 0:  # 左上顶点,4邻域
                                # 中心点旁边3个点
                                sum = int(cur_pixel) \
                                      + int(img[x, y + 1]) \
                                      + int(img[x + 1, y]) \
                                      + int(img[x + 1, y + 1])
                                if sum <= 2 * 245:
                                        img[x, y] = 0
                        elif x == height - 1:  # 右上顶点
                                sum = int(cur_pixel) \
                                      + int(img[x, y + 1]) \
                                      + int(img[x - 1, y]) \
                                      + int(img[x - 1, y + 1])
                                if sum <= 2 * 245:
                                        img[x, y] = 0
                        else:  # 最上非顶点,6邻域
                                sum = int(img[x - 1, y]) \
                                      + int(img[x - 1, y + 1]) \
                                      + int(cur_pixel) \
                                      + int(img[x, y + 1]) \
                                      + int(img[x + 1, y]) \
                                      + int(img[x + 1, y + 1])
                                if sum <= 3 * 245:
                                        img[x, y] = 0
                elif y == width - 1:  # 最下面一行
                        if x == 0:  # 左下顶点
                                # 中心点旁边3个点
                                sum = int(cur_pixel) \
                                      + int(img[x + 1, y]) \
                                      + int(img[x + 1, y - 1]) \
                                      + int(img[x, y - 1])
                                if sum <= 2 * 245:
                                        img[x, y] = 0
                        elif x == height - 1:  # 右下顶点
                                sum = int(cur_pixel) \
                                      + int(img[x, y - 1]) \
                                      + int(img[x - 1, y]) \
                                      + int(img[x - 1, y - 1])
                                if sum <= 2 * 245:
                                        img[x, y] = 0
                        else:  # 最下非顶点,6邻域
                                sum = int(cur_pixel) \
                                      + int(img[x - 1, y]) \
                                      + int(img[x + 1, y]) \
                                      + int(img[x, y - 1]) \
                                      + int(img[x - 1, y - 1]) \
                                      + int(img[x + 1, y - 1])
                                if sum <= 3 * 245:
                                        img[x, y] = 0
                else:  # y不在边界
                        if x == 0:  # 左边非顶点
                                sum = int(img[x, y - 1]) \
                                      + int(cur_pixel) \
                                      + int(img[x, y + 1]) \
                                      + int(img[x + 1, y - 1]) \
                                      + int(img[x + 1, y]) \
                                      + int(img[x + 1, y + 1])
                                if sum <= 3 * 245:
                                        img[x, y] = 0
                        elif x == height - 1:  # 右边非顶点
                                sum = int(img[x, y - 1]) \
                                      + int(cur_pixel) \
                                      + int(img[x, y + 1]) \
                                      + int(img[x - 1, y - 1]) \
                                      + int(img[x - 1, y]) \
                                      + int(img[x - 1, y + 1])
                                if sum <= 3 * 245:
                                        img[x, y] = 0
                        else:  # 具备9领域条件的
                                sum = int(img[x - 1, y - 1]) \
                                      + int(img[x - 1, y]) \
                                      + int(img[x - 1, y + 1]) \
                                      + int(img[x, y - 1]) \
                                      + int(cur_pixel) \
                                      + int(img[x, y + 1]) \
                                      + int(img[x + 1, y - 1]) \
                                      + int(img[x + 1, y]) \
                                      + int(img[x + 1, y + 1])
                                if sum <= 4 * 245:
                                        img[x, y] = 0
png8=png7.save('E://yanzhengma8.png')
img111=pytesseract.image_to_string(png8)#使用image_to_string识别验证码
print "png999 %s"%img111

