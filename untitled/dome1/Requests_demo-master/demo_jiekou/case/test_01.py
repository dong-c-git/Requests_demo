#coding:utf-8
import unittest
import requests
#导入登录模块,保持会话
from demo_jiekou.case.loginleetcode import Leetcode
from demo_jiekou.common.logger import Log

class Test(unittest.Testcase):
    log = Log()
    def setUp(self):
        s = requests.session()
        self.blog = Leetcode(s)


    def test_login(self):
        """
        测试登录用例
        :return:
        """
        self.log.info("-----start1------")
        result = self.blog.login()
        self.log.info("调用登录结果：%s"%result)
        self.log.info("获取是否登录成功：%s"%result["success"])
        self.assertEqual(result["success"],True)   #比较断言结果
        self.log.info("----end----")
        


