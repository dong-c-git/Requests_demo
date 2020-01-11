#coding:utf-8
"""
作业23：
1.把登录写到fixture
2.pytest写的其它测试用例，修改个人信息，调用登录的fixture
url = "http://49.235.92.12:9000/api/v1/userinfo"
body = {"name": "test","sex": "M","age": 20,"mail": "283340479@qq.com" }
"""
import pytest
import requests

@pytest.fixture()
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

def test_01(login):
    """登录用户修改个人信息"""
    s = login
    url = "http://49.235.92.12:9000/api/v1/userinfo"
    body = {"name": "test","sex": "M","age": 20,"mail": "283340479@qq.com" }
    req = s.post(url=url,json=body)
    #print(req.url)
    print(req.text)
    #assert "KEY ERROR!"==req.json().get("reason")
    #assert 10002 == req.json().get("error_code")
    assert req.json()["message"] == "update some data!"
    assert req.json()["code"] == 0
    assert req.json()["data"]["mail"] == "283340479@qq.com"

