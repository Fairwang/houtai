#!user/bin/python
# coding:utf-8

a=[u'100,195.00', u'\u5143']
# for i in a:
#     i.encode('unicode','ignore')
print type(a)

print a[0]
print type(a[0])

b=[u'', u'0\u7b14', u'/', u'23\u7b14']
print b

print "ss %s %s"%(a,b)