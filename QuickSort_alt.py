def func(arr,l,r):
    if l>=r or l<0 or r>=len(arr) :
        return
    
    i=l+1
    j=r
    while i<=j:
        if arr[i]<=arr[l]:
            i+=1
            continue
        if arr[j]>=arr[l]:
            j-=1
            continue
        arr[i],arr[j]=arr[j],arr[i]
    arr[l],arr[i-1]=arr[i-1],arr[l]
    func(arr,l,i-2)
    func(arr,i,r)
    return
arr=[9,8,7,9,6,5,4]
func(arr,0,len(arr)-1)
print(arr)
