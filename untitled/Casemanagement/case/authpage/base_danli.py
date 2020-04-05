#coding:utf-8
import requests
from os import path
import sys
from before_public import ts,ak_sk,ruuid,sort,sign
import json
packagepath = path.join(path.dirname(path.dirname(path.dirname(__file__))), "config")
sys.path.append(packagepath)
import readConfig
from threading import Thread,Lock
from time import sleep


def synchronized(func):
    lock = Lock()
    def synchronized_func(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)
    return synchronized_func


def singleton(cls):
    instance = {}
    @synchronized
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class Base():
    """单例模式"""
    def __init__(self):
        self.url = readConfig.test_url
        self.host = eval(self.url).split("//")[1]
        self.res = requests.session()
        self.headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Accept-Encoding': "gzip, deflate",
            'Host': self.host,
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        print(self.headers)


    def library_configuration_table_get(self):
        """业务鉴权接口-库配置表-查询store的静态库"""
        # 1请求头参数
        geturl = eval(self.url) + "/senserealty/platform/v1.0/confextra"
        join_str_get, ak, sk, tm, nonce = sort()
        get_sign = sign(join_str_get, sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = get_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数(待参数化)
        querystring = {"store_id": "07e0822ad3", "type_id": "-1", "company_id": "ID1150", "group_name": ""}
        getrequest = self.res.get(url=geturl, headers=headers, params=querystring)
        return getrequest


    def library_configuration_table_create(self):
        """业务鉴权接口-库配置表-store创建库"""
        # 1参数组织
        posturl = eval(self.url) + "/senserealty/platform/v1.0/confextra"
        join_str_get, ak, sk, tm, nonce = sort()
        post_sign = sign(join_str_get, sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = post_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数待参数化
        postdata = {'company_id': "ID1150", "store_id": "07e0822ad3", "ak": "l1-3dd91537-h0eb6c347fb6",
                    "group_name": "test12666666", "type_id": 1000, "opq_model": "3.0.0"}
        postrequest = self.res.post(url=posturl, headers=headers, data=json.dumps(postdata))
        print(postrequest.text)
        print(postrequest.url)
        return postrequest




if __name__=="__main__":
    create = Base.library_configuration_table_get("self")