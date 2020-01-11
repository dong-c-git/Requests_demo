#coding:utf-8
"""
作业22：
1.写一个登陆的函数，参数账号和密码可以灵活切换
http://49.235.92.12:9000/api/v1/login
body = {"username": "test",  "password": "123456"}
2.登录单独写一个py文件，其它.py文件地方导入登录的模块
"""
from day03_login import login

def getuserinfo():
    s = login(username="test",password="123456")
    userinfo = "http://49.235.92.12:9000/api/v1/userinfo"
    userinfo = s.get(userinfo)
    print(userinfo.text)

if __name__=="__main__":
    getuserinfo()
