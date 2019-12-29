#coding:utf-8
import unittest
import sys
import time
#加载测试文件
sys.path.append("test_case")
from test_case import test_count
from test_case import test_count2
from test_case.pub import HTMLTestRunner
import os

# #构造测试用例
# suite = unittest.TestSuite()
# suite.addTest(test_count.TestCount("test_add"))
# suite.addTest(test_count.TestCount("test_add1"))
# suite.addTest(test_count.TestCount("test_in"))
# suite.addTest(test_count2.TestCount2("test_add"))
# suite.addTest(test_count2.TestCount2("test_add1"))
# suite.addTest(test_count2.TestCount2("test_in"))

def creatsuite():
    testunit = unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir = os.path.dirname(__file__)
    print(test_dir)
    #定义discover方法参数
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern="test_count*.py",
                                                   top_level_dir=None
                                                   )
    print(discover)
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

#discover是已经匹配了测试用例的测试套件了，可以直接使用
def discover_test02():
    test_dir = os.path.dirname(__file__)
    print(test_dir)
    #定义discover方法参数
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern="test_count*.py",
                                                   top_level_dir=None
                                                   )
    return discover


if __name__=="__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #print(os.path.abspath(__file__))#得到的是文件绝对路径
    #print(os.path.dirname(__file__)) #得到的是文件真实路径
    #discover函数实现方式：
    # runner = unittest.TextTestRunner()
    # runner.run(creatsuite())
    #discover直接使用方式
    # runner = unittest.TextTestRunner()
    # runner.run(discover_test02())

    #生成测试报告
    #测试报告路径
    now = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
    filepath = os.path.join(os.path.dirname(__file__),"report",now+"result.html")
    print(filepath)
    fp = open(filepath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"自动化测试报告，测试结果如下",
                                           description=u"用例执行情况:")
    runner.run(discover_test02())
    fp.close()