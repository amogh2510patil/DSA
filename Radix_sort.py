
def count_sort(arr,exp):
    cnt=[0]*10
    res=[0]*len(arr)
    for val in arr:
        cnt[(val//exp)%10]+=1
    
    for i in range(1,10):
        cnt[i]+=cnt[i-1]
    
    for i in range(len(arr)-1,-1,-1):
        val=arr[i]
        ind=(val//exp)%10
        cnt[ind]-=1
        res[cnt[ind]]=val
    return res

        


def Radix_Sort(arr):
    mx=max(arr)

    exp=1
    while mx//exp>1:
        arr=count_sort(arr,exp)
        print(arr)
        exp*=10
    return arr
        
ar=[170, 45, 75, 90, 802, 24, 2, 66]
print(Radix_Sort(ar))
