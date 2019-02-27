#!user/bin/python
# coding:utf-8
import time, json, urllib, hashlib, requests,urllib2
from selenium import webdriver

class PAY():

    def request_pay(self,api_name, content):
        gate_way_url = "https://dev.herbeauty.top/Pay_Index.html"
        mch_id = "12001"
        datas = {
            'method': api_name,
            'version': '1.0',
            'timestamp': int(time.time()),
            'content': json.dumps(content),
            'mch_id': mch_id
        }
        sign_str = self.sign(**datas)
        if not sign_str:
            return '验签失败'
        datas['sign'] = sign_str
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


    # 判断参数param中是否含有sign值，有则删除，重新添加
    # 将paramlist重新排序，将排序后的的值取出后，使用= 将key和values连接
    # 将连接好后的list中的[a=1,b=2]连接成字符串a=1&b+2,将商户秘钥连接上去
    # 使用md5将字符串进行

    def sign(self,**kw):
        if 'sign' in kw:
            del kw['sign']
        key = '0d8cee92eed880b379fde0b78cbdc173'  # 商户密钥
        keys = sorted(kw)  # 排序 得出list
        a_list = []
        for i in keys:
            a_list.append("%s=%s" % (i, kw[i]))
        # print '%s' % a_list  #[a=b,c=d]
        sign_str2 = '&'.join(a_list) + '&key=' + key
        # print "Sign Str : "+sign_str2 #a=b&c=d&key=XXX
        #

        md5_sign = hashlib.md5(sign_str2).hexdigest()
        # print "Sign : "+ md5_sign
        return md5_sign

api_name = 'shop.payment.aliH5'
datas = {
    'total_fee': 100,
    'goods': '支付宝-H5',
    'order_sn': int(time.time()),
    'client': 'web',
    'notify_url': 'http://pay_project.com:8888/notify',
    'return_url': 'http://pay_project.com:8888/return',

}
pay=PAY()
r2 = pay.request_pay(api_name, datas)
# print type(r2)
r3=json.loads(r2)#转化 为dict

driver = webdriver.Chrome()
driver.get(r3['data']['pay_url'])


# driver.get(url)