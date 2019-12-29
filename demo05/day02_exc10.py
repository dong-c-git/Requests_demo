#coding:utf-8
"""
作业10：已知一个字符串为"hello_world_yoyo",
如何得到一个队列["hello","world","yoyo"]

"""
def strrelace(str):
    list1 = str.split("_")
    print(list1)
    return list1

if __name__=="__main__":
    str = "hello_world_yoyo"
    strrelace(str)

