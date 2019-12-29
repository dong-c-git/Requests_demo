#coding:utf-8
import pytest
import requests

def test_01():
    """星座运势-错误的请求KEY"""
    url = "http://web.juhe.cn:8080/constellation/getAll"
    params = {"key":"1234567890","consName":"射手座","type":"today"}
    req = requests.get(url=url,params=params)
    #print(req.url)
    #print(req.text)
    assert "KEY ERROR!"==req.json().get("reason")
    assert 10001 == req.json().get("error_code")


def test_02():
    """星座运势-无权限的key"""
    url = "http://web.juhe.cn:8080/constellation/getAll"
    params = {"key":"57d46b7258fc47e14290c33537f23d36","consName":"射手座","type":"today"}
    req = requests.get(url=url,params=params)
    #print(req.url)
    #print(req.text)
    #assert "KEY ERROR!"==req.json().get("reason")
    assert 10002 == req.json().get("error_code")


def test_03():
    """星座运势-错误的星座类型"""
    url = "http://web.juhe.cn:8080/constellation/getAll"
    params = {"key":"cde5e16435cd0217f505a88898b60707","consName":10,"type":"today"}
    req = requests.get(url=url,params=params)
    #print(req.url)
    #print(req.text)
    assert "NAME ERROR!"==req.json().get("reason")
    assert 205801 == req.json().get("error_code")


def test_04():
    """星座运势-错误的星座名称"""
    url = "http://web.juhe.cn:8080/constellation/getAll"
    params = {"key":"cde5e16435cd0217f505a88898b60707","consName":"大泽九章","type":"today"}
    req = requests.get(url=url,params=params)
    #print(req.url)
    #print(req.text)
    assert "Does not exist in the consName!"==req.json().get("reason")
    assert 205802 == req.json().get("error_code")

#test_04()

def test_05():
    """星座运势-正确的星座名称"""
    url = "http://web.juhe.cn:8080/constellation/getAll"
    params = {"key":"cde5e16435cd0217f505a88898b60707","consName":"射手座","type":"today"}
    req = requests.get(url=url,params=params)
    #print(req.url)
    #print(req.text)
    assert "射手座"==req.json().get("name")
    assert "200" == req.json().get("resultcode")

#test_05()