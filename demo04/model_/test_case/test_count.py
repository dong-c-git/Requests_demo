#coding:utf-8
import sys
sys.path.append('test_case')
from test_case.pub import count
import unittest
import time
import os
from test_case.pub import HTMLTestRunner

class TestCount(unittest.TestCase):

    def setUp(self):
        print("test case start!")
        time.sleep(1)

    def tearDown(self):
        print("test case end!")
        time.sleep(1)

    def test_add(self):
        '''测试加法运算，整数：2,整数：4'''
        j = count.Count(2,4)
        add = j.add()
        self.assertEqual(add,6)

    def test_add1(self):
        '''测试浮点数运算，浮点数：2.5,浮点数:4.4'''
        j = count.Count(2.5,4.4)
        add = j.add()
        self.assertEqual(add,6.9)

    def test_in(self):
        '''简单字符比较测试'''
        a = "hello world!"
        b = "hello"
        self.assertIn(b,a)

if __name__=='__main__':
    #unittest.main()
    #构建测试集
    suite = unittest.TestSuite()   #创建测试套件
    suite.addTest(TestCount("test_add")) #把测试用例加到测试套件中
    # suite.addTest(TestCount("test_add1"))
    # suite.addTest(TestCount("test_in"))
    #定义测试报告存放路径
    # if os.path.exists(os.path.join(os.path.dirname(__file__),"result.html")):
    #     os.mkdir(os.path.join(os.path.dirname(__file__),"result.html"))
    filepath = os.path.join(os.path.dirname(__file__),"result.html")
    print(filepath)
    fp = open(filepath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"测试百度搜索报告",
                                           description=u"用例执行情况:")
    runner.run(suite)
    fp.close()
    # fp = file(filepath,"wb")
    # with open("result.html","wb") as fp:
    #     runner = HTMLTestRunner.HTMLTestRunner(
    #         stream=fp,
    #         title=u'百度搜索测试报告',
    #         description=u"用例执行情况:"
    #     )
    #     #执行测试
    #     #runner = unittest.TextTestRunner()
    #     runner.run(suite)