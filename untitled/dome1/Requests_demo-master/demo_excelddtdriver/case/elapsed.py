#coding:utf-8
import requests

s = requests.session()
ret = s.get("http://www.baidu.com")
print("elapsed数据：",ret.elapsed)
print("总时长：",ret.elapsed.total_seconds)
print("微秒部分时长：",ret.elapsed.microseconds)
print("秒数：",ret.elapsed.seconds)
print("天数：",ret.elapsed.days)
print("最大时间：",ret.elapsed.max)
print("最小时间：",ret.elapsed.resolution)
