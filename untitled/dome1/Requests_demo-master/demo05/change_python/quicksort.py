# coding:utf-8


def quicksort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot: less.append(x)
        else: greater.append(x)
    print("less is:", less)
    print("pivot is:", pivot)
    print("greater is:", greater)
    return quicksort(less) + [pivot] + quicksort(greater)

list1 = [9,8,4,5,32,64,2,1,0,10,19,27]
list2 = quicksort(list1)
print(list2)

print("Hello %(name)s!" % {"name":"tom"})
