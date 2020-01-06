import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

s = requests.session()
url1 = "http://www.baidu.com"
headers = {"accept-encoding":"gzip, deflate, br",
           "Content-Type":"multipart/form-data; boundary='--------------test'"}
d= {
    "groupid": "test1",
    "ak": "test"
    }
file = {
   "files": ("1.png", open("one_login.py", "rb"), "image/png")
    }
r = s.post(url1, data=d, files=file,headers=headers)  # 分开传
#print(r.text)
print(r.request.body)
print(r.request.headers)
#m = MultipartEncoder()
m = MultipartEncoder(fields={'act': 'avatar',
                             'save': '1',
                             'image': ('filename',open('one_login.py', 'rb'), 'image/png')},
                     boundary='---------------------------7de1ae242c06ca'
                    )
req_headers = {'Content-Type': m.content_type}
print(m)
print(m.content_type)
# r = session.post(back_url_avatar, data=m, headers=req_headers)
# print r.status_code
# print r.content