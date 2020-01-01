#coding:utf-8
import requests
import unittest
from os import path
import sys
from requests_before import ts,ak_sk,ruuid,sort,sign
import json

class TestDbConfig(unittest.TestCase):

    def setUp(self):
        packagepath = path.join(path.dirname(path.dirname(__file__)), "config")
        sys.path.append(packagepath)
        import readConfig
        self.url = readConfig.test_url
        self.host = eval(self.url).split("//")[1]
        #print(self.host)
        self.res = requests.session()
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

    def test_01(self):
        """业务鉴权接口-库配置表-查询store的静态库"""
        #1请求头参数
        geturl = eval(self.url) + "/senserealty/platform/v1.0/confextra"
        join_str_get,ak,sk,tm,nonce = sort()
        get_sign =  sign(join_str_get,sk)
        print("请求url是:%s,生成的排序加密串:%s,請求參數是%s"%(geturl,join_str_get,(ak,sk,get_sign,nonce,tm)))
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = get_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        #2请求参数(待参数化)
        querystring = {"store_id": "07e0822ad3", "type_id": "-1", "company_id": "ID1150", "group_name": ""}
        getrequest = self.res.get(url = geturl,headers=headers,params=querystring)
        print(getrequest.text)
        print(getrequest.url)
        self.assertEqual(getrequest.status_code,200,msg="请求返回状态码错误")

    def test_02(self):
        """业务鉴权接口-库配置表-store创建库"""
        #1参数组织
        posturl = eval(self.url) + "/senserealty/platform/v1.0/confextra"
        join_str_get,ak,sk,tm,nonce = sort()
        post_sign =  sign(join_str_get,sk)
        print("请求url是:%s,生成的排序加密串:%s,請求參數是%s"%(posturl,join_str_get,(ak,sk,post_sign,nonce,tm)))
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = post_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        #2请求参数待参数化
        postdata = {'company_id':"ID1150","store_id":"07e0822ad3","ak": "l1-3dd91537-h0eb6c347fb6","group_name":"test12666666","type_id":1000,"opq_model":"3.0.0"}
        postrequest = self.res.post(url = posturl,headers=headers,data=json.dumps(postdata))
        print(postrequest.text)
        print(postrequest.url)
        self.assertEqual(postrequest.status_code,200,msg="请求返回状态码错误")

    def test_03(self):
        """业务鉴权接口-库配置表-更新人员库"""
        #1参数组织
        puturl = eval(self.url) + "/senserealty/platform/v1.0/confextra"
        join_str_get,ak,sk,tm,nonce = sort()
        get_sign =  sign(join_str_get,sk)
        print("请求url是:%s,生成的排序加密串:%s,請求參數是%s"%(puturl,join_str_get,(ak,sk,get_sign,nonce,tm)))
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = get_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        #2请求参数待参数化
        postdata = {'company_id':"ID1150","store_id":"07e0822ad3","ak": "l1-3dd91537-h0eb6c347fb6","group_name":"test7777666665","type_id":1000,"opq_model":"3.0.0"}
        postrequest = self.res.post(url = puturl,headers=headers,data=json.dumps(postdata))
        group_id = postrequest.json()["group_id"]
        putdata = {'company_id': "ID1150", "group_id":group_id, "group_name":"test12777777777","type_id": 1000, "opq_model": "3.0.0"}
        putrequest = self.res.put(url=puturl,headers=headers,data=json.dumps(putdata))
        print(putrequest.text)
        print(putrequest.url)
        self.assertEqual(putrequest.status_code,200,msg="请求返回状态码错误")

    def test_04(self):
        """业务鉴权接口-库配置表-delete"""
        # 1参数组织
        puturl = eval(self.url) + "/senserealty/platform/v1.0/confextra"
        join_str_get, ak, sk, tm, nonce = sort()
        delete_sign = sign(join_str_get, sk)
        #print("请求url是:%s,生成的排序加密串:%s,請求參數是%s" % (puturl, join_str_get, (ak, sk, delete_sign, nonce, tm)))
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = delete_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数待参数化
        postdata = {'company_id': "ID1150", "store_id": "07e0822ad3", "ak": "l1-3dd91537-h0eb6c347fb6",
                    "group_name": "abcdefghjilks123456", "type_id": 1000, "opq_model": "3.0.0"}
        postrequest = self.res.post(url=puturl, headers=headers, data=json.dumps(postdata))
        print(postrequest.json())
        group_id = postrequest.json()["group_id"]
        putdata = {'company_id': "ID1150","store_id":"07e0822ad3","group_id": group_id}
        deleterequest = self.res.put(url=puturl, headers=headers, data=json.dumps(putdata))
        print(deleterequest.text)
        print(deleterequest.url)
        self.assertEqual(deleterequest.status_code, 200, msg="请求返回状态码错误")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestDbConfig('test_04'))
    print(suite)
    unittest.TextTestRunner().run(suite)
    #unittest.main()

