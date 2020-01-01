#coding:utf-8
import requests

def login():
    login_url = "http://10.152.36.134:8890/sensego/2.0/web/console/ui/api/sensego/console/v1.0/tree/user"
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxNTY3IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMCIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTc2NjU1NDUzfQ.fJb3DYly5NVwVN5e38pL2aXQoVsyLdarJ5Wj9FzDmSg"}
    req = requests.session()
    ret = req.get(url=login_url,headers=headers)
    print(ret.content)
    print(ret.text)
    print("ret cookies:",ret.cookies)
    print("ret headers:",ret.headers)
    for i in ret.headers:
        print(i)
    #接口使用token保持会话请求，token生成在headers中;
    print(ret.status_code)

def get_token():
    url = "http://10.152.36.134:8890/sensego/2.0/web/console/ui/api/sensego/console/v1.0/tree/user"
    headers = {
    'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxNTY3IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMCIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTc2NjU1NDUzfQ.fJb3DYly5NVwVN5e38pL2aXQoVsyLdarJ5Wj9FzDmSg",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "d6325274-0358-4842-8040-8d1d8cf8b912,7946efff-7b89-4e8c-bc5a-1390b3864aa8",
    'Host': "10.152.36.134:8890",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    print(response.headers)


if __name__ == "__main__":
    #login()
    get_token()

{'X-Powered-By': 'Express',
 'connection': 'close',
 'x-frame-options': 'SAMEORIGIN',
 'x-xss-protection': '1; mode=block',
 'content-type': 'text/plain; charset=utf-8',
 'transfer-encoding': 'chunked',
 'server': 'nginx/1.10.3 (Ubuntu)',
 'date': 'Tue, 17 Dec 2019 04:46:56 GMT'}
