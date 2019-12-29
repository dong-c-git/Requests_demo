#coding:utf-8
"""
作业6：
如果一个正整数等于除它本身之外所有除数之和就称为完全数；
example:
6 = 1+2+3
28 = 14+7+4+2+1
求1000以下的完全数：

"""
def allnum():
    for i in range(1,1001):
        sum = 0
        for j in range(1,i):
            if i%j == 0:
                sum += j
        if sum == i:
            print(i)


if __name__=="__main__":
    allnum()