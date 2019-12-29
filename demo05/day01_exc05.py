#coding:utf-8
"""
作业6：
如果一个正整数等于除它本身之外所有除数之和就称为完全数；
example:
6 = 1+2+3
28 = 14+7+4+2+1
求1000以下的完全数：

"""
'''
作业5：如何判断一个数组是对称数组，如果是对称的返回true,如果不是返回false
example:
true:
[1,2,0,2,1]
[1,2,3,3,2,1]
false:
[1,"a",0,"2",0,"a",1]
'''
def equallist(list):
    '''判断数组是否对称'''
    if not list:
        return False
    if len(list) == 1:
        return True
    arglist = list
    lenlist = len(list)
    mid = lenlist//2
    if lenlist%2 == 0:
        eq1 = arglist[:mid]
        eq2 = arglist[mid:lenlist][::-1]
        return eq1 == eq2
    else:
        eq1 = arglist[0:mid]
        eq2 = arglist[mid+1:lenlist][::-1]
        return eq1 == eq2

if __name__=="__main__":
    list1 = [1,2,0,2,1]
    list2 = [1, 2, 3, 3, 2, 1]
    list3 = [1,"a",0,"2",0,"a",1]
    list4 = []
    list5 = [1]
    for i in list(range(1,6)):
        args = "list{}".format(i)
        test = equallist(eval(args))
        print("%s 对称数组判断结果：%s"%(args,test))