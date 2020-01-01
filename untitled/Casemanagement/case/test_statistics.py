#coding:utf-8
import unittest
from os import path
import sys
import json
import requests
import base64
from authpage.statistics import StatisticsFunction

class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.req = StatisticsFunction()

    def tearDown(self):
        pass

    def test_01(self):
        """统计功能--人数统计接口(按天数)"""
        res = self.req.statistics_person_days()
        self.assertTrue(res.status_code==200,msg="请求状态码错误")
        self.assertTrue(res.json().get("error_code")==0)
        self.assertTrue(res.json().get("error_msg")=="ok")

    def test_02(self):
        """统计功能--人数统计接口(按小时)"""
        req = self.req.statistics_person_hours()
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")

    def test_03(self):
        """统计功能--获取camera_name"""
        res = self.req.statistics_person_cameraname()
        self.assertTrue(res.status_code==200,msg="请求状态码错误")
        self.assertTrue(res.json().get("error_code")==0)
        self.assertTrue(res.json().get("error_msg")=="ok")

    def test_04(self):
        """统计功能--员工考勤数据统计"""
        req = self.req.statistics_person_attendance()
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")

    def test_05(self):
        """统计功能--频次统计"""
        req = self.req.statistics_person_frequencycount()
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")

    def test_06(self):
        """统计功能--以图搜图接口"""
        req = self.req.statistics_person_trace()
        self.assertTrue(req.status_code == 200, msg="请求状态码错误")
        self.assertTrue(req.json().get("error_code") == 0)
        self.assertTrue(req.json().get("error_msg") == "ok")


if __name__=="__main__":
    unittest.main()


