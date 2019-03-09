#! user/bin/env
# -*-coding:utf-8-*-
import unittest

import os,glob



testcase_path = ".\\testcase"

# report_path = ".\\report\\appium_report.html"





def creat_suite():

    suite = unittest.TestSuite()

    discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test_*.py")

    for test_suite in discover:

        # print(test_suite)

        for test_case in test_suite:

            suite.addTest(test_case)

    return suite



suite = creat_suite()
runner=unittest.TextTestRunner()
runner.run(suite)

# fp = open(report_path,"w+")
#
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试结果",description=u"简店test")
#
# runner.run(suite)
#
# fp.close()
#
#
#
#
#
#
#
# email=send_email.Send_mail()
#
#
#
# email.send_mail('E:\\Users\msi1\\PycharmProjects\\untitled\\jiandian\\report\\appium_report.html')
