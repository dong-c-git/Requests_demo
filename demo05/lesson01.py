#coding:utf-8

def printNarcissisticNumber():
    '判断一个数是否是水仙花数'
    for num in range(100, 1001):
        geWei = num % 10
        baiWei = int(num / 100)
        shiWei = int((num - baiWei * 100) / 10)
        sum = geWei * geWei * geWei + shiWei * shiWei * shiWei + baiWei * baiWei * baiWei
        if sum == num:
            print("%d是水仙花数" % num)

def jiujiuchefabiao():
    '实现99乘法表'
    for i in range(1, 10):
        for j in range(1, i + 1):
            d = i * j
            print('%d*%d=%-2d' % (i, j, d), end=' ')
        print()

def three():
    a = [1,6,8,11,9,1,8,6,8,7,8]
    #排序
    a.sort()
    print(a)
    #去重
    print(list(set(a)))

def four():
    a = [1,3,5,7,11]
    #反转
    print(a[::-1])
    #取奇数位
    print(a[::2])


if __name__ == "__main__":
    #three()
    four()
