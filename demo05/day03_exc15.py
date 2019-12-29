#coding:utf-8
'''
python作业15：
根据接口文档使用python发get请求，能请求成功
历史上的今天AppKey：57d46b7258fc47e14290c33537f23d36
https://www.juhe.cn/docs/api/id/63
'''
import requests

'''
接口地址：http://api.juheapi.com/japi/toh
返回格式：json
请求方式：http get/post
请求示例：http://api.juheapi.com/japi/toh?key=您申请的KEY&v=1.0&month=11&day=1
'''
class JuHe(object):
    '''
    接口参数：
    1、key	是	string	在个人中心->我的数据,接口名称上方查看
 	2、v	是	string	版本，当前：1.0
 	3、month	是	int	月份，如：10
 	4、day	是	int	日，如：1
    '''
    @staticmethod
    def gettianqi():
        geturl = "http://api.juheapi.com/japi/toh"
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
        getparams = {"key":"57d46b7258fc47e14290c33537f23d36",
                     "v":"1.0",
                     "month":"12",
                     "day":"29"}
        req = requests.get(url=geturl,headers=headers,params=getparams)
        print(req.url)          #请求url
        print(req.text)         #返回文本形式
        print(req.status_code)  #返回状态码
        print(req.content)      #返回bytes
        print(req.json())       #返回字典
if __name__ =="__main__":
    test1 = JuHe.gettianqi()
