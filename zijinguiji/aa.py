#!/user/bin/python
#  -*-coding: utf-8-*-

from selenium import webdriver
import time
import json
hanzi="心"
a={"code":0,"message":"OK","data":{"recognize_warn_msg":[],"recognize_warn_code":[],"items":[{"itemcoord":{"x":22,"y":36,"width":87,"height":26},"words":[{"character":"么","confidence":0.6924936175346375},{"character":"上","confidence":0.9979987740516664},{"character":"抑","confidence":0.6606981754302979},{"character":"油","confidence":0.9161732792854308}],"itemstring":"么上抑油"},{"itemcoord":{"x":128,"y":118,"width":90,"height":26},"words":[{"character":"以","confidence":0.9816042184829712},{"character":"必","confidence":0.50948566198349},{"character":"当","confidence":0.8555372953414917},{"character":"镜","confidence":0.9988377690315248}],"itemstring":"以必当镜"},{"itemcoord":{"x":101,"y":187,"width":80,"height":20},"words":[{"character":"创","confidence":0.4055652618408203},{"character":"您","confidence":0.722910463809967},{"character":"之","confidence":0.9305914044380188},{"character":"心","confidence":0.8593043088912964}],"itemstring":"创您之心"}],"session_id":"1258491432707977226","angle":1.98828125,"class":[]}}
print type(a)  #dict
items=a["data"]["items"]
print items
for item in items:
    # print item
    for word in item['words']:
        print word
        if word['character']==hanzi:
            itemcoord=item['itemcoord']     #{'y': 187, 'x': 101, 'height': 20, 'width': 80}
            print"hanzi %s" %item['itemcoord']
