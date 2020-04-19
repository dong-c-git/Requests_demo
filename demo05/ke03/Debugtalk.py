#coding:utf-8
import requests

host = "http://49.235.92.12:9000"

#写公共函数
def get_token(user="test",psw="123456"):
    s = requests.session()
    r = s.request(url=host+"/api/v1/login",
                  method="POST",
                  headers={"Content-Type":"application/json","User-Agent":"Fiddler"},
                  json={"password":psw,
                        "username":user},
                  )
    re_token = r.json()["token"]
    print("登录获取到的token:%s"%re_token)
    return re_token

if __name__=="__main__":
    get_token()