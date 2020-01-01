#coding:utf-8
import unittest
import requests
#导入登录模块,保持会话
import sys
sys.path.append("/common")
from login import StoreManager
#from common.logger import Log

class TestStore(unittest.TestCase):
    #log = Log()
    def setUp(self):
        s = requests.session()
        storelogin = StoreManager(s)
        self.token,self.company_id,self.loginresult = storelogin.usertoken('testSK02', 'Goodtest01')
        self.session = s
        self.url = "http://10.152.36.134:8890/sensego/2.0/web/console/ui/api/sensego/console/v1.0/login"
        self.headers = {"Content-Type":"application/json",
                        "User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}

    def test_getstore(self):
        """
        get store
        :return:
        """
        get_storeurl = "/".join(self.url.split("/")[:-1:]) + "/store/all"
        get_storeheaders = {
            "Content-Type": "application/json",
            "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
        get_storeheaders["token"] = self.token
        params = {"company_id":self.loginresult["company_id"]}
        #self.log.info("requests url:%s"%get_storeurl)
        #self.log.info("requests headers:%s"%get_storeheaders)
        result = self.session.get(url=get_storeurl,headers=get_storeheaders,params=params)
        #self.log.info("獲取結果：%s"%result.json())
        #self.log.info("获取是否登录成功：%s"%result["success"])
        #self.assertEqual(result["success"],True)   #比较断言结果
        #self.log.info("----end----")
        print(result.json())
        print(result.status_code)


    def test_addstore(self):
        """
        url='http://10.152.36.134:8890/sensego/2.0/web/console/ui/api/sensego/console/v1.0/store/add'
        url='http://10.152.36.134:8890/sensego/2.0/web/console/ui/api/sensego/console/v1.0/'
        """
        post_storeurl = "/".join(self.url.split("/")[:-1:]) + "/store/all"
        post_storeheaders = {
            "Content-Type": "application/json",
            "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
        post_storeheaders["token"] = self.token
        params = {"company_id": self.loginresult["company_id"]}
        postdata = '{store_name:"测试地址04",store_desc:"测试地址04",node_id: "000003",callback_url: "",company_id: "ID1150",product_line: 8,sense_id: "",opq_model: "3.0.0"}'.encode("utf-8")
        # self.log.info("requests url:%s"%get_storeurl)
        # self.log.info("requests headers:%s"%get_storeheaders)
        result = self.session.post(url=post_storeurl,headers=post_storeheaders,data=postdata)
        # self.log.info("獲取結果：%s"%result.json())
        # self.log.info("获取是否登录成功：%s"%result["success"])
        # self.assertEqual(result["success"],True)   #比较断言结果
        # self.log.info("----end----")
        print("test add store:",result)
        print(result.status_code)


if __name__ == "__main__":
    unittest.main()

