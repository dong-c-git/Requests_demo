#coding:utf-8
import requests
import unittest

class Test_dome(unittest.TestCase):
    '''
    get login sessionid
    '''
    login_url = "http://10.152.36.134:8890/sensego/2.0/web/console/ui/api/sensego/console/v1.0/tree/user"
    headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
               "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiSUQxNTY3IiwiY29tcGFueV9pZCI6IklEMTE1MCIsInVzZXJfdHlwZSI6ImFkbWluIiwibm9kZV9pZCI6IjAwMCIsImFrIjoibDEtZTAxYmZmMjItODBhNWNjOGY5MjM0IiwidXNlcl9hZ2VudCI6MSwiZXhwIjoxNTc2NjU1NDUzfQ.fJb3DYly5NVwVN5e38pL2aXQoVsyLdarJ5Wj9FzDmSg"}


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_get(self):
        pass

    def login(self):
        '''
        get sessionid keep login status
        '''
        login_req = requests.sessions()
        login_res = login_req.get(url=self.login_url,headers=self.headers)
        print(login_req.json())
        #return login_req.get_cookies


if __name__ == '__main__':
    test1 = Test_dome()
    test1.login()
