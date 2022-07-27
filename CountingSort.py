from typing import List


def counting_sort(arr):
    num = max(arr)
    lst = [0]*(num+1)
    for ele in arr:
        lst[ele]+=1
    
    for i in range(1,len(lst)):
        lst[i]+=lst[i-1]

    res=[None]*len(arr)
    for ele in arr:
        res[lst[ele]-1] = ele
        lst[ele] -=1
    return res

arr=[4,2,6,7,8,4,5,2,6,7,3,8]
print(counting_sort(arr))

