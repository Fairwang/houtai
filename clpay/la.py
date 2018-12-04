#!user/bin/python
# coding:utf-8
from selenium import webdriver
import re
import time
import requests
sc=[]
# faileurl1=['http://www.cnblogs.com/zhuwoyao88/p/8449053.html']
faileurl1=[ 'https://wenku.baidu.com/view/92c33d7b0029bd64783e2cef.html\n', 'http://www.open-open.com/lib/view/open1437483697115.html\n', 'http://www.onlinedown.net/soft/989451.htm\n', 'https://www.jianshu.com/p/bfa86847f81e\n', 'http://www.cnblogs.com/wanqieddy/archive/2011/12/15/2288598.html\n', 'http://www.cnblogs.com/sushi/p/7682996.html\n', 'https://www.cnblogs.com/minieye/p/5806911.html\n', 'https://www.cnblogs.com/notepad/articles/4711528.html\n', 'http://www.cnblogs.com/chongyou/p/5374406.html\n', 'https://www.cnblogs.com/xuxuzhaozhao/p/6740046.html\n', 'https://www.cnblogs.com/brad1994/p/6540461.html\n', 'https://www.cnblogs.com/Mushishi_xu/p/7685903.html\n', 'https://testerhome.com/topics/10552\n', 'http://www.php.cn/python-tutorials-358252.html\n', 'http://www.cnblogs.com/zz-yy/p/8432815.html\n', 'http://www.cnblogs.com/yoyoketang/p/6128741.html\n', 'https://www.cnblogs.com/BlueSkyyj/p/8392628.html\n', 'http://blog.csdn.net/kaka1121http://www.51testing.com/html/15/n-3717415.html\n', 'https://www.cnblogs.com/Mushishi_xu/category/1098394.html\n', 'https://nodejs.org/dist/v6.9.4\n', 'https://www.cnblogs.com/teamemory/p/8473727.html\n', 'https://m.jb51.net/softjc/595372.html\n', 'https://www.cnblogs.com/general-seven/p/6144972.html\n', 'http://www.51testing.com/html/47/n-3719147.html?from=groupmessage\n', 'https://www.cnblogs.com/aestheticism/p/5064998.html\n']
# faileurl1=[  'https://blog.csdn.net/column/details/12694.html\n', 'http://www.cnblogs.com/cnhkzyy/p/9252884.html\n', 'http://www.cnblogs.com/fengsiyi/p/7206537.html\n', 'http://www.360doc.com/content/11/0124/14/5480484_88697703.shtml\n', 'http://www.360doc.com/content/18/0913/13/3175779_786335678.shtml\n', 'http://0cx.cc/python_captcha_breaker.jspx\n', 'https://www.aliyun.com/jiaocheng/452316.html\n', 'https://www.sogou.com/tx?query=%E9%AA%8C%E8%AF%81%E7%A0%81+Python+%E5%80%BE%E6%96%9C%E5%BA%A6&ie=utf8&_ast=1538990336&_asf=null&w=01029901&hdq=sogou-clse-f507783927f2ec27&duppid=1&cid=&s_from=result_up&sut=1602&sst0=1538990168221&lkt=0%2C0%2C0&sugsuv=00662FD673C658C45BBAAFD6DE318500&sugtime=1538990168221\n', 'https://mp.weixin.qq.com/s/XW9geHZ9odHdI7srDiKBIg\n', 'https://www.yiibai.com/git/git-quick-start.html\n', 'https://testerhome.com/topics/12709\n', 'https://www.cnblogs.com/simple-free/p/8447358.html\n', 'https://www.aliyun.com/jiaocheng/450854.html\n', 'https://wenku.baidu.com/view/e4a23d0703d8ce2f00662335.html\n', 'https://www.cnblogs.com/NancyRM/p/8243821.html\n', 'https://www.pythontab.com/html/2017/pythonhexinbiancheng_1120/1184.html\n', 'https://www.pythontab.com/html/2017/pythonhexinbiancheng_1120/1184.html\n', 'https://www.cnblogs.com/chenlogin/p/6592228.html\n', 'https://pypi.org/project/opencv-python/#files\n', 'http://www.cnblogs.com/chensheng-zhou/p/4895332.html\n', 'https://www.linuxidc.com/Linux/2018-09/154317.htm\n', 'https://www.cnblogs.com/wuzhiming/category/665000.html\n', 'https://blog.csdn.net/reboot123\n', 'http://www.cnblogs.com/only-love-you-519920/p/Alice.html\n', 'http://www.cnblogs.com/fengpingfan\n', 'http://www.cnblogs.com/yangxia-test/p/4137519.htmlJmeter\n', 'http://www.cnblogs.com/linxinmeng/p/7207156.html\n', 'https://www.yiibai.com/jmeter/jmeter_web_test_plan.html\n', 'http://www.cnblogs.com/cnhkzyy/p/9252884.html\n', 'http://www.cnblogs.com/fengsiyi/p/7206537.html\n', 'http://www.360doc.com/content/11/0124/14/5480484_88697703.shtml\n', 'http://www.cnblogs.com/meitian/p/6103391.html\n', 'http://www.testclass.net/appium/appium-base-summary/\n', 'https://baike.sogou.com/v171812.htm?fromTitle=.bat\n']
i=0
for url in faileurl1:
    url1=url.strip()
    r=requests.post(url1,)
    r2=r.text
    r3=r2.split("title>",2)
    # print r3
    r4=r3[1]
    # print r4
    r5=r4[:-3]
    i+=1
    sc1 = '<DT><A HREF=' + '"' + url1+ '"' + ">" + r4+ "</A>"
    sc.append(sc1)
    if i == 10:
        print sc
