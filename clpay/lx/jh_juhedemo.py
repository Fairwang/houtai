#!user/bin/python
# coding:utf-8
import time, json, urllib, hashlib, requests,urllib2
from selenium import webdriver

class PAY():

    def request_pay(self,content):
        gate_way_url = "https://www.juhepay.com/Pay_Index.html"
        datas = {
            'version': '1.0',
            'content': json.dumps(content)
        }
        pay_md5sign_str = self.pay_md5sign(**datas)
        if not pay_md5sign_str:
            return '验签失败'
        datas['pay_md5sign'] = pay_md5sign_str
        # print"datas%s"%(datas)
        #方法一：
        result = requests.post(gate_way_url,data=datas) #requests 模块发起请求时，url 不需要进行编码
        return result.text
        #方法二：
        # datas_encode = urllib.urlencode(datas) # 中文转换url编码 只对dict 有效,将data 中的逗号改为=
        # print datas_encode
        # result=urllib2.Request(url=gate_way_url,data=datas_encode)
        # print "%s"%result
        # result_data=urllib2.urlopen(result)
        # r=result_data.read()
        # print r
        # print result.headers


    # 判断参数param中是否含有pay_md5sign值，有则删除，重新添加
    # 将paramlist重新排序，将排序后的的值取出后，使用= 将key和values连接
    # 将连接好后的list中的[a=1,b=2]连接成字符串a=1&b+2,将商户秘钥连接上去
    # 使用md5将字符串进行

    def pay_md5sign(self,**kw):
        if 'pay_md5sign' in kw:
            del kw['pay_md5sign']
        key = 'trrt15bkvjfceo27ehs1dt1oao71s7wn'  # 商户密钥
        keys = sorted(kw)  # 排序 得出list
        a_list = []
        for i in keys:
            a_list.append("%s=%s" % (i, kw[i]))
        # print '%s' % a_list  #[a=b,c=d]
        pay_md5sign_str2 = '&'.join(a_list) + '&key=' + key
        # print "pay_md5sign Str : "+pay_md5sign_str2 #a=b&c=d&key=XXX
        #

        md5_pay_md5sign = hashlib.md5(pay_md5sign_str2).hexdigest()
        # print "pay_md5sign : "+ md5_pay_md5sign
        return md5_pay_md5sign

datas = {
    'pay_memberid': "10005",
    'pay_orderid': int(time.time()),
    'pay_amount':"100",
    'pay_productname': '支付宝H5测试',
    'notify_url': 'http://pay_project.com:8888/notify',
    'return_url': 'http://pay_project.com:8888/return',
    'pay_applydate':time.time(),
    'pay_ip':"127.0.0.1",

}
s=requests.session()
s.keep_alive=False
pay=PAY()
r2 = pay.request_pay(datas)

print r2
# print type(r2)/
r3=json.loads(r2)#转化 为dict
# driver = webdriver.Chrome()
# driver.get(r3['data']['pay_url'])


# driver.get(url)