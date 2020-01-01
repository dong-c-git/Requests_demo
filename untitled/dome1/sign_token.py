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

'''
1. 用户自己生成timestamp（Unix时间戳），及一个随机nonce。
2. 将timestamp、nonce和ak这三个字符串依据字符串的ASCII码进行升序排列，
并join成一个字符串，然后用sk对该字符做hamc-sha256签名，以16进制编码。
3. 将上述得到的签名结果作为sign的值，与timestamp、nonce、ak一起按照接口的要求传给SenseGo云端接口。

'''
#1 timestamp = time.time()
#  import uuid
#  ret = uuid.uuid4()
#  print(ret)
#  ret1 = str(ret)
#  print(ret1.replace("-",""))
#2  ASCII码进行升序排列
#  用sk对该字符做hamc-sha256签名
#string1 = "thisismytest"

out1 = hashlib.sha256(string1).hexdigest()

print(out1)

#16进制
def str_to_hex(s):
    return r"/x" + r'/x'.join([hex(ord(c)).replace('0x', '') for c in s])


def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(r'/x')[1:]]])


def str_to_bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def bin_to_str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


a = "abcdefg"
x = str_to_hex(a)
print(x)
print(hex_to_str(x))


def str_to_hex(s):
    return ' '.join([hex(ord(c)).replace('0x', '') for c in s])


def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])


def str_to_bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def bin_to_str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


a = "abcdef"
x = str_to_hex(a)
print(x)
print(hex_to_str(x))
