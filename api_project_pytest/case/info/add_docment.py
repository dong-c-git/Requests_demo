#coding:utf-8
'''
作业27
找个multipart/form-data接口能提交成功
先登录
http://49.235.92.12:8020/xadmin/
admin yoyo123456
文章分类页面
http://49.235.92.12:8020/xadmin/hello/articleclassify/
新增一篇文章
'''
import requests
import re
from requests_toolbelt import MultipartEncoder
import time
from lxml import etree

def adddocment():
    s = requests.session()
    login_url = "http://49.235.92.12:8020/xadmin/"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    login_csrf = s.get(url=login_url,headers=headers)
    #获取csrf 和 匹配请求参数的csrfmiddlewaretoken
    csrfmiddlewaretoken = re.findall("name=\'csrfmiddlewaretoken\' value=\'(.*?)\'",login_csrf.text)
    #更新登录后会话headers
    headers["Cookie"] = "csrftoken={}".format(login_csrf.cookies["csrftoken"])
    s.headers.update(headers)
    #登录参数传递：
    data = {"csrfmiddlewaretoken":csrfmiddlewaretoken[0],
            "username":"admin",
            "password":"yoyo123456",
            "this_is_the_login_form":1,
            "next":"/xadmin/"}
    login_session = s.post(url=login_url,data=data)
    #print("登录后返回信息是",login_session.text)
    #更新会话请求头
    s.headers.update(login_session.request.headers)
    add_url = "http://49.235.92.12:8020/xadmin/hello/articleclassify/add/"
    get_add_docment = s.get(url=add_url)
    print("增加页面返回内容:",get_add_docment.text)
    #获取请求需要使用的csrftoken
    addmiddlewaretoken = re.findall("name=\'csrfmiddlewaretoken\' value=\'(.*?)\'",get_add_docment.text)
    print(addmiddlewaretoken)
    #提交请求数据
    m = MultipartEncoder(fields=[("csrfmiddlewaretoken",addmiddlewaretoken[0]),
                                 ("csrfmiddlewaretoken",addmiddlewaretoken[0]),
                                 ("n","冠状病毒"+str(int(time.time()))),
                                 ("_save","")],)
    post_url = "http://49.235.92.12:8020/xadmin/hello/articleclassify/add/"
    r4 = s.post(url=post_url,data=m,headers={'Content-Type': m.content_type})
    print(r4.text)
    x = '//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a'
    demo = etree.HTML(r4.text)
    nodes = demo.xpath(x)
    t = nodes[0].text
    print(t)

if __name__ == "__main__":
    adddocment()