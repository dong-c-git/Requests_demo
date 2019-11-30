import requests
import unittest

class V2exTestCase(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.v2ex.com/"
        self.querystring = {"tab":"qna=qna"}
        self.headers = {
                'User-Agent': "PostmanRuntime/7.19.0",
                'Accept': "*/*",
                'Cache-Control': "no-cache",
                'Postman-Token': "3ad8411b-0d57-419a-8812-f643374fc672,614df146-15c0-494a-a26a-943e202eb58f",
                'Host': "www.v2ex.com",
                'Accept-Encoding': "gzip, deflate",
                'Cookie': '''__cfduid=d87aba7721a79e059390c4ef6bfc4c1771574131614; PB3_SESSION="2|1:0|10:1574145185|11:PB3_SESSION|40:djJleDoxMTMuMTE2LjIzNy44OTo0NjQ4OTM3Mg==|aa43e0c41f2e2e18ab21999123a274a9698257988c2e356a6f8bc6dae6667322"; V2EX_LANG=zhcn; V2EX_TAB="2|1:0|10:1574146443|8:V2EX_TAB|8:dGVjaA==|0ce0019ca17de91444ce0f1224d30ac89d1815ccf86513c5ed951f091d8d18c4"''',
                'Connection': "keep-alive",
                'cache-control': "no-cache"
                }

    def test_v2ex(self):
        response = requests.request("GET", url=self.url, headers=self.headers, params=self.querystring)
        self.assertEqual(response.status_code,200)
        print(response.text)

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()
