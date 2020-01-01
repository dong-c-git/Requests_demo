#coding:utf-8
import unittest
from os import path
import sys
import json
import requests
import base64
from authpage.static_person import StaticPage
sys.path.append(path.join(path.dirname(path.dirname(__file__)),"common"))
from common.logger import Log

class TestPerson(unittest.TestCase):
    log = Log()

    def setUp(self):
        self.req = StaticPage()

    def tearDown(self):
        pass

    def test_01(self):
        """静态库人像管理--获取所有person"""
        self.log.info("------start------")
        res = self.req.static_person_get_all()
        self.log.info("------调用接口结果是:%s------"%res.json())
        self.assertTrue(res.status_code==200,msg="请求状态码错误")
        self.assertTrue(res.json().get("error_code")==0)
        self.assertTrue(res.json().get("error_msg")=="ok")
        self.log.info("------end!------")

    def test_02(self):
        """静态库人像管理--添加一个person"""
        self.log.info("------start------")
        req = self.req.static_person_add()
        self.log.info("------调用接口结果是:%s------" % req.json())
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")
        self.log.info("------end!------")

    def test_03(self):
        """静态库人像管理--更新一个person"""
        self.log.info("------start------")
        res = self.req.static_person_update()
        self.log.info("------调用接口结果是:%s------" % res.json())
        self.assertTrue(res.status_code==200,msg="请求状态码错误")
        self.assertTrue(res.json().get("error_code")==0)
        self.assertTrue(res.json().get("error_msg")=="ok")
        self.log.info("------start------")

    def test_04(self):
        """静态库人像管理--删除一个person"""
        self.log.info("------start------")
        req = self.req.static_person_delete()
        self.log.info("------调用接口结果是:%s------" % req.json())
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")
        self.log.info("------start------")

    def test_05(self):
        """静态库人像管理--获取一个person"""
        self.log.info("------start!------")
        req = self.req.static_person_getone()
        self.log.info("------调用接口结果是:%s------" % req.json())
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")
        self.log.info("------end!------")

    def test_06(self):
        """静态库人像管理--批量导入person"""
        self.log.info("------start------")
        req = self.req.static_person_getone()
        self.log.info("------调用接口结果是:%s------" % req.json())
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")
        self.log.info("------end!------")


if __name__=="__main__":
    unittest.main()


