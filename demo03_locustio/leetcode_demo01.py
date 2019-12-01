#coding:utf-8
'''
1、登录请求分析：
https://leetcode-cn.com/accounts/login/
参数：
csrfmiddlewaretoken: vFExzqnGgmfIw34qhSYB9v0Ag0ClQl9VpbHeOdoGKP0Bpt7mGr0phCZ3vMkMfaoA
csrftoken=           vFExzqnGgmfIw34qhSYB9v0Ag0ClQl9VpbHeOdoGKP0Bpt7mGr0phCZ3vMkMfaoA
login: 1277207158@qq.com
password: 111
next: /problemset/all/
有对应的csrf_token，尝试使用request

'''
import requests

def main():
    url = "https://leetcode-cn.com/accounts/login/"
    body = {
        "csrfmiddlewaretoken":"vFExzqnGgmfIw34qhSYB9v0Ag0ClQl9VpbHeOdoGKP0Bpt7mGr0phCZ3vMkMfaoA",
        "login":"1277207158@qq.com",
        "password":"dongchao123",
        "next":"/problemset/all/",
    }
    headers = {
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "x-csrftoken": "vFExzqnGgmfIw34qhSYB9v0Ag0ClQl9VpbHeOdoGKP0Bpt7mGr0phCZ3vMkMfaoA",
        "cookie": "csrftoken=vFExzqnGgmfIw34qhSYB9v0Ag0ClQl9VpbHeOdoGKP0Bpt7mGr0phCZ3vMkMfaoA; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1574156406,1575193676; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1575193676; _ga=GA1.2.1968277811.1575193676; _gid=GA1.2.1936914546.1575193676; gr_user_id=b2cd0869-c09c-4cd0-96fd-2f30e2ef7d49; a2873925c34ecbd2_gr_session_id=ac667a1c-4e49-437f-adc3-553193f1270e; grwng_uid=208b9cda-4bee-470b-a370-b2fea7b36207; a2873925c34ecbd2_gr_session_id_ac667a1c-4e49-437f-adc3-553193f1270e=true"
    }
    #res = requests.session()
    #print(res.headers,res.cookies)
    response = requests.post(url=url,data=body,headers=headers)
    print("响应文本：",response.text)
    print("响应主体：",response.content)
    print("响应状态码：",response.status_code)
    print("请求头：",response.headers)


if __name__ == "__main__":
    main()