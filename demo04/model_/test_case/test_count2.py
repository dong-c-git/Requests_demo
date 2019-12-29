#coding:utf-8
import sys
sys.path.append('pub')
from pub import count
import unittest
import time

class TestCount2(unittest.TestCase):

    def setUp(self):
        print("test case start!")
        time.sleep(1)

    def tearDown(self):
        print("test case end!")
        time.sleep(1)

    def test_add(self):
        j = count.Count(2,4)
        add = j.add()
        self.assertEqual(add,6)

    def test_add1(self):
        j = count.Count(2.5,4.4)
        add = j.add()
        self.assertEqual(add,6.9)

    def test_in(self):
        a = "hello world!"
        b = "hello"
        self.assertIn(b,a)

if __name__=='__main__':
    #unittest.main()
    #构建测试集
    suite = unittest.TestSuite()   #创建测试套件
    suite.addTest(TestCount2("test_add")) #把测试用例加到测试套件中
    suite.addTest(TestCount2("test_add1"))
    suite.addTest(TestCount2("test_in"))

    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)