#coding:utf-8
'''
作业20：
用session会话保持方法，登录http://49.235.92.12:9000/admin/login/
账号 admin密码yoyo123456
并判断是否登录成功
'''
import requests
import json
import re
def login():
    s = requests.session()
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    get_url = "http://49.235.92.12:9000/admin/login/"
    get_csrf = s.get(url=get_url,headers=headers)
    #获取csrf 和 匹配请求参数的csrfmiddlewaretoken
    csrfmiddlewaretoken = re.findall("name=\'csrfmiddlewaretoken\' value=\'(.*?)\'",get_csrf.text)
    #更新会话headers
    headers["Cookie"] = "csrftoken={}".format(get_csrf.cookies["csrftoken"])
    s.headers.update(headers)
    #post登录参数传递：
    data = {"csrfmiddlewaretoken":csrfmiddlewaretoken[0],
            "username":"admin",
            "password":"yoyo123456",
            "next":"/admin/"}
    session_id = s.post(url=get_url,data=data)
    #通过session获取admin首页
    admin_url = "http://49.235.92.12:9000/admin/"
    admin = s.get(admin_url)
    if admin.status_code == 200:
        print("请求状态码正常")
    else:
        print("请求状态码异常,请修正请求,请求的状态码是:{}".format(admin.status_code))
        return
    if "Site Administration | Django Site Admin" in admin.text.title():
        print("登录成功，获取admin首页title是:{}".format(admin.text.title()))
    else:
        print("获取首页title失败，登录失败，请修正！返回请求报文:{}".format(admin.text))
        return

if __name__=="__main__":
    login()