#coding:utf-8
import unittest
from os import path
import sys
from requests_before import ts,ak_sk,ruuid,sort,sign,TrickUrlSession
import json
import requests
import base64


class TestPersonCount(unittest.TestCase):

    def setUp(self):
        packagepath = path.join(path.dirname(path.dirname(__file__)), "config")
        sys.path.append(packagepath)
        import readConfig
        self.url = readConfig.test_url
        self.host = eval(self.url).split("//")[1]
        #print(self.host)
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

    def test_01(self):
        """统计功能对外接口-人数统计接口(按照天数)"""
        # 1请求头参数
        posturl = eval(self.url) + "/senserealty/platform/v1.0/statistics/summary/days"
        join_str_get, ak, sk, tm, nonce = sort()
        post_sign = sign(join_str_get, sk)
        print("请求url是:%s,生成的排序加密串:%s,請求參數是%s" % (posturl, join_str_get, (ak, sk, post_sign, nonce, tm)))
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = post_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数(待参数化)
        postdata = {"store_id":"de848b669b", "start_time": "2019-11-24", "end_time": "2019-12-24","camera_id":""}
        postrequest = self.res.post(url=posturl, headers=headers, data=json.dumps(postdata))
        print(postrequest.text)
        print(postrequest.url)
        self.assertTrue(postrequest.status_code == 200, msg="请求返回状态码错误")
        self.assertTrue(postrequest.json().get("error_code") == 0)
        self.assertTrue(postrequest.json().get("error_msg") == "ok")

    def test_02(self):
        """统计功能对外接口-人数统计接口(按小时)"""
        # 1请求头参数
        posturl = eval(self.url) + "/senserealty/platform/v1.0/statistics/summary/hours"
        join_str_get, ak, sk, tm, nonce = sort()
        post_sign = sign(join_str_get, sk)
        #print("请求url是:%s,生成的排序加密串:%s,請求參數是%s" % (posturl, join_str_get, (ak, sk, post_sign, nonce, tm)))
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = post_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数(待参数化)
        postdata = {"store_id": "de848b669b", "start_time": "2019-12-23", "end_time": "2019-12-23", "camera_id": ""}
        postrequest = self.res.post(url=posturl, headers=headers, data=json.dumps(postdata))
        print(postrequest.text)
        print(postrequest.url)
        self.assertTrue(postrequest.status_code == 200, msg="请求返回状态码错误")
        self.assertTrue(postrequest.json().get("error_code") == 0)
        self.assertTrue(postrequest.json().get("error_msg") == "ok")
        self.assertTrue(((postrequest.json().get("info")).get("total_lists")[0]).get("date"))

    def test_03(self):
        """统计功能对外接口-获取camera_name和camera_id"""
        # 1请求头参数
        geturl = eval(self.url) + "/senserealty/platform/v1.0/statistics/summary/camerainfo"
        join_str_get, ak, sk, tm, nonce = sort()
        get_sign = sign(join_str_get, sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = get_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        #2请求参数(待参数化)
        querysting = {"store_id": "de848b669b", "start_time": "2019-11-23", "end_time": "2019-12-23"}
        getrequest = self.res.get(url=geturl, headers=headers,params=querysting)
        print("统计功能对外接口-获取camera_name和camera_id",getrequest.text)
        print("统计功能对外接口-获取camera_name和camera_id",getrequest.url)
        self.assertTrue(getrequest.status_code == 200, msg="请求返回状态码错误")
        self.assertTrue(getrequest.json().get("error_code") == 0)
        self.assertTrue(getrequest.json().get("error_msg") == "ok")

    def test_04(self):
        """统计功能对外接口-员工考勤数据统计"""
        # 1请求头参数
        posturl = eval(self.url) + "/senserealty/platform/v1.0/statistics/summary/staff/attendance"
        join_str_get, ak, sk, tm, nonce = sort()
        post_sign = sign(join_str_get, sk)
        print("请求url是:%s,生成的排序加密串:%s,請求參數是%s" % (posturl, join_str_get, (ak, sk, post_sign, nonce, tm)))
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = post_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数(待参数化)
        postdata = {"store_id": "de848b669b", "company_id": "ID1150","start_date":"","end_date": "2019-12-23"}
        postrequest = self.res.post(url=posturl, headers=headers, data=json.dumps(postdata))
        print("员工考勤数据统计接口:",postrequest.text)
        print(postrequest.url)
        self.assertTrue(postrequest.status_code == 200, msg="请求返回状态码错误")
        self.assertTrue(postrequest.json().get("error_code") == 0)
        self.assertTrue(postrequest.json().get("error_msg") == "ok")


    def test_05(self):
        """统计功能对外接口-频次统计"""
        # 1请求头参数
        posturl = eval(self.url) + "/senserealty/platform/v1.0/statistics/frequencycount"
        join_str_get, ak, sk, tm, nonce = sort()
        post_sign = sign(join_str_get, sk)
        #print("请求url是:%s,生成的排序加密串:%s,請求參數是%s" % (posturl, join_str_get, (ak, sk, post_sign, nonce, tm)))
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = post_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数(待参数化)
        postdata = {"group_id": "de848b669b"}
        postrequest = self.res.post(url=posturl, headers=headers, data=json.dumps(postdata))
        print("员工考勤数据频次统计接口:",postrequest.text)
        print("员工考勤数据频次统计接口:",postrequest.url)
        self.assertTrue(postrequest.status_code == 200, msg="请求返回状态码错误")
        self.assertTrue(postrequest.json().get("error_code") == 0)
        self.assertTrue(postrequest.json().get("error_msg") == "ok")
        self.assertTrue(((postrequest.json().get("frequency"))[0]).get("name") == "once")

    def test_06(self):
        """统计功能对外接口-以图搜图接口"""
        # 1请求头参数
        posturl = eval(self.url) + "/sensego/v2.0/realestate/realestate/trace"
        join_str_get, ak, sk, tm, nonce = sort()
        post_sign = sign(join_str_get, sk)
        #print("请求url是:%s,生成的排序加密串:%s,請求參數是%s" % (posturl, join_str_get, (ak, sk, post_sign, nonce, tm)))
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = post_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        headers["Content-Type"] = "multipart/form-data"
        # 2请求参数(待参数化)
        with open("20170508134213.png", "rb") as fp:
            # b64encode是编码，b64decode是解码
            base64_data = base64.b64encode(fp.read())
            #base64.b64decode(base64_data)
            print(base64_data)
        postdata = {"group_id": "de848b669b","face_image":base64_data,"ak":ak,"sign":post_sign,"nonce":nonce,"ts":tm}
        postrequest = self.res.get(url=posturl, headers=headers, data=json.dumps(postdata))
        print(postrequest.text)
        print(postrequest.url)
        self.assertTrue(postrequest.status_code == 200, msg="请求返回状态码错误")
        self.assertTrue(postrequest.json().get("error_code") == 0)
        self.assertTrue(postrequest.json().get("error_msg") == "ok")

    def tearDown(self):
        print("tearDown")

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestPersonCount('test_03'))
    unittest.TextTestRunner().run(suite)