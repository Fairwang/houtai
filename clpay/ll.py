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

print 379-1.44+65-0.23+216-0.82

a=[1,2]
b=[1,2]
if a==b:
    print "a==b"

def ii():
    i=1
    iii=2
    return [i,iii]

print ii()

c=(1,2)
d=(1,2)
if c==d:
    print "c==d"
