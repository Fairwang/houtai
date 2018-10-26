#!/user/bin/python
#  -*-coding: utf-8-*-
import MySQLdb

coon = MySQLdb.connect(host='cpay.hypayde.com', user='root', passwd='root123456', db='cl_cpay', port=3306,
                       charset='utf8')

cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
sql = "insert into cl_grade_price(mch_id,price,num) ""values(1006,1888,5)"
try:
    cur = cursor.execute(sql)
    rows = cursor.fetchall()
    price = []

except:
    print "Error: This is except"
    # coon.commit()
coon.close()
