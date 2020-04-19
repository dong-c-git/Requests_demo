import requests
import hashlib
import time

token = 'token-device-1:b233efca98514065bb06633775013178'
nowtime = lambda: int(round(time.time() * 1000))
timestamp = str(nowtime())
print(timestamp)

def get_sign():
    SECRET = 'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8'
    md5 = "AUTH-TIMESTAMP=" + timestamp + "&AUTH-TOKEN=" + token + "#" + SECRET
    m1 = hashlib.md5()
    m1.update(md5.encode("utf-8"))
    sign = m1.hexdigest()
    return sign


url = 'http://link-test.bi.sensetime.com'
headers = {
    "Content-Type": "application/json;charset=UTF-8",
    'AUTH-TOKEN': token,
    'AUTH-TIMESTAMP': timestamp,
    'AUTH-SIGN': get_sign(),
    'LDID': 'SPS-cc8d61e43319262798afb06affea4f68'
}
#response = requests.get(url + "/sl/v2/device", headers=headers)
#print(response.text)


#导出识别记录
token = 'token-web-1:7c71707bda154665b42954858847f60a'
nowtime = lambda: int(round(time.time() * 1000))
timestamp = str(nowtime())


#获取token
def get_sign():
    SECRET = 'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8'
    md5 = "AUTH-TIMESTAMP=" + timestamp + "&AUTH-TOKEN=" + token + "#" + SECRET
    m1 = hashlib.md5()
    m1.update(md5.encode("utf-8"))
    sign = m1.hexdigest()
    return sign


url = 'http://link-test.bi.sensetime.com'
url = 'http://127.0.0.1:8080'


def get_para(object):
    str1 = ""
    for obj in object.items():
        key, value = obj
        str1 = str1 + key + "=" + value + "&"
    str1 = str1[:-1]
    return str1


headers = {
    "Content-Type": "application/json;charset=UTF-8",
    'AUTH-TOKEN': token,
    'AUTH-TIMESTAMP': timestamp,
    'AUTH-SIGN': get_sign(),
    'LDID': 'SPS-cc8d61e43319262798afb06affea4f68'
}

response = requests.get(
    url + "/sl/v2/record/export",
    headers=headers)
print(response.text)
