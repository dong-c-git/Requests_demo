#coding:utf-8
"""
1、encoding
   获取请求编码
   设置响应编码
2、headers
   获取响应信息头信息

"""
#1、导包
import requests
#2、调用get方法
url = "http://www.baidu.com"
r = requests.get(url)
#3、查看请求默认编码
print("请求编码是：",r.encoding)
#4、设置响应报文请求编码并打印返回内容
r.encoding = "utf-8"
print(r.text)
#5、查看响应头信息，返回信息的cookie相关信息一般在headers中
print(r.headers)

print(r.cookies)

