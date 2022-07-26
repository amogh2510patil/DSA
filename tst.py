def ScamSort(arr):
    num = max(arr)
    lst = [None]*(num+1)
    for i,ele in enumerate(arr):
        if not lst[ele]:
            lst[ele]=i
            continue
        lst[ele]= max(lst[ele],i)

    flag=0
    res=[None]*len(arr)
    res[lst[-1]]=-1
    ma=len(lst)+1
    for i in range(len(lst)-2,-1,-1):
        if lst[i]:
            res[lst[i]]=ma
            ma=i
    return res

arr=[1,5,3,7,4,3,2]
print(ScamSort(arr))

