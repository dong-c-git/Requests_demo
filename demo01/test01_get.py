#coding：utf-8
'''
响应数据：
   响应对象.url          获取响应地址
   响应对象.status_code  获取响应状态码
   响应对象.text         以文本形式显示响应内容

'''
#1、导包
import requests
#2、调用get
url = "http://www.baidu.com"
r = requests.get(url)
#3、获取请求url地址
print("请求url是：",r.url)
#4、获取响应状态码
print("请求状态码是：",r.status_code)
#5、获取响应信息，文本形式
print("请求响应文本是：",r.text.encode("utf-8"))
