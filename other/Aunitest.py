#!/user/bin/bin
#-*- coding: utf-8-*-
import unittest
class RTest(unittest.TestCase):
    def setUp(self):
        self.number=raw_input('enter anumber:')
        self.number=int(self.number)

    def test_case1(self):
        print self.number
        self.assertEqual(self.number,10,msg="your input is not 10")

    def test_case2(self):
        print self.number
        self.assertEqual(self.number,20,msg='your input is no 20')

    @unittest.skip(u"暂时跳过")
    def test_case(self):
        self.assertEqual(self.number,30,msg="your imput is not 30")

    def tearDown(self):
        print "test over"

if __name__=='__main__':
    #方法1
    # unittest.main()
    #方法2
    # suite=unittest.TestSuite()
    # suite.addTest(RTest('test_case1'))
    # suite.addTest(RTest('test_case2'))
    # runner=unittest.TextTestRunner()
    # runner.run(suite)
    #方法3
    # test_dir='./'
    # discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
    # runner=unittest.TextTestRunner()
    # runner.run(discover)
