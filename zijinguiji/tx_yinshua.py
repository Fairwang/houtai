#!/user/bin/python
#  -*-coding: utf-8-*-
import time
def tx_yinshua(hanzi):
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

    from hashlib import sha1
    import hmac
    import base64
    import requests
    original='a='+APPID+'&b='+bucket+'&k='+SecretId+'&e='+time2+'&t='+time1+'&'+'r='+rand+'&f='+fileid
    my_sign = hmac.new(SecretKey,original, sha1).digest()
    my_sign = base64.b64encode(my_sign+original)
    print my_sign

    headers={
        'Authorization':my_sign
    }
    url='https://recognition.image.myqcloud.com/ocr/general'
    data={
        "appid":APPID,
        'bucket':'test',
    }

    files={'image':open('./tupian/daichuli.png','rb')}

    res=requests.post(url,data=data,files=files,headers=headers)
    results=res.text
    print type(results) #<type 'unicode'>
    items = results["data"]["items"]
    for item in items:
        # print item
        for word in item['words']:
            print word
            if word['character'] == hanzi:
                itemcoord = item['itemcoord']  # {'y': 187, 'x': 101, 'height': 20, 'width': 80}
                print"hanzi %s" % item['itemcoord']
a=tx_yinshua("心")
print a