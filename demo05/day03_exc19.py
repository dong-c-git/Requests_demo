#coding:utf-8
import requests
'''
python作业19：
访问接口地址http://49.235.92.12:9000/api/test/demo（不需要登录）
根据name为yoyo111（list里面顺序不是固定的），取出对应的email值：123445@qq.com
{"code": 0, "msg": "success!", "datas": [{"age": 20, "create_time": "2019-09-15", "id": 1, "mail": "283340479@qq.com", "name": "yoyo", "sex": "M"}, {"age": 21, "create_time": "2019-09-16", "id": 2, "mail": "123445@qq.com", "name": "yoyo111", "sex": "M"}]}
'''
class GetInformation:


    @staticmethod
    def getemail():
        infourl = "http://49.235.92.12:9000/api/test/demo"
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
        req = requests.get(url=infourl,headers=headers)
        #print(req.json().get("datas"))   #取出data中用户信息
        for i in req.json().get("datas"):
            if i.get("name") == 'yoyo111':
                print("yoyo111对应的email是：",i.get("mail"))

if __name__=="__main__":
    test = GetInformation.getemail()

