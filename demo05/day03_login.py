#coding:utf-8
'''作业21：
session自动关联token，登录成功后把token更新到头部，后面所有请求自动带上token
http://49.235.92.12:9000/api/v1/login
body = {"username": "test",  "password": "123456"}
　
获取个人信息
http://49.235.92.12:9000/api/v1/userinfo
'''
import requests

def loginapi():
    url = "http://49.235.92.12:9000"
    body = {"username": "test",  "password": "123456"}
    s = requests.session()
    r = s.post(url=url+"/api/v1/login",json=body)
    token = r.json()["token"]
    print("token是:{}".format(token))
    h = {"Authorization": "Token {}".format(token)}
    #更新前的token是：
    print("没有更新前的token:{}".format(s.headers))
    s.headers.update(h)
    print("更新后的token是:{}".format(s.headers))
    userinfo = s.get(url=url+"/api/v1/userinfo")
    print(userinfo.text)

def login(**kwargs):
    url = "http://49.235.92.12:9000"
    username = kwargs["username"] if "username" in kwargs else "test"
    password = kwargs["password"] if "password" in kwargs else "123456"
    body = {"username":username,"password":password}
    s = requests.session()
    r = s.post(url=url+"/api/v1/login",json=body)
    token = r.json()["token"]
    print("token是:{}".format(token))
    h = {"Authorization": "Token {}".format(token)}
    s.headers.update(h)
    return s

if __name__=="__main__":
    loginapi()