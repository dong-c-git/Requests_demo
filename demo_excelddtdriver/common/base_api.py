#coding:utf-8
import json
import requests
import time
from demo_excelddtdriver.common.writeexcel import Write_excel,copy_excel
from demo_excelddtdriver.common.readexcel import ExcelUtil

def send_requests():
    url = "https://leetcode-cn.com/problemset/all/"
    res_headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    s = requests.session()    #session创建的空会话，headers是默认代理，cookies是一个空的对象
    res = s.get(url=url,headers=res_headers)
    print("重新设置请求头后的请求头：",res.headers)
    print("请求后的cookie是：",res.cookies)
    print("取出的csrftoken内容：",res.cookies["csrftoken"])
    print("获取csrftoken：",[i for i in res.cookies][0].value)
    return s,res.cookies["csrftoken"],res.cookies

def login_leetcode():
    url = "https://leetcode-cn.com/accounts/login/"
    session, csrftoken, cookies = send_requests()
    print(cookies)
    res_headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
                   "x-csrftoken":csrftoken,
                   "cookie":str(cookies),
                   "origin":"https://leetcode-cn.com",
                   "x-requested-with":"XMLHttpRequest",
                   "sec-fetch-site":"same-origin"}
    body = {"csrfmiddlewaretoken":csrftoken,"login":"1277207158@qq.com","password":"dong159753","next":"/problemset/all/"}
    login_res = session.post(url=url,headers=res_headers,data=body,cookies=cookies)
    print("请求后状态码：",login_res.status_code)
    print("请求后报文：",login_res.text)
    print("请求报文：",body)
    print("登录状态的session:",login_res.cookies)

def send_requests(s,testdata):
    """
    封装requests请求
    :param s:           session会话消息
    :param testdata:    测试数据，方法内部根据传入测试数据类型进行处理
    :return:            返回请求结果
    """
    #1、处理请求数据，必传参数部分
    method = testdata["method"]
    url = testdata["url"]
    #2、处理请求参数中非必传参数部分
    # url后面的params参数
    try:
        params = eval(testdata["params"])
    except:
        params = None
    #请求头部headers
    try:
        headers = eval(testdata["headers"])
        print("请求头部:%s"%headers)
    except:
        headers = None
    #post请求body类型
    type = testdata["type"]
    #执行的用例条数：
    test_nub = testdata["id"]
    print("******正在执行用例：---- %s ---- ********"%test_nub)
    print("请求方式：%s,请求url：%s"%(method,url))
    print("请求params:%s"%params)
    #post请求body内容
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}
    #3、判断传data数据还是json数据
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata
    if method == "post":print("post请求body类型为:%s，body内容为：%s"%(type,body))
    verify = False
    res = {}     #定义空字典接收返回数据
    try:
        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify)
        print("页面返回信息：%s"%r.content.decode("utf-8"))
        res["id"] = testdata["id"]
        res["rowNum"] = testdata["rowNum"]
        res["statuscode"] = str(r.status_code)   #转换状态码格式
        res["text"] = r.content.decode("utf-8")
        res["times"] = str(r.elapsed.total_seconds())  #接口请求时间转str
        if res["statuscode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果：%s---->%s"%(test_nub,res["result"]))
        else:
            res["result"] = "fail"
        return res
    except Exception as msg:
        res["msg"] = str(msg)
        return res

def write_result(result,filename="result.xlsx"):
    #返回结果行数row_nub
    row_nub = result["rowNum"]
    #写入statucode
    wt = Write_excel(filename)
    #写入statuscode
    wt.write(row_nub,8,result["statuscode"])
    wt.write(row_nub,9,result["times"])
    wt.write(row_nub,10,result["error"])
    wt.write(row_nub,12,result["result"])
    wt.write(row_nub,13,result["msg"])


if __name__=="__main__":
    data = ExcelUtil("debug_api.xlsx").dict_data()
    print(data[0])
    s = requests.session()
    res = send_requests(s,data[0])
    copy_excel("debug_api.xlsx","result.xlsx")
    write_result(res,filename="result.xlsx")
