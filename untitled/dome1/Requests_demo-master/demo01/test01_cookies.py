#coding:utf-8
import requests
#1、cookie操作
url = "http://www.baidu.com"
r = requests.get(url)
#获取请求的cookie
print(r.cookies)
#获取请求的cookie是字典可以通过键值形式取值
print(r.cookies["BDORZ"])

#2、content操作
url_img = "https://www.baidu.com/img/bd_logo1.png?where=super"
r = requests.get(url=url_img)
#获取响应content内容
#print(r.text)   图片以text形式解析--->乱码
print(r.content)   #返回的是图片的字节流
with open("baidu.png","wb") as f:
    f.write(r.content)

