#coding:utf-8
import unittest
from os import path
import sys
from before_public import ts,ak_sk,ruuid,sort,sign,TrickUrlSession
import json
import requests
packagepath = path.join(path.dirname(path.dirname(path.dirname(__file__))), "config")
sys.path.append(packagepath)
import readConfig


class Recongnition():

    def __init__(self):
        self.url = readConfig.test_url
        self.host = eval(self.url).split("//")[1]
        self.res = requests.session()  #重写session的url禁止urlcode转义
        self.Trick = TrickUrlSession()
        self.headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Accept-Encoding': "gzip, deflate",
            'Host':self.host,
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

    def recongnition_get_camera(self):
        """业务鉴权接口-获取camera_name和camera_id"""
        # 1请求头参数
        geturl = eval(self.url) + "/senserealty/platform/v1.0/statistics/summary/camerainfo"
        join_str_get, ak, sk, tm, nonce = sort()
        get_sign = sign(join_str_get, sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = get_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数(待参数化)
        querystring = {"store_id": "07e0822ad3", "start_time": "2019-11-24", "end_time": "2019-12-24"}
        getrequest = self.res.get(url=geturl, headers=headers, params=querystring)
        print(getrequest.text)
        print(getrequest.url)
        return getrequest

    def recongnition_get_result(self):
        """业务鉴权接口-识别结果"""
        # 1请求头参数
        geturl = eval(self.url) + "/senserealty/platform/v1.0/trace"
        join_str_get, ak, sk, tm, nonce = sort()
        get_sign = sign(join_str_get, sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = get_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数(待参数化)
        start_time =  "1577203200"
        end_time = "1577258779"
        group_id = "e8b8027ffc"
        device_id = "30:9c:23:a0:1c:75"
        limit = 10
        geturl = "http://172.30.1.176:11111/senserealty/platform/v1.0/trace?start_time=%s&end_time=%s&group_id=%s&device_id=%s&limit=%s"%(start_time,end_time,group_id,device_id,limit)
        print(geturl)
        self.Trick.setUrl(geturl)
        getrequest = self.Trick.get(url=geturl, headers=headers)
        print(getrequest.text)
        print(getrequest.url)
        return getrequest


if __name__ == "__main__":
    test = Recongnition()
    test.recongnition_get_camera()
    test.recongnition_get_result()