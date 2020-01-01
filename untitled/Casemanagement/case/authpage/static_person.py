#coding:utf-8
import requests
from os import path
import sys
from authpage.before_public import ts,ak_sk,ruuid,sort,sign
import json
packagepath = path.join(path.dirname(path.dirname(path.dirname(__file__))), "config")
sys.path.append(packagepath)
import readConfig
import base64

class StaticPage():

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
            'Host':self.host,
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

    def static_person_get_all(self):
        """静态库人像管理-获取所有person"""
        #1请求头参数
        geturl = eval(self.url) + "/senserealty/platform/v1.0/person/extra/all"
        join_str_get,ak,sk,tm,nonce = sort()
        get_sign =  sign(join_str_get,sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = get_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        #2请求参数(待参数化)
        querystring = {"ak":eval(ak), "group_id":"3d40780e7d", "count":5, "page_index":1}
        getrequest = self.res.get(url = geturl,headers=headers,params=querystring)
        print(getrequest.text)
        print(getrequest.url)
        return getrequest


    def static_person_add(self):
        """静态库人像管理-添加一个person"""
        #1参数组织
        posturl = eval(self.url) + "/senserealty/platform/v1.0/person/extra"
        join_str_get,ak,sk,tm,nonce = sort()
        post_sign =  sign(join_str_get,sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = post_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        filepath = path.join(path.dirname(__file__),"7.jpeg")
        print(filepath)
        with open(filepath,"rb") as fp:
            base_data = base64.b64encode(fp.read())
            print("转换后的base64是",base_data)
        print("图片base64是:",base_data.decode("utf-8"))
        #print("图片base64-2是:", base_data2)
        #2请求参数待参数化
        postdata = {'ak':eval(ak),"group_id":"3d40780e7d","person_id": "",
                    "image":base_data.decode("utf-8"),"image_url":"","id_card":"","name":"testpycharm","age":0,
                    "gender":0,"phone_number":"","birthday":"","status":0,
                    "id_card_type":"","id_card_exp_date":"","other_id_card":"","we_chat":""}
        print(postdata)
        postrequest = self.res.post(url = posturl,headers=headers,data=json.dumps(postdata))
        print(postrequest.text)
        print(postrequest.url)
        return postrequest

    def static_person_update(self):
        """静态库人像管理-更新一个person"""
        #1参数组织
        puturl = eval(self.url) + "/senserealty/platform/v1.0/person/extra"
        join_str_get,ak,sk,tm,nonce = sort()
        get_sign =  sign(join_str_get,sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = get_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        #2请求参数待参数化
        with open("7.jpeg", "rb") as fp:
            base_data = base64.b64encode(fp.read())
            print("转换后的base64是", base_data)
        print("图片base64是:", base_data)
        # print("图片base64-2是:", base_data2)
        # 2请求参数待参数化
        putdata = {'ak': eval(ak), "group_id": "3d40780e7d", "person_id": "aedc80aaae8ea89ba5","face_id":"aedc80aaae8ea89ba5",
                    "image": base_data.decode("utf-8"), "id_card": "", "name": "testupdatename", "age": 0,
                    "gender": 0, "phone_number": "", "birthday": "", "status": 0,
                    "id_card_type": "", "id_card_exp_date": "", "other_id_card": "", "we_chat": ""}
        print(putdata)
        putrequest = self.res.post(url=puturl, headers=headers, data=json.dumps(putdata))
        print(putrequest.text)
        print(putrequest.url)
        return putrequest


    def static_person_delete(self):
        """静态库人像管理-删除一个person"""
        # 1参数组织
        deleteurl = eval(self.url) + "/senserealty/platform/v1.0/person/extra"
        join_str_get, ak, sk, tm, nonce = sort()
        delete_sign = sign(join_str_get, sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = delete_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数待参数化
        with open("7.jpeg", "rb") as fp:
            base_data = base64.b64encode(fp.read())
            print("转换后的base64是", base_data)
        print("图片base64是:", base_data)
        # print("图片base64-2是:", base_data2)
        # 2请求参数待参数化
        deletedata = {'ak': eval(ak), "group_id": "3d40780e7d", "person_id": "aedc80aaae8ea89ba5",
                   "face_id": "aedc80aaae8ea89ba5"}
        print(deletedata)
        deleterequest = self.res.delete(url=deleteurl, headers=headers, data=json.dumps(deletedata))
        print(deleterequest.text)
        print(deleterequest.url)
        return deleterequest


    def static_person_getone(self):
        """静态库人像管理-获取一个person"""
        # 1参数组织
        geturl = eval(self.url) + "/senserealty/platform/v1.0/person/extra"
        join_str_get, ak, sk, tm, nonce = sort()
        get_sign = sign(join_str_get, sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = get_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        # 2请求参数待参数化
        getdata = {'ak': eval(ak), "group_id": "3d40780e7d", "person_id": "aedc80aaae8ea89ba5"}
        print(getdata)
        getrequest = self.res.get(url=geturl, headers=headers, params=getdata)
        print(getrequest.text)
        print(getrequest.url)
        return getrequest


    def static_person_batches(self):
        """静态库人像管理-批量导入person图片"""
        # 1参数组织
        posturl = eval(self.url) + "/senserealty/platform/v1.0/person/extra/batchupload"
        join_str_get, ak, sk, tm, nonce = sort()
        post_sign = sign(join_str_get, sk)
        headers = self.headers
        headers["ak"] = eval(ak)
        headers["sign"] = post_sign
        headers["nonce"] = nonce
        headers["ts"] = tm
        headers["Content-Type"] = "multipart/form-data"
        # 2请求参数待参数化
        postdata = {'ak': eval(ak), "group_id": "3d40780e7d"}
        files = [('file', open('/home/SENSETIME/dongchao_vendor/下载/666/777777777.zip','rb'))]
        print(postdata)
        postrequest = self.res.post(url=posturl, headers=headers, data=json.dumps(postdata))
        print(postrequest.text)
        print(postrequest.url)
        return postrequest


if __name__ == "__main__":
    test =  StaticPage()
    p1 = test.static_person_get_all()
    p2 = test.static_person_add()
    #p3 = test.static_person_update()
    #p4 = test.static_person_getone()
    #p5 = test.static_person_delete()

