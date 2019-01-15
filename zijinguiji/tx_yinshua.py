#!/user/bin/python
#  -*-coding: utf-8-*-
import time
APPID=' '
SecretId=' '
SecretKey=' '
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

files={'image':open('123456.png','rb')}

res=requests.post(url,data=data,files=files,headers=headers)
print res.text