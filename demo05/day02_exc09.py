#coding:utf-8
"""
作业8：已知一个数列：1，1，2，3，5，8，13
从3开始每一项等于前两项之和，求满足规律100以内的斐波那契数列
"""
def feibonaqi(num):
    if num < 1:
        return 0
    elif num == 1 or num == 2:
        return [1]
    elif num > 2:
        return_list = [1,1]
        per = return_list[-2]
        res = return_list[-1]
        for i in range(2, num):
            ret = per + res
            if ret > 100:
                break
            return_list.append(ret)
            per = return_list[-2]
            res = return_list[-1]
        return return_list
    else:
        return None

if __name__ == "__main__":
    num = 100
    test = feibonaqi(num)
    print(test)