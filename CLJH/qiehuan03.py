#! user/bin/env
# -*-coding:utf-8-*-
import unittest
import time
from selenium import webdriver
from houtai.CLJH import qiehuan01
from houtai.CLJH import qiehuan02
import threading

class uu(unittest.TestCase):
    def setUp(self):
        self.a1=qiehuan01.qiehuan01()

    def test01(self):
        time.sleep(2)
        # a2=qiehuan02.qiehuan02()
        tasks_number=1
        t = threading.Thread(target=self.a1.test_01)
        t.start()
        time.sleep(2)
        # t2 = threading.Thread(target=a2.test_02)
        # t2.start()



    def tearDown(self):
        pass
if __name__ == "main":
    unittest.main()

