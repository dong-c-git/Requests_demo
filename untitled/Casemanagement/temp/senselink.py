#coding:utf-8
import requests
import hashlib
import time

app_key = "e1080ac2d5d8baae"
app_secret = "eedb1dfe5a0082f9d9b18123ee50ccba"
path = "https://link.bi.sensetime.com"
uri = "/api/v3/event/viewSub"

nowtime = lambda:int(round(time.time())*1000)
# timestamp = str(nowtime())
# print(timestamp)
def get_sign(func):
    h1 = hashlib.md5()
    timestamp = str(nowtime())
    h1.update((timestamp+'#'+app_secret).encode(encoding='utf-8'))
    data = {
        "app_key": app_key,
        "sign": h1.hexdigest(),
        "timestamp": timestamp,
    }
    print(data)
    def wrappend(data):
        data = data
        return func(data)
    return wrappend

@get_sign
def get_status(data=''):
    response = requests.get(path+uri,params=data)
    print(response.text)


def smart_decorator(decorator):
    def decoreator

if __name__=="__main__":
    get_status()