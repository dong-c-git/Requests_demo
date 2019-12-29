#coding:utf-8
import requests
import json
'''
python作业16：
使用python发post请求，
登陆接口基本信息POST /api/v1/login Content-Type: application/json  {"username":"test","password":"123456"}
接口服务部署ip地址49.235.92.12， 端口9000
要求：1.根据接口文档和部署地址拼接请求，能登录成功；
2.取出token值，并打印出来
'''
class Login:
    @staticmethod
    def logintoken():
        host = "49.235.92.12"
        port = 9000
        loginurl = "http://"+host+":"+str(port)+"/api/v1/login"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
            "Content-Type":"application/json"
        }
        logindata = {"username":"test","password":"123456"}
        req = requests.post(url = loginurl,headers = headers,data=json.dumps(logindata))
        #print(req.url)    #请求地址
        #print(req.text)   #返回文本数据、
        #print(req.content)#返回bytes数据
        #print(req.json()) #返回字典数据
        print("登录后状态码：",req.status_code)
        print("登录的token信息如下:",req.json().get("token"))  #取出并打印token

if __name__ == "__main__":
    test = Login.logintoken()