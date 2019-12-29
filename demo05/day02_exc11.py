#coding:utf-8

def count_num(list):
    if not list:
        return None
    list_len = len(list)
    count_num = 0
    for i in list:
        if type(i) != type(1):
            list_len -= 1
            continue
        if i < 0:
            count_num += 1
    print("正整数个数为：",list_len-count_num)
    print("负数个数是：", count_num)

if __name__ == "__main__":
    list1 = [1,3,5,7,0,-1,-9,-4,-5,8]
    count_num(list1)