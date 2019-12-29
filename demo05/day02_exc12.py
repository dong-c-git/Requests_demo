#coding:utf-8
"""
使用列表生成式找出列表中大于0的数字
[1,3,-3,4,-2,8,-7,6]
"""
def list_set(list):
    temp = [i for i in list if i > 0]
    print(temp)

if __name__ == "__main__":
    list1 = [1,3,-3,4,-2,8,-7,6]
    list_set(list1)