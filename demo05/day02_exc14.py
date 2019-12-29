#coding:utf-8
"""
作业14：
a = [1,2,3,4,5]
b = ["a","b","c","d","e"]
需要得出：c = ["a1","b2","c3","d4","e5"]
"""
def sethebin(list1,list2):
    if not list1 and not list2:
        return None
    if len(list1) == len(list2):
        c = []
        for i in range(len(list2)):
            c.append(str(list2[i])+str(list1[i]))
        print(c)
        return c

if __name__=="__main__":
    a = [1,2,3,4,5]
    b = ["a","b","c","d","e"]
    sethebin(a,b)