#coding:utf-8
import unittest
from os import path
import sys
import json
import requests
import base64
from authpage.recongnition_result import Recongnition

class TestRecongnition(unittest.TestCase):

    def setUp(self):
        self.req = Recongnition()

    def tearDown(self):
        pass

    def test_01(self):
        """业务鉴权--获取camera_name和camera_id"""
        res = self.req.recongnition_get_camera()
        self.assertTrue(res.status_code==200,msg="请求状态码错误")
        self.assertTrue(res.json().get("error_code")==0)
        self.assertTrue(res.json().get("error_msg")=="ok")

    def test_02(self):
        """业务鉴权接口--识别结果"""
        req = self.req.recongnition_get_result()
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")


if __name__=="__main__":
    unittest.main()


