#!user/bin/python
# coding:utf-8
import time, json, urllib, hashlib, requests,urllib2
from selenium import webdriver


def request_pay(api_name, content):
    gate_way_url = "https://pay.hongnaga.com/api/gateway"
    mch_id = "12001"
    datas = {
        'method': api_name,
        'version': '1.0',
        'timestamp': int(time.time()),
        'content': json.dumps(content),
        'mch_id': mch_id
    }
    sign_str = sign(**datas)
    if not sign_str:
        return '验签失败'
    datas['sign'] = sign_str
    print"datas%s"%(datas)
    datas_encode = urllib.urlencode(datas) # 中文转换url编码 只对dict 有效
    print datas_encode
    # driver=webdriver.Chrome()
    # driver.get(gate_way_url+datas_encode)
    # url=datas_encode
    result=urllib2.urlopen(gate_way_url+"?"+datas_encode)
    # result = requests.post(gate_way_url,data=datas_encode)
    # result = requests.get(gate_way_url,datas_encode)
    return result.text

# 判断参数param中是否含有sign值，有则删除，重新添加
# 将paramlist重新排序，将排序后的的值取出后，使用= 将key和values连接
# 将连接好后的list中的[a=1,b=2]连接成字符串a=1&b+2,将商户秘钥连接上去
# 使用md5将字符串进行

def sign(**kw):
    if 'sign' in kw:
        del kw['sign']
    key = '0d8cee92eed880b379fde0b78cbdc173'  # 商户密钥
    keys = sorted(kw)  # 排序 得出list
    a_list = []
    for i in keys:
        a_list.append("%s=%s" % (i, kw[i]))
    # print '%s' % a_list
    sign_str2 = '&'.join(a_list) + '&key=' + key
    # print "Sign Str : "+sign_str2
    md5_sign = hashlib.md5(sign_str2).hexdigest()
    # print "Sign : "+ md5_sign
    return md5_sign

api_name = 'shop.payment.aliH5'
datas = {
    'total_fee': 1,
    'goods': '支付宝-H5',
    'order_sn': int(time.time()),
    'client': 'web',
    'notify_url': 'http://www.baidu.com/notify_url',
    'return_url': 'http://www.baidu.com/return_url'
}

r2 = request_pay(api_name, datas)
print(r2)
