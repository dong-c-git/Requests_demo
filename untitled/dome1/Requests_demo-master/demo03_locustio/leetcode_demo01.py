#coding:utf-8
'''
1、leetcode登录请求分析：
https://leetcode-cn.com/accounts/login/
参数：
csrfmiddlewaretoken: vFExzqnGgmfIw34qhSYB9v0Ag0ClQl9VpbHeOdoGKP0Bpt7mGr0phCZ3vMkMfaoA
login: 1277207158@qq.com
password: 111
next: /problemset/all/
有对应csrf_token,先获取csrftoken(一般会在浏览器cookie中)
   1、请求https://leetcode-cn.com/problemset/all/地址时发现向浏览器设置过csrf_tooken；
   先get获取到csrftoken;


'''
import requests

def get_csrf():
    url = "https://leetcode-cn.com/problemset/all/"
    res_headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    s = requests.session()    #session创建的空会话，headers是默认代理，cookies是一个空的对象
    res = s.get(url=url,headers=res_headers)
    print("重新设置请求头后的请求头：",res.headers)
    print("请求后的cookie是：",res.cookies)
    print("取出的csrftoken内容：",res.cookies["csrftoken"])
    print("获取csrftoken：",[i for i in res.cookies][0].value)
    return s,res.cookies["csrftoken"],res.cookies

def login_leetcode():
    url = "https://leetcode-cn.com/accounts/login/"
    session, csrftoken, cookies = get_csrf()
    print(cookies)
    res_headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
                   "x-csrftoken":csrftoken,
                   "cookie":str(cookies),
                   "origin":"https://leetcode-cn.com",
                   "x-requested-with":"XMLHttpRequest",
                   "sec-fetch-site":"same-origin"}
    body = {"csrfmiddlewaretoken":csrftoken,"login":"1277207158@qq.com","password":"dong159753","next":"/problemset/all/"}
    login_res = session.post(url=url,headers=res_headers,data=body,cookies=cookies)
    print("请求后状态码：",login_res.status_code)
    print("请求后报文：",login_res.text)
    print("请求报文：",body)
    print("登录状态的session:",login_res.cookies)
    #返回会话、cookie、登录sessionno相关信息

if __name__ == "__main__":
    login_leetcode()