#coding:utf-8
import requests
import json
import hashlib

class StoreManager():
    #用户名和密码用户管理后添加
    username = "xxxx"
    password =  hashlib.md5("Goodtest01".encode()).hexdigest()
    loginurl = "http://10.152.36.134:8890/sensego/2.0/web/console/ui/api/sensego/console/v1.0/login"
    session = requests.session()
    headers = {"Content-Type":"application/json",
               "User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}

    def usertoken(self,**kwargs):
        '''
        获取用户token数据，返回用户token、company_id、session会话请求
        '''
        if not kwargs:   #用户名、密码字典形式传入
            postdata = {"user_name":"testSK02","pwd":self.password,"scene":"login"}
            rest = self.session.post(url=self.loginurl,headers=self.headers,data=json.dumps(postdata))
            result = rest.json()
            print(result)#返回字典数据
            '''
            {'type': 'admin', 'company_name': 'SenseRealty测试专用-营销识客', 'ak': 'l1-e01bff22-80a5cc8f9234',
             'node_name': '321', 'productline_name': ['营销识客', '渠道风控'], 'role': 1, 'name': 'testSK02',
             'email': 'test@sensetime.com',
             'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxODY1IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMDAwMyIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTc2ODA1MTIxfQ.53M2SATSUcezawaTQX3ivJqzDwmvJdYzfOSIbF7ZoYc',
             'member': '1', 'request_id': '1576632321.6784', 'user_id': 'ID1865', 'phone': '12345678912',
             'company_id': 'ID1150', 'black': '1', 'productline': [8, 4], 'error_code': 0, 'node_id': '000003'}
             '''
            print(result["token"])
            print(result)
            return result["token"],result["company_id"]

    def getstore(self,token,company_id):
        '''参数company_id和token获取用户案场数据'''
        #1组织参数
        storeurl = "/".join(self.loginurl.split("/")[:-1:])+"/store/all"
        print(storeurl)
        params = {"company_id":company_id}
        if all([token,company_id]):#校验参数后验证帐号案场列表
            store_header = self.headers
            store_header["token"] = token
            print(store_header)
            store_list = self.session.get(storeurl,headers=store_header,params=params)
            print(store_list.json())
            return store_list
        else:
            raise Exception("请求参数不完整")

    def addstore(self,token,addstoredata):
        '''添加案场'''
        addstore_url = "/".join(self.loginurl.split("/")[:-1:])+"/store/all"
        addstore_header = self.headers
        addstore_header["token"] = token
        '''
        store_name: "addtest"
        store_desc: "测试增加案场"
        node_id: "000003"
        callback_url: "test"
        company_id: "ID1150"
        product_line: 8
        sense_id: ""
        opq_model: "3.0.0"
        '''
        addstore_data = {
                "store_name":addstoredata["store_name"],
                "store_desc":addstoredata["store_desc"],
                "node_id":addstoredata["node_id"],
                "callback_url":addstoredata["callback_url"],
                "company_id":addstoredata["company_id"],
                "product_line":addstoredata["product_line"],
                "sense_id":addstoredata["sense_id"],   #一体机编号
                "opq_model":addstoredata["opq_model"]
            }
        print("准备好的data数据：",set(addstore_data),addstore_url)
        addstore_ret = self.session.post(url=addstore_url,headers=addstore_header,data=json.dumps(addstore_data))
        print(addstore_ret.status_code)

    def usertoken(self,**kwargs):
        '''
        获取用户token数据，返回用户token、company_id、session会话请求
        '''
        if not kwargs:   #用户名、密码字典形式传入
            postdata = {"user_name":"testSK02","pwd":self.password,"scene":"login"}
            rest = self.session.post(url=self.loginurl,headers=self.headers,data=json.dumps(postdata))
            result = rest.json()
            print(result)#返回字典数据
            '''
            {'type': 'admin', 'company_name': 'SenseRealty测试专用-营销识客', 'ak': 'l1-e01bff22-80a5cc8f9234',
             'node_name': '321', 'productline_name': ['营销识客', '渠道风控'], 'role': 1, 'name': 'testSK02',
             'email': 'test@sensetime.com',
             'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxODY1IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMDAwMyIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTc2ODA1MTIxfQ.53M2SATSUcezawaTQX3ivJqzDwmvJdYzfOSIbF7ZoYc',
             'member': '1', 'request_id': '1576632321.6784', 'user_id': 'ID1865', 'phone': '12345678912',
             'company_id': 'ID1150', 'black': '1', 'productline': [8, 4], 'error_code': 0, 'node_id': '000003'}
             '''
            print(result["token"])
            print(result)
            return result["token"],result["company_id"]
        "http://10.152.36.134:8890/sensego/2.0/web/console/ui/api/sensego/console/v1.0/store/add"


if  __name__=="__main__":
    test1 = StoreManager()
    token,company_id = test1.usertoken()
    #获取案场
    store_list = test1.getstore(token,company_id)
    print(store_list)
    #增加案场
    add_store = {
        "store_name":"addtest_python",
        "store_desc":"测试增加案场_python",
        "node_id":"000003",
        "callback_url":"test02",
        "company_id":"ID1150",
        "product_line":"8",
        "sense_id":"",
        "opq_model":"3.0.0"
    }
    #add_store_test = test1.addstore(token,add_store)
    import uuid
    ret = uuid.uuid4()
    print(ret)
    ret1 = str(ret)
    print(ret1.replace("-",""))

    




