#coding:utf-8
import requests
import re
import time
from requests_toolbelt import MultipartEncoder
from lxml import etree
import os

def login():
    s = requests.session()
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    get_url = "http://49.235.92.12:9000/admin/login/"
    get_csrf = s.get(url=get_url,headers=headers)
    #获取csrf 和 匹配请求参数的csrfmiddlewaretoken
    csrfmiddlewaretoken = re.findall("name=\'csrfmiddlewaretoken\' value=\'(.*?)\'",get_csrf.text)
    #更新会话headers
    headers["Cookie"] = "csrftoken={}".format(get_csrf.cookies["csrftoken"])
    s.headers.update(headers)
    #post登录参数传递：
    data = {"csrfmiddlewaretoken":csrfmiddlewaretoken[0],
            "username":"admin",
            "password":"yoyo123456",
            "next":"/admin/"}
    session_id = s.post(url=get_url,data=data)
    #通过session获取admin首页
    admin_url = "http://49.235.92.12:9000/admin/"
    admin = s.get(admin_url)
    if admin.status_code == 200:
        print("请求状态码正常")
    else:
        print("请求状态码异常,请修正请求,请求的状态码是:{}".format(admin.status_code))
        return
    if "Site Administration | Django Site Admin" in admin.text.title():
        print("登录成功，获取admin首页title是:{}".format(admin.text.title()))
    else:
        print("获取首页title失败，登录失败，请修正！返回请求报文:{}".format(admin.text))
        return

def login2():
    s = requests.session()
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    get_url = "http://49.235.92.12:8020/xadmin/"
    get_csrf = s.get(url=get_url,headers=headers)
    #获取csrf 和 匹配请求参数的csrfmiddlewaretoken
    csrfmiddlewaretoken = re.findall("name=\'csrfmiddlewaretoken\' value=\'(.*?)\'",get_csrf.text)
    #更新会话headers
    headers["Cookie"] = "csrftoken={}".format(get_csrf.cookies["csrftoken"])
    s.headers.update(headers)
    #post登录参数传递：
    data = {"csrfmiddlewaretoken":csrfmiddlewaretoken[0],
            "username":"admin",
            "password":"yoyo123456",
            "this_is_the_login_form":1,
            "next":"/xadmin/"}
    session_id = s.post(url=get_url,data=data)
    print("登录后返回信息是",session_id.text)
    #返回登录后的页面
    print("登录后cookies是",session_id.cookies)
    print("登录后的headers",session_id.request.headers)
    print("请求头",session_id.headers)
    print("会话headers",s.headers)
    #更新会话请求头
    s.headers.update(session_id.request.headers)
    add_docment_url = "http://49.235.92.12:8020/xadmin/hello/articleclassify/add/"
    get_add_docment = s.get(url=add_docment_url)
    print("增加页面返回内容:",get_add_docment.text)
    #获取请求需要使用的csrftoken
    addmiddlewaretoken = re.findall("name=\'csrfmiddlewaretoken\' value=\'(.*?)\'",get_add_docment.text)
    print(addmiddlewaretoken)
    #提交请求数据
    from requests_toolbelt import MultipartEncoder
    import time
    from lxml import etree
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


def login_xadmin(s):
    url = os.environ["xadmin_host"]+"/xadmin/"
    r1 = s.get(url)
    # 第一次请求登录页
    # 正则提取csrfmiddlewaretoken
    csrfmiddlewaretoken = re.findall("name=\'csrfmiddlewaretoken\' value=\'(.+?)\'",r1.text)
    print(csrfmiddlewaretoken[0])
    # 登录
    body = {
              "csrfmiddlewaretoken": csrfmiddlewaretoken[0],
              "username": "admin",
              "password": "yoyo123456",
              "this_is_the_login_form": "1",
              "next": "/xadmin/"
           }
    r = s.post(url, data=body)
    print(r.text)
    if "主页面 | 后台页面" in r.text:
        print("登录成功")
    else:
        print("登录失败")


def add_docment(s,docment_name="冠状病毒_test双黄连"):
    url = os.environ["xadmin_host"]+"/xadmin/hello/articleclassify/add/"
    r3 = s.get(url)
    token2 = re.findall("name=\'csrfmiddlewaretoken\' value=\'(.*?)\'",r3.text)
    print(token2[0])
    #multipart请求类型，类型post请求
    m = MultipartEncoder(fields=[("csrfmiddlewaretoken",token2[0]),
                                 ("csrfmiddlewaretoken",token2[0]),
                                 ("n",docment_name),
                                 ("_save","")])
    r4 = s.post(url=url,data=m,headers={'Content-Type': m.content_type})
    print(r4.text)
    return r4.text

def get_add_docment(result):
    """获取添加文本结果"""
    demo = etree.HTML(result)
    nodes = demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
    print(nodes[0].text)
    return nodes[0].text


def is_add_success(s):
    url_r = "http://49.235.92.12:8020/xadmin/hello/articleclassify/"
    x = '//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a'
    r = s.get(url_r)
    demo = etree.HTML(r.text)
    nodes = demo.xpath(x)
    t = nodes[0].text
    print("获取到页面值：%s" % t)
    return t


if __name__=="__main__":
    s = requests.session()
    login_xadmin(s)
    add_docment(s,"双黄连月饼")
    is_add_success(s)
