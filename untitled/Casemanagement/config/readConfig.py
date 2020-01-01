#coding:utf-8
import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
configpath = os.path.join(cur_path,"cfg.ini")
conf = configparser.ConfigParser()
conf.read(configpath)

smtp_server = conf.get("email","smtp_server")

sender = conf.get("email","sender")

psw = conf.get("email","psw")

receiver = conf.get("email","receiver")

port = conf.get("email","port")

ak = conf.get("sign","ak")

sk = conf.get("sign","sk")

test_url = conf.get("url","test_url")

if __name__=="__main__":
    print("smtp_server:",smtp_server)
    print("sender:",sender)
    print("psw:",psw)
    print("receiver:",receiver)
    print("port:",port)
    print("ak",ak)
    print("sk",sk)