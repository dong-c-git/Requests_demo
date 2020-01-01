#coding:utf-8
import unittest
from os import path
import sys
import json
import requests
import base64
from authpage.library_configuration_table import LibraryPage

class TestConfiguration(unittest.TestCase):

    def setUp(self):
        self.req = LibraryPage()

    def tearDown(self):
        pass

    def test_01(self):
        """库配置表--查询store的静态库"""
        res = self.req.library_configuration_table_get()
        self.assertTrue(res.status_code==200,msg="请求状态码错误")
        self.assertTrue(res.json().get("error_code")==0)
        self.assertTrue(res.json().get("error_msg")=="ok")

    def test_02(self):
        """库配置表--创建静态库"""
        req = self.req.library_configuration_table_create()
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")

    def test_03(self):
        """库配置表--更新人员库"""
        res = self.req.library_configuration_table_update()
        self.assertTrue(res.status_code==200,msg="请求状态码错误")
        self.assertTrue(res.json().get("error_code")==0)
        self.assertTrue(res.json().get("error_msg")=="ok")

    def test_04(self):
        """库配置表--删除静态库"""
        req = self.req.library_configuration_table_delete()
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")


if __name__=="__main__":
    unittest.main()


