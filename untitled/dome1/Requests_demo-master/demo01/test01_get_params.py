#coding:utf-8
'''
get请求带参数化：
   1、http://www.baidu.com?id=1001
   2、http://www.baidu.com?id=1001，1002
请求get请求：
   1、请求方法：GET
参数：
   params:字典或者字符串（推荐使用字典）
响应：
   响应对象.url
   响应对象.status_code
   响应对象.text
'''
#1、导包
import requests
#2、调用get
url = "http://www.baidu.com"
#不推荐写静态方法
#url = "http://www.baidu/com?id=1001"
#定义字典
#单个参数
#params = {"id":1001}
#多个参数
#params = {"id":[1001,1002]} #写法不推荐
#params = {"id":'1001,1002'}  #%2c  ASCI值为逗号
#多个键值形式的参数
params = {"id":1001,"kw":"北京"}
#请求带参数params
r = requests.get(url,params=params)
#3、查看请求url
print("请求url：",r.url)
print("请求状态码：",r.status_code)
print("请求响应内容：",r.text.encode("utf-8"))


