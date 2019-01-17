#!/user/bin/python
#  -*-coding: utf-8-*-

from selenium import webdriver
import time
import json

# hanzi=u"“心”"#unicode
# # print hanzi
# # hanzi=hanzi.encode('gbk')
# # print type(hanzi)
# print hanzi
# # hanzi = hanzi.split('“')[1].split('”')[0]  # 分割出需要被识别的汉字  #UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 0: ordinal not in range(128)
# hanzi = hanzi.split(u'“')[1].split(u'”')[0]
# print hanzi
# # hanzi="心" #str
# # hanzi2=u"心"#unicode
# # hanzi_unicode=hanzi2.encode('gbk')
# # print type(hanzi)
# # print type(hanzi2)
# # print type(hanzi_unicode)
# # a={"code":0,"message":"OK","data":{"recognize_warn_msg":[],"recognize_warn_code":[],"items":[{"itemcoord":{"x":22,"y":36,"width":87,"height":26},"words":[{"character":"么","confidence":0.6924936175346375},{"character":"上","confidence":0.9979987740516664},{"character":"抑","confidence":0.6606981754302979},{"character":"油","confidence":0.9161732792854308}],"itemstring":"么上抑油"},{"itemcoord":{"x":128,"y":118,"width":90,"height":26},"words":[{"character":"以","confidence":0.9816042184829712},{"character":"必","confidence":0.50948566198349},{"character":"当","confidence":0.8555372953414917},{"character":"镜","confidence":0.9988377690315248}],"itemstring":"以必当镜"},{"itemcoord":{"x":101,"y":187,"width":80,"height":20},"words":[{"character":"创","confidence":0.4055652618408203},{"character":"您","confidence":0.722910463809967},{"character":"之","confidence":0.9305914044380188},{"character":"心","confidence":0.8593043088912964}],"itemstring":"创您之心"}],"session_id":"1258491432707977226","angle":1.98828125,"class":[]}}
# # print type(a)  #dict
# # items=a["data"]["items"]
# # print items
# #
# # for item in items:
# #     # print item
# #     i = 1
# #     for word in item['words']:
# #         print word
# #         print i
# #         if word['character']==hanzi:
# #             itemcoord=item['itemcoord']     #{'y': 187, 'x': 101, 'height': 20, 'width': 80}
# #             print"hanzi %s" %item['itemcoord']
# #             x=itemcoord["x"]
# #             y=itemcoord["y"]
# #             height=itemcoord["height"]
# #             width=itemcoord["width"]
# #             y=y+int(height/2)
# #             x=x+int(width*i/4)
# #             print x,y
# while not False:
#      print 1
#      time.sleep(5)
#_
# print 2

from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
img=driver.find_element_by_xpath('//*[@title="看春晚抢百度红包"]')
print img.size()
print img.location()
ActionChains(driver).move_to_element_with_offset(img,"-22","-102").click().perform()

#{'width': 0, 'height': 14}
#{'y': 267.0, 'x': 600.0}
y = 2
x = 1
# print x, y
print  {'x': -x, 'y': -y}

if x!=3:
    print 3
print 1