#coding:utf-8
from selenium import webdriver
from time import sleep

def main():
    data = open("data.txt","r")
    args = data.readlines()
    for li in args:
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        sleep(1)
        driver.find_element_by_id("kw").send_keys(li)
        sleep(3)
        driver.quit()


if __name__=="__main__":
    main()