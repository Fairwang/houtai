#!/user/bin/python
#  -*-coding: utf-8-*-
#使用接口获取汉字
import urllib, urllib2, sys
import ssl


host = 'https://ocrapi-document.taobao.com'
path = '/ocrservice/document'
method = 'POST'
appcode = '你自己的AppCode'
querys = ''
bodys = {}
url = host + path

bodys[''] = "{\"img\":\"\",\"url\":\"\",\"prob\":false}"
post_data = bodys['']
request = urllib2.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib2.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)