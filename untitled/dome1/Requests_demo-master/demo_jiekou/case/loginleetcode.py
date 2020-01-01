#coding:utf-8
import requests
from demo_jiekou.common.logger import Log
#禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Leetcode():
    s = requests.session()
    def __init__(self,s):
        self.s = s

    def login(self):
        url = "https"