#coding:utf-8
import requests
import unittest
import uuid
import time
import random
import hmac
import hashlib
import sys
sys.path.append("config")
import js2py

class authentication():
    """生成签名"""
    def __init__(self,ak,sk):
        #获取时间戳
        timestime = time.time()
        print(int(timestime))
        self.timestime = str(int(timestime))
        # 获取随机字符串
        ruuid = ""
        for i in range(32):
            ruuid += random.choice("ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678")
        self.ruuid = ruuid
        print("ruuid是:",self.ruuid)
        #获取ak
        self.ak = ak
        self.sk = sk
        #获取nonce
        # str1 = uuid.uuid4()
        # str2 = "".join(str(uuid.uuid4()).split("-")).upper()
        # print(str2)
        nonce2 = js2py.eval_js("function uuid(len) {len = len || 32; var $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';var maxPos = $chars.length; var pwd = '';　for (i = 0; i < len; i++) {pwd += $chars.charAt(Math.floor(Math.random() * maxPos));}return pwd;} var nonce = uuid(32)")
        print("nonce2is :",nonce2)
        self.uuid = nonce2
        # 组合参数
        arr = []
        arr.append(str(int(timestime)))
        arr.append(ak)
        arr.append(self.uuid)
        #print("排序前:", arr)
        arr.sort()
        #print("排序后:", arr)
        resultstr = "".join(arr)
        print(resultstr)
        js = """
        function creatsign(join_str,sk) {
        return CryptoJS.HmacSHA256(join_str, sk);
        }
        var join_str = "%s";
        var sk = "%s";
        var sign = creatsign(join_str,sk);
        """%(resultstr,sk)
        print(js)

        js2 = """
        <script src="core.js"></script>
        <script src="hmac.js"></script>
        <script src="sha256.js"></script>
        <script src="enc-base64.js"></script>
        function aa() {
        var val = document.getElementById('pwd').value;
        //此处只能是"Message"，不然会加密结果不对
        var hash = CryptoJS.HmacSHA256("Message", val);
        var hashInBase64 = CryptoJS.enc.Base64.stringify(hash);
        console.log(hashInBase64)
        }</script>   
        """
        context = js2py.EvalJs()
        context.execute(js)
        test = context.sign
        print(test)
        #print(resultstr)
        # js = 'var sk = "%s"; var sign = CryptoJS.HmacSHA256("%s", sk);'%(sk,resultstr)
        # print(js)
        # eet = js2py.eval_js(js)
        # print(eet)
        #signnew = js2py.evaljs("var sk = {}; var sign = CryptoJS.HmacSHA256({}, sk);".format(sk,resultstr))
        #rint("signnew is:",signnew)
        self.resultstr = "1577250945T2NCp5PG7xMyJCrpG2QaPH3E6FZtnDebl1-e01bff22-80a5cc8f9234"
        # hmac_sha256加密
        signature = hmac.new(bytes(self.resultstr, encoding='utf-8'),bytes(self.sk, encoding='utf-8'),digestmod=hashlib.sha256).digest()
        print("转换后",signature)
        signature2 = hmac.new(bytes(self.resultstr,encoding='utf-8'),bytes(self.sk,encoding='utf-8'),digestmod=hashlib.sha256).digest()
        print("转换后2:",type(signature2))
        # 二进制转为HEX
        self.HEX = signature.hex()
        print("HEx:",self.HEX)
        # 将字符串换为小写
        self.lowsigne = self.HEX.lower()
        #print(lowsigne)

    def main(self):
        url = "http://172.30.1.176:11111/senserealty/platform/v1.0/confextra"
        querystring = {"store_id": "07e0822ad3", "type_id": "-1", "company_id": "ID1150", "group_name": ""}
        headers = {
            'Content-Type': "application/json",
            'ak':self.ak,
            'sign':self.HEX,
            'nonce':self.uuid,
            'ts':self.timestime,
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "172.30.1.176:11111",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        print("the headers is:",headers)
        res = requests.session()
        ret = res.get(url=url,headers=headers,params=querystring)
        #response = requests.request("GET", url, headers=headers, params=querystring)
        print(ret.text)
        print(ret.status_code)

if __name__=="__main__":
    import sys
    from os import path
    #引包路径处理
    packagepath = path.join(path.dirname(path.dirname(__file__)),"config")
    sys.path.append(packagepath)
    import readConfig
    ak = readConfig.ak
    sk = readConfig.sk
    print("ak是:",ak)
    print("sk是:",sk)
    ak = "l1-e01bff22-80a5cc8f92347777777"
    sk = "d22e16b7a7465b1b51e701299d5ac45b7777777"
    test = authentication(ak,sk)
    test.main()
    js = "nonce = uuid(32)"

#2bd8a4e87b017d22ea3d4c398a9181232bb01fbdcaa15ee0de35ee09247516fd
#77cab74c1461d406377672ee848e963e6a55a1b88c36328f799deebd0f79fff1
#0ddfae349cf1fbd3f478284c427973862a9b6637de48e1c50ed8f02352497c81
#1da4272a2ba08f1a9a7d48c068a3a8e9a9f4f013a4110cbd77118dbda9a82bc5
#157717808259714c7ccfc340fb9115f3a8c1afe824l1-e01bff22-80a5cc8f9234
