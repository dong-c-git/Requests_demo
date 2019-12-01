#coding:utf-8
#locustio环境安装：
'''
1、使用pip安装locustio(locustio支持的版本：2.7,3.4,3.5,3.6)
pip install locustio
pip show locustio
使用locust --help查看帮助信息

'''
from locust import HttpLocust,TaskSet,task

class BlogDemo(TaskSet):
    """用户行为：打开我的博客首页"""
    @task(1)
    def open_blog(self):
        #定义requests的请求头
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        r = self.client.get("/yoyoketang",headers=header,verify=False)
        print(r.status_code)
        assert r.status_code == 200

class websitUser(HttpLocust):
    task_set = BlogDemo
    min_wait = 3000    #单位毫秒
    max_wait = 6000    #单位毫秒

if __name__ == "__main__":
    import os
    os.system("locust -f locustio_01.py --host=https://www.cnblogs.com")


