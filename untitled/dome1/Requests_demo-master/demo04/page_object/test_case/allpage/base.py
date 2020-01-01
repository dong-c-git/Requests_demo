#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Page(object):
    """
    基本类，用于所有页面的继承
    """
    def __init__(self,selenium_driver,base_url,parent):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
        self.tabs = {}