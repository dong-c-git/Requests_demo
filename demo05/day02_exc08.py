#coding:utf-8
"""
作业8：已蜘一个队列如：[1,3,5,7],如何把第一个数字，放到第三个位置得到[3,5,1,7]

"""

def setlist(list):
    temp = list.pop(0)
    list.insert(2,temp)
    print(list)

if __name__=="__main__":
    list1 = [1,3,5,7]
    setlist(list1)