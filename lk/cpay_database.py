#!/user/bin/python
#  -*-coding: utf-8-*-
import MySQLdb
# class qrocde_url():
def query_database(sql):
    #
    # coon = MySQLdb.connect(host='cpaytest.tinywan.com', user='root', passwd='123456', db='cpay', port=3306,
    #                        charset='utf8')
    # cursor = coon.cursor()
    # coon = MySQLdb.connect(host='103.93.252.181', user='root', passwd='6WUmY1Py', db='cl_cpay', port=3306,
    #                        charset='utf8')
    coon = MySQLdb.connect(host='103.93.252.181', user='www', passwd='www123456', db='cl_cpay', port=3306,
                           charset='utf8')

    cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
    try:
        cur = cursor.execute(sql)
        rows = cursor.fetchall()
        qrcode_url = []
        print rows
        for row in rows:
            print row["qrcode_url"]
            qrcode_url.append(row["qrcode_url"])
        print rows
        return qrcode_url
    except:
        print "Error: This is except"
        # coon.commit()
    coon.close()