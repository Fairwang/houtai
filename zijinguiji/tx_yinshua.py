#!/user/bin/python
#  -*-coding: utf-8-*-
import time
import json
from hashlib import sha1
import hmac
import base64
import requests
def tx_yinshua(hanzi,file_path):
    tx_appid=open("E:\\zxtest\\tx_appid.txt","r")#只有一行
    lines=tx_appid.readlines()
    for line in lines:
        line=line.strip()
        f=line.split(',')
        APPID=f[0]
        SecretId=f[1]
        SecretKey=f[2]
        print APPID,SecretId,SecretKey
    time2=str(int(time.time()+2592000))
    print time2
    bucket=''
    time1=str(int(time.time()))
    rand='123456456'
    fileid=''

    original='a='+APPID+'&b='+bucket+'&k='+SecretId+'&e='+time2+'&t='+time1+'&'+'r='+rand+'&f='+fileid
    my_sign = hmac.new(SecretKey,original, sha1).digest()
    my_sign = base64.b64encode(my_sign+original)
    print my_sign   #WR3ajae/eK0Qj+tiAqYZKg1X9I5hPTEyNTg0OTE0MzImYj0maz1BS0lEZzZ6YzVoYVJXTHZIT0g4UWpwZ0lmbWZOelVsblk4VFomZT0xNTUwMzEwNzAxJnQ9MTU0NzcxODcwMSZyPTEyMzQ1NjQ1NiZmPQ==


    headers={
        'Authorization':my_sign
    }
    url='https://recognition.image.myqcloud.com/ocr/general'
    data={
        "appid":APPID,
        'bucket':'test',
    }

    files={'image':open(file_path,'rb')}

    res=requests.post(url,data=data,files=files,headers=headers)
    results=res.text  # {"code":0,"message":"OK","data":{"recognize_warn_msg":[],"recognize_warn_code":[],"items":[{"itemcoord":{"x":22,"y":36,"width":87,"height":26},"words":[{"character":"么","confidence":0.6924936175346375},{"character":"上","confidence":0.9979987740516664},{"character":"抑","confidence":0.6606981754302979},{"character":"油","confidence":0.9161732792854308}],"itemstring":"么上抑油"},{"itemcoord":{"x":128,"y":118,"width":90,"height":26},"words":[{"character":"以","confidence":0.9816042184829712},{"character":"必","confidence":0.50948566198349},{"character":"当","confidence":0.8555372953414917},{"character":"镜","confidence":0.9988377690315248}],"itemstring":"以必当镜"},{"itemcoord":{"x":101,"y":187,"width":80,"height":20},"words":[{"character":"创","confidence":0.4055652618408203},{"character":"您","confidence":0.722910463809967},{"character":"之","confidence":0.9305914044380188},{"character":"心","confidence":0.8593043088912964}],"itemstring":"创您之心"}],"session_id":"1258491432707977226","angle":1.98828125,"class":[]}}
    print "tx_yinshua_hanzi：%s" %type(hanzi)
    print results
    print type(results) #<type 'unicode'>
    results=results.encode('utf-8')
    result=json.loads(results)
    print type(result) #<type 'dict'>
    items = result["data"]["items"]
    for item in items:
        # print item
        i = 1
        for word in item['words']:
            # print word
            # print i
            if word['character'] == hanzi:  #Unicode可以运行成功 str 不能运行成功
                itemcoord = item['itemcoord']  # {'y': 187, 'x': 101, 'height': 20, 'width': 80}
                print"hanzi %s" % item['itemcoord']
                x = itemcoord["x"]
                y = itemcoord["y"]
                height = itemcoord["height"]
                width = itemcoord["width"]
                y = y + int(height / 2)
                x = x + int((width * i *2-1)/ 8)
                # print x, y
                return {'x':-x,'y':-y}
            i=i+1
#hanzi 为<type 'unicode'>时可以识别    <type 'str'>
# hanzi=u"星"
# print type(hanzi)
# hanzi_location = tx_yinshua(hanzi, './tupian/xiaotu.png')  # {'x':121,'y':197}
# print hanzi_location